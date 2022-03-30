from typing import Any, List

from scriptable.api.accessor import Accessor


class TypescriptStringAccessor(Accessor[str]):

    def __init__(self, value: str):
        self.value = value

    def __getitem__(self, item):
        if isinstance(item, int):
            return self.value[item]
        if item == "length":
            return len(self.value)
        raise ValueError(f"{item} property value access is not supported")

    def __call__(self, name: str, args: List[Any]):
        if name == "slice":
            return self._slice(args)
        if name == "substring":
            return self._substring(args)
        if name == "substr":
            return self._substr(args)
        if name == "replace":
            return self._replace(args)
        if name == "toUpperCase":
            return self.value.upper()
        if name == "toLowerCase":
            return self.value.lower()
        if name == "concat":
            return self._concat(args)
        if name == "trim":
            return self.value.strip()
        if name == "padStart":
            return self._pad_start(args)
        if name == "padEnd":
            return self._pad_end(args)
        if name == "charAt":
            return self._char_at(args)
        if name == "charCodeAt":
            return self._char_code_at(args)
        if name == "split":
            return self._split(args)
        raise ValueError(f"{name} function value access is not supported")

    def _slice(self, args: List[Any]):
        if len(args) == 1:
            if args[0] < 0:
                args[0] = len(self.value) + args[0]
            return self.value[args[0]:]
        else:
            if args[0] < 0:
                args[0] = len(self.value) + args[0]
            if args[1] < 0:
                args[1] = len(self.value) + args[1]
            return self.value[args[0]: args[1]]

    def _substring(self, args: List[Any]):
        if len(args) == 1:
            return self.value[args[0]:]
        return self.value[args[0]: args[1]]

    def _substr(self, args: List[Any]):
        if len(args) == 1:
            return self.value[args[0]:]
        return self.value[args[0]:args[0] + args[1]]

    def _replace(self, args: List[Any]):
        assert len(args) == 2, f"invalid arguments for replace {args}"
        assert isinstance(args[0], TypescriptStringAccessor), "argument is not a string"
        assert isinstance(args[1], TypescriptStringAccessor), "argument is not a string"
        return self.value.replace(args[0].value, args[1].value)

    def _concat(self, args: List[Any]):
        assert len(args) == 1, f"invalid arguments for concat {args}"
        assert isinstance(args[0], TypescriptStringAccessor), "argument is not a string"
        return TypescriptStringAccessor(self.value + args[0].value)

    def _pad_start(self, args: List[Any]):
        assert len(args) == 2, f"invalid arguments for replace {args}"
        assert isinstance(args[0], int), "argument is not an int"
        return self.value.rjust(args[0], str(args[1]))

    def _pad_end(self, args: List[Any]):
        assert len(args) == 2, f"invalid arguments for replace {args}"
        assert isinstance(args[0], int), "argument is not an int"
        return self.value.ljust(args[0], str(args[1]))

    def _char_at(self, args: List[Any]):
        assert len(args) == 1, f"invalid arguments for replace {args}"
        assert isinstance(args[0], int), "argument is not an int"
        return self.value[args[0]]

    def _char_code_at(self, args: List[Any]):
        assert len(args) == 1, f"invalid arguments for replace {args}"
        assert isinstance(args[0], int), "argument is not an int"
        return ord(self.value[args[0]])

    def _split(self, args: List[Any]):
        assert len(args) == 1, f"invalid arguments for replace {args}"
        assert isinstance(args[0], TypescriptStringAccessor), "argument is not a string"
        return self.value.split(args[0].value)

    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return self.value

    def __contains__(self, item):
        if isinstance(item, int):
            return len(self.value) >= item
        return item in self.value