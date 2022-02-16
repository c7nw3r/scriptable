from scriptable.api import AST
from scriptable.api.ast_binding import ASTBinding


class Decrement(AST[None]):
    def __init__(self, name: str):
        self.name = name

    def execute(self, binding: ASTBinding) -> None:
        value = binding.properties[self.name]
        binding.add_property(self.name, value - 1)
        return None

    @staticmethod
    def parse(name: str) -> 'Decrement':
        return Decrement(name)
