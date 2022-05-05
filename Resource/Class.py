# discard

class FnChar(object):
    def __init__(self):
        self.f_type = ""

    def to_dict(self):
        return self.__dict__


class NonFnChar(object):
    def __init__(self):
        self.name = ""
        self.value = ""
        self.dataType = ""

    def to_dict(self):
        return self.__dict__


class Operation(object):
    def __init__(self):
        self.uid = "http://example.com/operation"
        self.NonFnChar_list = []            # consist nonFunctionalChar [0 ... *]

    def add_NonFnChar(self, _non_fn_char):
        # add non_functional_characteristic into operation
        if isinstance(_non_fn_char, NonFnChar):
            self.NonFnChar_list.append(_non_fn_char)

    def to_dict(self):
        result = self.__dict__
        tmp_nonFnChar_list = []
        for tmp in self.NonFnChar_list:
            tmp_nonFnChar_list.append(tmp.__dict__)
        result.pop("NonFnChar_list")
        result["Non_Functional_Characteristic"] = tmp_nonFnChar_list
        return result


class Interface:
    def __init__(self):
        self.uid = "http://example.com/interface"
        self.NonFnChar_list = []            # consist nonFunctionalChar [0 ... *]
        self.operation_list = []            # consist operation [1 ... *]

    def add_NonFnChar(self, _non_fn_char):
        # add non_functional_characteristic into interface
        if isinstance(_non_fn_char, NonFnChar):
            self.NonFnChar_list.append(_non_fn_char)

    def add_operation(self, _operation):
        # add operation into interface
        if isinstance(_operation, Operation):
            self.operation_list.append(_operation)

    def to_dict(self):
        result = {}
        result["uid"] = self.uid

        tmp_nonFnChar_list = []
        for tmp in self.NonFnChar_list:
            tmp_nonFnChar_list.append(tmp.__dict__)
        result["Non_Functional_Characteristic"] = tmp_nonFnChar_list

        tmp_operation_list = []
        for tmp in self.operation_list:
            tmp_operation_list.append(tmp.to_dict())
        return result


class Provider:
    def __init__(self):
        self.uid = "http://example.com/provider"

    def to_dict(self):
        return self.uid


class Resource:
    def __init__(self):
        # self.context = "http://www.w3.org/ns/resource.jsonld"
        self.uid = ""
        self.FnChar_list = []                   # consist FunctionalChar [1...*]
        self.provider = Provider()              # consist 1 provider
        self.interface_list = []                # consist interface [1...*]

    def set_Provider(self, _provider):
        # set resource's provider
        if isinstance(_provider, Provider):
            self.provider = _provider

    def add_FnChar(self, _fn_char):
        # add Functional_Characteristic to resource
        if isinstance(_fn_char, FnChar):
            self.FnChar_list.append(_fn_char)

    def add_interface(self, _interface):
        # add interface to resource
        if isinstance(_interface, Interface):
            self.interface_list.append(_interface)

    def to_dict(self):
        # Turn class into dict
        result = self.__dict__

        # provider class -> provider dict
        result["provider"] = self.provider.to_dict()

        # fn char class list -> fn char dict list
        tmp_FnChar_list = []
        for tmp in self.FnChar_list:
            tmp_FnChar_list.append(tmp.to_dict())
        result["Functional_Characteristic"] = tmp_FnChar_list
        result.pop("FnChar_list")

        # interface class list -> interface dict list
        tmp_interface_list = []
        for tmp in self.interface_list:
            tmp_interface_list.append(tmp.to_dict())
        result.pop("interface_list")
        result["interface"] = tmp_interface_list
        return result




