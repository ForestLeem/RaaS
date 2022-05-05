from Constraint import *


class Party(object):
    def __init__(self, _function, _uid):
        if _function == "assigner":
            self.function = 1
        if _function == "assignee":
            self.function = 2
        self.function = _function       # 0:none, 1:assigner,  2: assignee
        self.uid = _uid
        # self.partOf = []

    def to_dict(self):
        if self.function == 1:
            return {"assigner": self.uid}
        elif self.function == 2:
            return {"assignee": self.uid}


class PartyCollection(Party):
    def __init__(self):
        super(PartyCollection, self).__init__()
        self.refinement = []  # [0 ... *] refinement

    def to_dict(self):
        return



