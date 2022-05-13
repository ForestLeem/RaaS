from ODRL.Constraint import *
from ODRL.helper import *


class Action(object):
    def __init__(self):
        self.name = ""
        self.refinement_list = []       # [0 ... *] refinement (constraint)

    def add_refinement(self, _constraint):
        if isinstance(_constraint, Constraint):
            self.refinement_list.append(_constraint)

    def to_dict(self):
        if len(self.refinement_list) == 0:
            return {"action": self.name}
        else:
            action_result = {"name": self.name}
            tmp_constraint = self.refinement_list[0].to_dict()
            for i in range(1, len(self.refinement_list)):
                tmp_constraint = add_dict(tmp_constraint, self.refinement_list[i].to_dict())
            merge_dict(tmp_constraint, action_result)
            return {"action": action_result}

    def to_class(self, dict_data):
        if type({}) == type(dict_data):
            self.name = dict_data["name"]
            tmp_constraint = dict_data["refinement"]
            for i_cons in tmp_constraint:
                tmp_cons = Constraint("refinement")
                tmp_cons.leftOperand = i_cons["leftOperand"]
                tmp_cons.operator = i_cons["operator"]
                tmp_cons.rightOperand = i_cons["rightOperand"]
                tmp_cons.unit = i_cons["unit"]
                self.add_refinement(tmp_cons)
        else:
            self.name = dict_data

