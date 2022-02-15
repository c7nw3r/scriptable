from scriptable.api import AST
from scriptable.api.AST import ASTBinding
from scriptable.api.exit_value import GoTo


class Continue(AST[GoTo]):

    def execute(self, context: ASTBinding) -> GoTo:
        return GoTo("continue")

    @staticmethod
    def parse() -> 'Continue':
        return Continue()
