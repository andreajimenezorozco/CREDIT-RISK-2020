import json
import functools


def good_format(logger, serializer_function=lambda obj: obj.dict):
    def putting_format(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            first_value = func(*args, **kwargs)
            try:
                last_value = json.dumps(first_value, indent=4, default=serializer_function)
                return last_value
            except TypeError:
                logger.error("Type Error {error}".format(error=TypeError))
                raise
        return wrapper
    return putting_format


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

    return fun_json



