from Resource.Provider import Provider
from Resource.Func_Char import FnChar
from Resource.Interface import Interface
from Resource.Operation import Operation


class Resource:
    def __init__(self):
        self.context = "http://www.w3.org/ns/resource.jsonld"
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
        result = {"@context": self.context, "uid": self.uid, "provider": self.provider.to_dict()}

        # fn char class list -> fn char dict list
        tmp_FnChar_list = []
        for tmp in self.FnChar_list:
            tmp_FnChar_list.append(tmp.to_dict())
        result["Functional_Characteristic"] = tmp_FnChar_list

        # interface class list -> interface dict list
        tmp_interface_list = []
        for tmp in self.interface_list:
            tmp_interface_list.append(tmp.to_dict())
        result["interface"] = tmp_interface_list
        return result
