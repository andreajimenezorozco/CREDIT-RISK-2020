import json


def flatten_json(dicc):
    j = {}

    # print("dict:",dicc)
    def flatten(dicc, character=''):
        # print("list",dicc)
        if type(dicc) is dict:
            for args in dicc:
                flatten(dicc[args], character + args + '.')
        elif type(dicc) is list:
            i = 0
            for args in dicc:
                flatten(args, character + str(i) + '.')
                i += 1
        else:
            j[character[:-1]] = dicc

    flatten(dicc)
    return json.dumps(j, indent=3, sort_keys=True)