from dataclasses import dataclass


@dataclass
class ASTRestrictions:
    max_precision = 10  # The max allowed number of digits in a number.
    max_scale = 4  # The max allowed digits to the right of the decimal point in a number.
    max_loops = 10 # The max allowed number of loop iterations.
