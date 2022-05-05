from Action import *
from Asset import *
from Party import *
from Constraint import *
from helper import *


class Permission(object):
    def __init__(self):
        self.asset_list = []                # [1 ... *] asset
        self.party_list = []                # [0 ... *] party
        self.action = Action()              # 1 action
        self.constraint_list = []           # [0 ... *] constraint
        self.duty_list = []                 # [0 ... *] duty

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

    def add_constraint(self, _constraint):
        if isinstance(_constraint, Constraint):
            self.constraint_list.append(_constraint)

    def add_asset(self, _asset):
        if isinstance(_asset, Asset):
            self.asset_list.append(_asset)

    def to_dict(self):
        result = {}

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

        # action
        merge_dict(self.action.to_dict(), result)

        # party
        for tmp in self.party_list:
            merge_dict(tmp.to_dict(), result)

        # constraint
        if len(self.constraint_list) == 0:
            pass
        else:
            tmp_constraint = self.constraint_list[0].to_dict()
            for i in range(1, len(self.constraint_list)):
                tmp_constraint = add_dict(tmp_constraint, self.constraint_list[i].to_dict())
            merge_dict(tmp_constraint, result)

        # duty
        if len(self.duty_list) == 0:
            pass
        else:
            tmp_duty = self.duty_list[0].to_dict()
            for i in range(1, len(self.duty_list)):
                tmp_duty = add_dict(tmp_duty, self.duty_list[i].to_dict())
            merge_dict(tmp_duty, result)

        return {"permission": [result]}

