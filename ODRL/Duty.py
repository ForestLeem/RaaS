from ODRL.Action import *
from ODRL.Asset import *
from ODRL.Party import *
from ODRL.Constraint import *
from ODRL.helper import *


class Duty(object):
    def __init__(self, _type):
        self.type = _type                   # 1 obligation, 2 duty, 3 remedy, 4 consequence
        self.asset_list = []                # [0 ... *] asset
        self.party_list = []                # [0 ... *] party
        self.action = Action()              # 1 action
        self.constraint_list = []           # [0 ... *] constraint
        self.consequence_list = []          # [0 ... *] consequence (duty)

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

    def add_consequence_list(self, _consequence):
        if isinstance(_consequence, Duty):
            self.consequence_list.append(_consequence)

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

        # consequence
        if len(self.consequence_list) == 0:
            pass
        else:
            tmp_consequence = self.consequence_list[0].to_dict()
            for i in range(1, len(self.consequence_list)):
                tmp_consequence = add_dict(tmp_consequence, self.consequence_list[i].to_dict())
            merge_dict(tmp_consequence, result)

        if self.type == 1:
            return {"obligation": result}
        elif self.type == 2:
            return {"duty": result}
        elif self.type == 3:
            return {"remedy": result}
        elif self.type == 4:
            return {"consequence": result}

    def to_class(self, dict_data):
        # asset
        if "target" in dict_data.keys():
            tmp_asset_list = dict_data["target"]
            if type([]) == type(tmp_asset_list):
                for i in tmp_asset_list:
                    new_asset = Asset("target", tmp_asset_list[i])
                    self.add_asset(new_asset)
            else:
                self.add_asset(Asset("target", tmp_asset_list))

        # action
        if "action" in dict_data.keys():
            tmp_action = Action()
            tmp_action.to_class(dict_data["action"])
            self.action = tmp_action

            # party
            if "assignee" in dict_data.keys():
                _assignee = Party("assignee", dict_data["assignee"])
                self.add_party(_assignee)

            if "assigner" in dict_data.keys():
                _assigner = Party("assigner", dict_data["assigner"])
                self.add_party(_assigner)

        # constraint
        if "constraint" in dict_data.keys():
            for i_cons in dict_data["constraint"]:
                tmp_cons = Constraint("constraint")
                tmp_cons.leftOperand = i_cons["leftOperand"]
                tmp_cons.operator = i_cons["operator"]
                tmp_cons.rightOperand = i_cons["rightOperand"]
                tmp_cons.unit = i_cons["unit"]
                self.add_constraint(tmp_cons)

        # consequence obligation
        if "consequence" in dict_data.keys():
            for i_consequence in dict_data["consequence"]:
                tmp_consequence = Duty(4)
                tmp_consequence.to_class(i_consequence)
                self.add_consequence_list(tmp_consequence)

        return
