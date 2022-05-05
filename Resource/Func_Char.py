class FnChar(object):
    def __init__(self):
        self.f_type = ""
        self.description = ""

    def to_dict(self):
        result = self.__dict__
        if self.description == "":
            result.pop("description")
        return result
