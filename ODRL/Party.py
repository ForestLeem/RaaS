from ODRL.Constraint import *


class Party(object):
    def __init__(self, _function, _uid):
        self.function = _function       #  assigner,  assignee
        self.uid = _uid
        # self.partOf = []

    def to_dict(self):
        return {self.function: self.uid}


class PartyCollection(Party):
    def __init__(self):
        super(PartyCollection, self).__init__()
        self.refinement = []  # [0 ... *] refinement

    def to_dict(self):
        return



