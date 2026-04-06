# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = (b ** 2 - 4 * a * c)
    r1 = ((-1* b) + discriminante ** 0.5) / (2 * a)
    r2 = ((-1* b) - discriminante ** 0.5) / (2 * a)

    if discriminante == 0:
        return f"({r1})"
    elif discriminante > 0:
        return f"({r1}, {r2})"
    else:
        return "( )"

def value_y(a, b, c, x):
    return (a * x**2) + (b * x) + c


def to_string(a, b, c):
    if a != 0:
        if b != 0:
            if c != 0:
                return f"f(x) = {a} * X^2 + {b} * X + {c}"
            else:
                return f"f(x) = {a} * X^2 + {b} * X"
        elif b == 0 and c != 0:
            return f"f(x) = {a} * X^2 + {c}"
        else:
            return f"f(x) = {a} * X^2"
    elif b != 0 and c != 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0 and c != 0:
        return f"f(x) = {c}"
    elif b != 0 and c == 0:
        return f"f(x) = {b} * X"


def derivation(a, b, c):
    if a != 0:
        if b != 0:
            return f"f'(x) = {2*a} * X + {b}"
        else:
            return f"f'(x) = {2*a} * X"
    elif a == 0 and b != 0:
        return f"f'(x) = {b}"
    else:
        return f"f'(x) = 0"
