import json

from .utils import good_format
from .utils import flatten_dict
from fintools.settings import get_logger

logger = get_logger(name="__main__")


class Main(object):
    @good_format
    def show(self, file):
        logger.info("Calling the show method.")
        with open(file, "r") as f:
            content = json.loads(f.read())
        return content

    @staticmethod
    def flatten(file):
        with open(file, "r") as f:
            example = json.loads(f.read())
        return flatten_dict(example)
