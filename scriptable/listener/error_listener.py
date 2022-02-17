from dataclasses import dataclass
from typing import List

from antlr4.error.ErrorListener import ErrorListener


class ScriptableErrorListener(ErrorListener):
    errors: List['ScriptableError'] = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if "no viable alternative at input" in msg:
            _msg = "compiler error: " + msg[len("no viable alternative at input"):]
            self.errors.append(ScriptableError(_msg, line, column))
        else:
            self.errors.append(ScriptableError(msg, line, column))

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass


@dataclass
class ScriptableError:
    msg: str
    line: int
    column: int

    def __repr__(self):
        return f"{self.msg} at {self.line}:{self.column}"
