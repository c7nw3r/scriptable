from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class And(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "and"

    def __repr__(self):
        return "and"


class Or(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "or"

    def __repr__(self):
        return "or"


class Not(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "not"

    def __repr__(self):
        return "not"


class Plus(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "+"

    def __repr__(self):
        return "+"


class Minus(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "-"

    def __repr__(self):
        return "-"


class Mul(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "*"

    def __repr__(self):
        return "*"


class Div(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "/"

    def __repr__(self):
        return "/"


class Power(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "**"

    def __repr__(self):
        return "**"


class Equals(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "=="

    def __repr__(self):
        return "=="


class NotEquals(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "!="

    def __repr__(self):
        return "!="


class LowerThan(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "<"

    def __repr__(self):
        return "<"


class LowerEquals(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return "<="

    def __repr__(self):
        return "<="


class GreaterThan(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return ">"

    def __repr__(self):
        return ">"


class GreaterEquals(AST[str]):

    def execute(self, binding: ASTBinding) -> str:
        return ">="

    def __repr__(self):
        return ">="
