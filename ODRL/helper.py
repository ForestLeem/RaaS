import json


def merge_dict(dict1, dict2):
    # different key
    return dict2.update(dict1)


def add_dict(dict1, dict2):
    # same key,
    tmp_key = list(dict1.keys())
    tmp_value = []
    result = {}

    for tmp in tmp_key:
        tmp_data = dict1[tmp]
        if type([]) == type(tmp_data):
            tmp_value += tmp_data
        else:
            tmp_value.append(tmp_data)

        tmp_data = dict2[tmp]
        if type([]) == type(tmp_data):
            tmp_value += tmp_data
        else:
            tmp_value.append(tmp_data)
        result[tmp] = tmp_value

    return result


def my_obj_pairs_hook(lst):
    result = {}
    count = {}
    for key, val in lst:
        if key in count:
            count[key] = 1 + count[key]
        else:
            count[key] = 1

        if key in result:
            if count[key] > 2:
                result[key].append(val)
            else:
                result[key] = [result[key], val]
        else:
            result[key] = val
    return result


def dict_to_json(data, indent, deep=1):
    result = ""
    for key in data.keys():
        tmp_value = data[key]
        result += "\n"
        for i in range(0, indent * deep):
            result += " "
        if (type(tmp_value) == type([])):
            # list
            if(len(tmp_value) > 1):
                for i in range(0, len(tmp_value)):
                    if(i != 0):
                        result += "\n"
                        for j in range(0, indent * deep):
                            result += " "
                    result += '"'
                    result += str(key)
                    result += '": '
                    if (type(tmp_value[i]) == type([])):
                        result += list_to_json(tmp_value[i], indent, deep + 1)
                    elif (type(tmp_value[i]) == type({})):
                        result += dict_to_json(tmp_value[i], indent, deep + 1)
                    else:
                        result += str(tmp_value[i])

                    if (i != (len(tmp_value)-1)):
                        result += ', '
            else:
                result += '"'
                result += str(key)
                result += '": '
                result += list_to_json(tmp_value, indent, deep+1)

        elif (type(tmp_value) == type({})):
            #dict
            result += '"'
            result += str(key)
            result += '": '
            result += dict_to_json(tmp_value, indent, deep+1)
        else:
            result += '"'
            result += str(key)
            result += '": '
            result += '"'
            result += str(tmp_value)
            result += '"'

        if (key != list(data.keys())[-1]):
            result += ', '

    if(len(data.keys()) == 0):
        return "{" + result + "}"

    if(deep != 1):
        indent_b = "\n"
        indent_e = "\n"
    else:
        indent_b = ""
        indent_e = ""
    for i in range(0, indent*(deep - 1)):
        indent_b += " "

    for i in range(0, indent * (deep - 1)):
        indent_e += " "
    if(deep == 1):
        return indent_b + "{" + result + indent_e + "\n}"
    return indent_b + "{" + result + indent_e + "}"


def list_to_json(data, indent, deep=1):
    result = ""
    for tmp_data in data:
        if (type(tmp_data) == type([])):
            result += list_to_json(tmp_data, indent, deep+1)
        elif (type(tmp_data) == type({})):
            result += dict_to_json(tmp_data, indent, deep+1)
        else:
            result += str(tmp_data)
    return "[" + result + "]"
