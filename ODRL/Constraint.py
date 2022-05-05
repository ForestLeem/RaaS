class Constraint(object):
    def __init__(self, _type):
        self.type = _type           # constraint, refinement
        self.uid = None
        self.leftOperand = ""
        self.operator = ""
        self.rightOperand = ""
        self.dataType = None
        self.unit = None
        self.status = None

    def to_dict(self):
        tmp_result = self.__dict__.copy()
        tmp_result.pop("type")
        keys = list(tmp_result.keys())
        for tmp_key in keys:
            if tmp_result[tmp_key] is None:
                tmp_result.pop(tmp_key)

        return {self.type: [tmp_result]}


