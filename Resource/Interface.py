from Resource.Operation import Operation
from Resource.Non_Func_Char import NonFnChar


class Interface:
    def __init__(self):
        self.uid = "http://example.com/interface"
        self.description = ""
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
        result = {"uid": self.uid}
        if self.description != "":
            result["description"] = self.description

        tmp_nonFnChar_list = []
        for tmp in self.NonFnChar_list:
            tmp_nonFnChar_list.append(tmp.__dict__)
        result["Non_Functional_Characteristic"] = tmp_nonFnChar_list

        tmp_operation_list = []
        for tmp in self.operation_list:
            tmp_operation_list.append(tmp.to_dict())
        result["operation"] = tmp_operation_list
        return result
