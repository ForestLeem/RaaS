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

    def to_interface(self, dict_data):
        # Turn dict into class
        self.uid = dict_data["uid"]

        if "description" in dict_data.keys():
            self.description = dict_data["description"]

        # add Non_fnchar
        tmp_non_fnchar_list = dict_data["Non_Functional_Characteristic"]
        for tmp_non_fnchar in tmp_non_fnchar_list:
            if "description" in tmp_non_fnchar.keys():
                tmp_non_fnchar_class = NonFnChar(tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                                 tmp_non_fnchar["dataType"], tmp_non_fnchar["description"])
            else:
                tmp_non_fnchar_class = NonFnChar(tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                                 tmp_non_fnchar["dataType"])
            self.add_NonFnChar(tmp_non_fnchar_class)

        # add operation
        tmp_operation_list = dict_data["operation"]
        for tmp_operation in tmp_operation_list:
            tmp_operation_class = Operation()
            tmp_operation_class.uid = tmp_operation["uid"]
            if "description" in tmp_operation.keys():
                tmp_operation_class.description = tmp_operation["description"]

            # add Non_fnchar in operation
            tmp_non_fnchar_list = tmp_operation["Non_Functional_Characteristic"]
            for tmp_non_fnchar in tmp_non_fnchar_list:
                if "description" in tmp_non_fnchar.keys():
                    tmp_non_fnchar_class = NonFnChar(tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                                     tmp_non_fnchar["dataType"], tmp_non_fnchar["description"])
                else:
                    tmp_non_fnchar_class = NonFnChar(tmp_non_fnchar["name"], tmp_non_fnchar["value"],
                                                     tmp_non_fnchar["dataType"])
                tmp_operation_class.add_NonFnChar(tmp_non_fnchar_class)

            self.add_operation(tmp_operation_class)
