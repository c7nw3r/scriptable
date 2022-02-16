from typing import List

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import GoTo


class ForOf(AST[None]):

    def __init__(self, name: str, value: AST, tail: AST):
        self.name = name
        self.value = value
        self.tail = tail

    def execute(self, context: ASTBinding) -> None:
        if self.name in context.properties:
            raise ValueError(f"property {self.name} is already defined")

        value = self.value.execute(context)
        assert len(value) <= context.restrictions.max_loops, "max loops exceeded"

        if isinstance(value, str):
            for char in value:
                context.add_property(self.name, char)
                result = self.tail.execute(context)

                if isinstance(result, GoTo) and result.value == "break":
                    break
                if isinstance(result, GoTo) and result.value == "continue":
                    continue
        else:
            for item in value:
                context.add_property(self.name, item)
                result = self.tail.execute(context)

                if isinstance(result, GoTo) and result.value == "break":
                    break
                if isinstance(result, GoTo) and result.value == "continue":
                    continue

        return None

    @staticmethod
    def parse(name: str, branch: List[AST]) -> 'ForOf':
        # noinspection PyTypeChecker
        return ForOf(name, branch[0], branch[1])
