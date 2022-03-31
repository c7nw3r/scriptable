from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Operator(AST[str]):
    def execute(self, binding: ASTBinding) -> str:
        pass


class And(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "and"

    def __repr__(self):
        return "and"


class Or(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "or"

    def __repr__(self):
        return "or"


class Not(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "not"

    def __repr__(self):
        return "not"


class Plus(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "+"

    def __repr__(self):
        return "+"


class Minus(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "-"

    def __repr__(self):
        return "-"


class Mul(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "*"

    def __repr__(self):
        return "*"


class Div(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "/"

    def __repr__(self):
        return "/"


class Power(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "**"

    def __repr__(self):
        return "**"


class Equals(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "=="

    def __repr__(self):
        return "=="


class NotEquals(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "!="

    def __repr__(self):
        return "!="


class LowerThan(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "<"

    def __repr__(self):
        return "<"


class LowerEquals(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return "<="

    def __repr__(self):
        return "<="


class GreaterThan(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return ">"

    def __repr__(self):
        return ">"


class GreaterEquals(Operator):

    def execute(self, binding: ASTBinding) -> str:
        return ">="

    def __repr__(self):
        return ">="
