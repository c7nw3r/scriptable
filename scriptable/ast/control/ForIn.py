from typing import List

from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class ForIn(AST[None]):

    def __init__(self, name: str, value: AST, tail: AST):
        self.name = name
        self.value = value
        self.tail = tail

    def execute(self, context: ASTBinding) -> None:
        if self.name in context.properties:
            raise ValueError(f"property {self.name} is already defined")

        value = self.value.execute(context)
        assert len(value) <= context.sandbox.max_loops, "max loops exceeded"

        for i, _ in enumerate(value):
            context.add_property(self.name, i)
            self.tail.execute(context)

        return None

    @staticmethod
    def parse(name: str, branch: List[AST]) -> 'ForIn':
        # noinspection PyTypeChecker
        return ForIn(name, branch[0], branch[1])
