from typing import Any, List, Optional

from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import ExitValue, GoTo


class If(AST[Optional[Any]]):

    def __init__(self, if_branch: List[AST], else_if_branch: List[AST], else_branch: List[AST]):
        self.if_branch = if_branch
        self.else_if_branch = else_if_branch
        self.else_branch = else_branch

    def execute(self, binding: ASTBinding) -> Optional[Any]:
        expression = self.if_branch[0].execute(binding)
        if expression:
            for branch in self.if_branch[1:]:
                result = branch.execute(binding)
                if isinstance(result, ExitValue):
                    return result
                if isinstance(result, GoTo):
                    return result

        for branch in self.else_if_branch:
            result = branch.execute(binding)
            if isinstance(result, ExitValue):
                return result
            if isinstance(result, GoTo):
                return result

        for branch in self.else_branch:
            result = branch.execute(binding)
            if isinstance(result, ExitValue):
                return result
            if isinstance(result, GoTo):
                return result

        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'If':
        if_branch = list(filter(lambda x: not isinstance(x, ElseIf) and not isinstance(x, Else), branch))
        else_if_branch = list(filter(lambda x: isinstance(x, ElseIf), branch))
        else_branch = list(filter(lambda x: isinstance(x, Else), branch))

        return If(if_branch, else_if_branch, else_branch)


class ElseIf(AST[Optional[Any]]):

    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> Optional[Any]:
        expression = self.branch[0].execute(binding)
        if expression:
            for branch in self.branch[1:]:
                result = branch.execute(binding)
                if isinstance(result, ExitValue):
                    return result
                if isinstance(result, GoTo):
                    return result
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'ElseIf':
        return ElseIf(branch)


class Else(AST[Optional[Any]]):

    def __init__(self, branch: List[AST]):
        self.branch = branch

    def execute(self, binding: ASTBinding) -> Optional[Any]:
        for branch in self.branch:
            result = branch.execute(binding)
            if isinstance(result, ExitValue):
                return result
            if isinstance(result, GoTo):
                return result
        return None

    @staticmethod
    def parse(branch: List[AST]) -> 'Else':
        return Else(branch)
