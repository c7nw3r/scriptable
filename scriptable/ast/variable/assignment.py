from scriptable.api import AST
from scriptable.api.accessor import Accessor
from scriptable.api.ast_binding import ASTBinding
from scriptable.ast.property import PropertyAccess, Property


class Assignment(AST[None]):
    def __init__(self, target: AST, source: AST):
        self.source = source
        self.target = target

    def execute(self, binding: ASTBinding) -> None:
        value = self.source.execute(binding)

        if isinstance(self.target, PropertyAccess):
            def unwrap(obj):
                if isinstance(obj, Accessor):
                    return obj.value
                return obj

            branch = list(map(lambda ast: ast.execute(binding), self.target.branch))
            current = branch.pop(0)
            while len(branch) > 1:
                current = current[unwrap(branch.pop(0))]

            current[unwrap(branch.pop(0))] = value
            return None

        if isinstance(self.target, Property):
            binding.add_property(self.target.value, value)
            return None

        raise ValueError("cannot handle " + str(self.target))

    @staticmethod
    def parse(target: AST, source: AST) -> 'Assignment':
        return Assignment(target, source)
