class QoS:
    def __init__(self, _name="", _value="", _operator="", _unit=None):
        self.name = _name
        self.value = _value
        self.operator = _operator
        self.unit = _unit

    def to_dict(self):
        return self.__dict__
