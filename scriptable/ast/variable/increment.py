from scriptable.api import AST
from scriptable.api.AST import ASTBinding


class Increment(AST[None]):
    def __init__(self, name: str):
        self.name = name

    def execute(self, binding: ASTBinding) -> None:
        value = binding.properties[self.name]
        binding.add_property(self.name, value + 1)
        return None

    @staticmethod
    def parse(name: str) -> 'Increment':
        return Increment(name)
