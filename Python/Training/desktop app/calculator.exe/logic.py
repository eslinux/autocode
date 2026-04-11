# calculator logic: evaluate expressions safely
import math

ALLOWED_NAMES = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
ALLOWED_NAMES.update({
    'abs': abs,
    'round': round,
})


def evaluate_expression(expr: str):
    """Evaluate a mathematical expression using a restricted namespace.

    Supports math functions from the math module and basic operators.
    Raises ValueError on invalid expressions.
    """
    # sanitize expression: allow digits, operators, parentheses, dots, names, and spaces
    import re
    if not expr or not expr.strip():
        raise ValueError("Empty expression")

    if re.search(r"[^0-9a-zA-Z_\.\+\-\*\/%\(\)\,\s]", expr):
        raise ValueError("Invalid characters in expression")

    try:
        # compile and evaluate with controlled globals and locals
        code = compile(expr, "<string>", "eval")
        for name in code.co_names:
            if name not in ALLOWED_NAMES and name not in ('e', 'pi'):
                raise ValueError(f"Use of name '{name}' not allowed")
        result = eval(code, {"__builtins__": {}}, ALLOWED_NAMES)
    except Exception as e:
        raise ValueError("Error evaluating expression: " + str(e))
    return result
