from Resource.Non_Func_Char import NonFnChar


class Operation(object):
    def __init__(self):
        self.uid = "http://example.com/operation"
        self.description = ""
        self.NonFnChar_list = []            # consist nonFunctionalChar [0 ... *]

    def add_NonFnChar(self, _non_fn_char):
        # add non_functional_characteristic into operation
        if isinstance(_non_fn_char, NonFnChar):
            self.NonFnChar_list.append(_non_fn_char)

    def to_dict(self):
        result = {"uid": self.uid}
        if self.description != "":
            result["description"] = self.description
        tmp_nonFnChar_list = []
        for tmp in self.NonFnChar_list:
            tmp_nonFnChar_list.append(tmp.__dict__)
        result["Non_Functional_Characteristic"] = tmp_nonFnChar_list
        return result
