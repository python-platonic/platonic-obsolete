from .mapping import Mapping


class DictMapping(dict, Mapping):
    """Implementation of a Mapping based on a standard dict."""
