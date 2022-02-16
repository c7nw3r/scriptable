from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from scriptable.api.ast_binding import ASTBinding

T = TypeVar("T")


class AST(ABC, Generic[T]):

    @abstractmethod
    def execute(self, context: ASTBinding) -> T:
        pass


class EmptyAST(AST[None]):

    def execute(self, context: ASTBinding) -> None:
        return None
