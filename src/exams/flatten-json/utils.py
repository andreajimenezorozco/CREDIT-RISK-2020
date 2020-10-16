import json


def flatten_dict(dicc):
    res = {}
    def flatten(dicc, character=''):
        if type(dicc) is dict:
            for args in dicc:
                flatten(dicc[args], character + args + '.')
        elif type(dicc) is list:
            i = 0
            for args in dicc:
                flatten(args, character + str(i) + '.')
                i += 1
        else:
            res[character[:-1]] = dicc

    flatten(dicc)
    return json.dumps(res, indent=3, sort_keys=True)


