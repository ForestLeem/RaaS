class Consumer:
    def __init__(self, _uid=""):
        self.uid = _uid

    def to_dict(self):
        return self.uid
