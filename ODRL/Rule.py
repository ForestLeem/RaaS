from ODRL.Permission import *
from ODRL.Prohibition import *
from ODRL.Duty import *
from ODRL.Action import *
from ODRL.Asset import *
from ODRL.Party import *
from ODRL.Constraint import *
from ODRL.helper import *


# duty_name_ = {"permission": "duty", "prohibition": "remedy", "obligation": "consequence"}


class Rule(object):
    def __init__(self, _type):
        self.type = _type
        self.asset_list = []                # [1 ... *] asset
        self.party_list = []                # [0 ... *] party
        self.action = Action()              # 1 action
        self.constraint_list = []           # [0 ... *] constraint
        self.duty_list = []                 # [0 ... *] duty

        # self.duty_name = duty_name_[_type]

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

    def add_duty(self, _duty):
        if isinstance(_duty, Duty):
            self.duty_list.append(_duty)

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

        return {self.type: [result]}

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

        # duty permission
        if "duty" in dict_data.keys():
            for i_duty in dict_data["duty"]:
                tmp_duty = Duty(2)
                tmp_duty.to_class(i_duty)
                self.add_duty(tmp_duty)

        # remedy prohibition
        if "remedy" in dict_data.keys():
            for i_remedy in dict_data["remedy"]:
                tmp_remedy = Duty(3)
                tmp_remedy.to_class(i_remedy)
                self.add_duty(tmp_remedy)

        # consequence obligation
        if "consequence" in dict_data.keys():
            for i_consequence in dict_data["consequence"]:
                tmp_consequence = Duty(4)
                tmp_consequence.to_class(i_consequence)
                self.add_duty(tmp_consequence)

        pass
