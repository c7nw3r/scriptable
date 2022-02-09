from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class And(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "and"


class Or(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "or"


class Not(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "not"


class Plus(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "+"


class Minus(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "-"


class Mul(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "*"


class Div(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "/"


class Power(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "**"
