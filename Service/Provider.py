class Provider:
    def __init__(self, _uid=""):
        self.uid = _uid
        self.description = ""

    def to_dict(self):
        result = {"uid": self.uid}
        if self.description != "":
            result["description"] = self.description
        return result
