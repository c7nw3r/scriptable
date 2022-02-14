from typing import Any, List, Dict

from scriptable.api.accessor import Accessor


class MapAccessor(Accessor[Dict[str, Any]]):

    def __init__(self, value: Dict[str, Any]):
        self.value = value

    def __getitem__(self, item):
        raise ValueError(f"{item} property value access is not supported")

    def __call__(self, name: str, args: List[Any]):
        raise ValueError(f"{name} function value access is not supported")

    def __repr__(self):
        return ", ".join(map(str, self.value))
