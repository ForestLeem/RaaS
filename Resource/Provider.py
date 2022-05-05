class Provider:
    def __init__(self):
        self.uid = "http://example.com/provider"

    def to_dict(self):
        return self.uid
