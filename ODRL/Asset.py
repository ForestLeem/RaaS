from ODRL.Constraint import *
from ODRL.helper import *


class Asset(object):
    def __init__(self, _relation, _uid):
        self.relation = _relation
        self.uid = _uid
        self.refinement = []

    def add_refinement(self, _refinement):
        if isinstance(_refinement, Constraint):
            self.refinement.append(_refinement)

    def to_dict(self):
        if len(self.refinement) == 0:
            return {self.relation: self.uid}
        else:
            result = {"source": self.uid}

            tmp_refinement = self.refinement[0].to_dict()
            for i in range(1, len(self.refinement)):
                tmp_consequence = add_dict(tmp_refinement, self.refinement[i].to_dict())
            merge_dict(tmp_refinement, result)

            return {self.relation: result}

    def to_class(self, dict_data):
        pass

