import os
import functools
import json

INDUSTRY_SEARCH_DEFAULT_FILENAME = os.environ.get(
    "INDUSTRY_SEARCH_DEFAULT_FILENAME",
    default="./sic-industry/industries.json"
)

INDUSTRY_SEARCH_DEFAULT_THRESHOLD = float(os.environ.get(
    "INDUSTRY_SEARCH_DEFAULT_THRESHOLD",
    default="0.5"
))


def good_format(logger, serializer_function=lambda obj: obj.__dict__):
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

