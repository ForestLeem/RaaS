def merge_dict(dict1, dict2):
    return dict2.update(dict1)


class Permission(object):
    def __init__(self):
        self.asset_list = []                # [1 ... *] asset
        self.party_list = []                # [0 ... *] party
        self.action = Action()              # 1 action
        self.constraint_list = []           # [0 ... *] constraint

    def to_dict(self):
        result = {}
        merge_dict(self.action.to_dict(), result)
        return result


class Prohibition(object):
    def __init__(self):
        self.asset_list = []  # [1 ... *] asset
        self.party_list = []  # [0 ... *] party
        self.action = Action()  # 1 action
        self.constraint_list = []  # [0 ... *] constraint
        return


class Constraint(object):
    def __init__(self):
        self.leftOperand = ""
        self.operator = ""
        self.rightOperand = ""


class Asset(object):
    def __init__(self):
        self.uid = ""

    def to_dict(self):
        return {"target": self.uid}


class Action(object):
    def __init__(self):
        self.name = ""

    def to_dict(self):
        return {"action": self.name}


class Policy(object):
    def __init__(self):
        self.inheritForm = ""
        self.profile = ""
        self.type = ""
        self.uid = ""
        self.permission = []
        self.prohibition = []
        self.obligation = []

    def to_dict(self):
        return


