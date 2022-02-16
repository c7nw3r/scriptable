from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class MutableVar(AST[None]):
    def __init__(self, name: str, value: AST):
        self.name = name
        self.value = value

    def execute(self, binding: ASTBinding) -> None:
        binding.add_property(self.name, self.value.execute(binding))
        return None

    @staticmethod
    def parse(name: str, value: AST) -> 'MutableVar':
        return MutableVar(name, value)
