from ODRL.Action import *
from ODRL.Asset import *
from ODRL.Party import *
from ODRL.Constraint import *
from ODRL.Permission import *
from ODRL.Prohibition import *
from ODRL.Duty import *
from ODRL.helper import *
import json


class Policy(object):
    def __init__(self, _type, _uid):
        self.context = "http://www.w3.org/ns/odrl.jsonld"
        # self.inheritForm = None
        self.profile = None
        self.type = _type
        self.uid = _uid
        self.party_list = []             # [0 ... *] party (assigner, assignee)
        self.asset_list = []             # [0 ... *] asset (mainly target)
        self.action = []                 # [0 ... *] action
        self.permission = []             # [0 ... *]
        self.prohibition = []            # [0 ... *]
        self.obligation = []             # [0 ... *]

    def add_permission(self, _permission):
        # add permission
        if isinstance(_permission, Permission):
            self.permission.append(_permission)

    def add_prohibition(self, _prohibition):
        # add prohibition
        if isinstance(_prohibition, Prohibition):
            self.prohibition.append(_prohibition)

    def add_obligation(self, _obligation):
        # add obligation (duty)
        if isinstance(_obligation, Duty):
            self.obligation.append(_obligation)

    def add_party(self, _party):
        if isinstance(_party, Party):
            # get function to know assigner or assignee
            function_type = _party.function

            for tmp in self.party_list:
                # replace the party
                if function_type == tmp.function:
                    self.party_list.remove(tmp)
                    self.party_list.append(_party)
                    return

            # add party
            self.party_list.append(_party)
        return

    def add_asset(self, _asset):
        if isinstance(_asset, Asset):
            self.asset_list.append(_asset)

    def to_dict(self):
        result = {"@context": self.context, "@type": self.type, "uid": self.uid}
        if self.profile is not None:
            result["profile"] = self.profile

        # asset
        if len(self.asset_list) == 0:
            # no asset
            pass
        if len(self.asset_list) == 1:
            # 1 asset (target)
            merge_dict(self.asset_list[0].to_dict(), result)

        else:
            # 2 or more assets (targets)
            tmp_asset = []
            for tmp in self.asset_list:
                tmp_asset.append(tmp.uid)
            tmp_target = {"target": tmp_asset}
            merge_dict(tmp_target, result)

        # party
        for tmp in self.party_list:
            merge_dict(tmp.to_dict(), result)

        # permission
        if len(self.permission) == 0:
            pass
        else:
            tmp_permission = self.permission[0].to_dict()
            for i in range(1, len(self.permission)):
                tmp_permission = add_dict(tmp_permission, self.permission[i].to_dict())
            merge_dict(tmp_permission, result)

        # prohibition
        if len(self.prohibition) == 0:
            pass
        else:
            tmp_prohibition = self.prohibition[0].to_dict()
            for i in range(1, len(self.prohibition)):
                tmp_prohibition = add_dict(tmp_prohibition, self.prohibition[i].to_dict())
            merge_dict(tmp_prohibition, result)

        # obligation
        if len(self.obligation) == 0:
            pass
        else:
            tmp_obligation = self.obligation[0].to_dict()
            for i in range(1, len(self.obligation)):
                tmp_obligation = add_dict(tmp_obligation, self.obligation[i].to_dict())
            merge_dict(tmp_obligation, result)

        return result


# test = Policy("Agreement", "http://example.com/policy:01")
# a = Party(1, "http://example.com/provider:01")
# c = Party(2, "http://example.com/client1/")
# b = Permission()
# b.add_party(a)
# b.add_party(c)
# tmp2 = Asset("http://example.com/document:1234")
# tmp1 = Constraint(1)
# b.add_asset(tmp2)
# print(tmp1.to_dict())
# b.add_constraint(tmp1)
# test.add_permission(b)
# mm = test.to_dict()
#
# print(json.dumps(mm, indent=2))
#

