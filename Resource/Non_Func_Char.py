class NonFnChar(object):
    def __init__(self, _name="", _value="", _data_type="", _description=""):
        self.name = _name
        self.value = _value
        self.dataType = _data_type
        self.description = _description

    def to_dict(self):
        result = self.__dict__
        if self.description == "":
            result.pop("description")
        return result
