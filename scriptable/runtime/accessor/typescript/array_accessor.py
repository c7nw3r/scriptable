from typing import Any, List

from scriptable.api.accessor import Accessor


class ArrayAccessor(Accessor[List[Any]]):

    def __init__(self, value: List[Any]):
        self.value = value

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.value[item]
        raise ValueError(f"{item} property value access is not supported")

    def __call__(self, name: str, args: List[Any]):
        if name == "sort":
            return self._sort(args)
        if name == "push":
            self.value.append(args[0])
            return None

        raise ValueError(f"{name} function value access is not supported")

    def _sort(self, args: List[Any]):
        def compare(a, b):
            return args[0]([a, b])
        from functools import cmp_to_key
        return sorted(self.value, key=cmp_to_key(compare))

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return ", ".join(map(str, self.value))
