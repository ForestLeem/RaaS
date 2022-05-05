class NonFnChar(object):
    def __init__(self):
        self.name = ""
        self.value = ""
        self.dataType = ""
        self.description = ""

    def to_dict(self):
        result = self.__dict__
        if self.description == "":
            result.pop("description")
        return result
