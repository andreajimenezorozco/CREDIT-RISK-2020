import json


def flatten_dict(fun_json):
    res = {}

    def flatten(dic1, character=''):

        if type(dic1) is dict:
            for args in dic1:
                flatten(dic1[args], character + args + '.')
        elif type(dic1) is list:
            i = 0
            for args in dic1:
                flatten(args, character + str(i) + '.')
                i += 1
        else:
            res[character[:-1]] = dic1

    flatten(fun_json)
    return json.dumps(res, indent=2, sort_keys=True)



