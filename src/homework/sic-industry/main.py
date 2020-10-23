import os
import json
from typing import Dict

from fintools.settings import get_logger
from fintools.utils import StringWrapper, timeit

from .settings import (
    INDUSTRY_SEARCH_DEFAULT_FILENAME,
    INDUSTRY_SEARCH_DEFAULT_THRESHOLD
)

logger = get_logger(name=__name__)


class Main:
    threshold = INDUSTRY_SEARCH_DEFAULT_THRESHOLD

    def _recursive_search(self, node, string_wrapper, exact):
        title = node["title"]
        children = node["children"]
        new_children = []

        for child in children:
            is_child_valid = self._recursive_search(child, string_wrapper, exact=exact)
            if is_child_valid:
                new_children.append(child)

        node["children"] = new_children
        search = len(new_children) or string_wrapper.boolean_search(title, reverse=True, exact=exact)
        return search

    @timeit(logger)
    def search(self, title: str, exact: bool = False, filename: str = INDUSTRY_SEARCH_DEFAULT_FILENAME):
        target_tittle = StringWrapper(value=title)
        sic_industries = json.loads(filename)
        children = sic_industries["children"]
        new_children = []
        for child in children:
            if self._recursive_search(child, target_tittle, exact=exact):
                new_children.append(child)
        return new_children
