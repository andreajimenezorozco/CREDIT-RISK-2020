import json

from fintools.settings import get_logger
from fintools.utils import StringWrapper, timeit

from .settings import (
    INDUSTRY_SEARCH_DEFAULT_FILENAME,
    INDUSTRY_SEARCH_DEFAULT_THRESHOLD
)
from .settings import good_format

logger = get_logger(name=__name__)


class Main:
    threshold = INDUSTRY_SEARCH_DEFAULT_THRESHOLD

    @staticmethod
    def load_json(filename=INDUSTRY_SEARCH_DEFAULT_FILENAME):
        with open(filename, "r") as f:
            sic_industry = json.loads(f.read())
        return sic_industry

    def recursive_search(self, node, string_wrapper, exact):
        title = node["title"]
        children = node["children"]
        new_children = []

        for child in children:
            is_child_valid = self.recursive_search(child, string_wrapper, exact=exact)
            if is_child_valid:
                new_children.append(child)
        node["children"] = new_children
        result = len(new_children) or string_wrapper.boolean_search(title, threshold=INDUSTRY_SEARCH_DEFAULT_THRESHOLD,
                                                                    reverse=True, exact=exact)
        return result

    @timeit(logger=logger)
    @good_format(logger)
    def search(self, title: str, exact: bool = False, file: str = INDUSTRY_SEARCH_DEFAULT_FILENAME):
        target_tittle = StringWrapper(value=title)
        sic_industries = self.load_json(file)
        children = sic_industries["children"]
        new_children = []
        for child in children:
            if self.recursive_search(child, target_tittle, exact=exact):
                new_children.append(child)
        return new_children


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(Main)
