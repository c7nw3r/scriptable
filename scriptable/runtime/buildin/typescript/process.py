from typing import Any, Dict


class Process:

    def __init__(self, context: Dict[str, Any]):
        self.context = context

    def __call__(self, *args):
        pass

    def __getitem__(self, item):
        if item == "env":
            return self.context
        raise ValueError(f"cannot handle {item}")
