from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding
from scriptable.api.exit_value import GoTo


class Break(AST[GoTo]):

    def execute(self, context: ASTBinding) -> GoTo:
        return GoTo("break")

    @staticmethod
    def parse() -> 'Break':
        return Break()
