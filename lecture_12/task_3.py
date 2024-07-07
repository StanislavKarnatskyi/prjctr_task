
def check_types(func):
    def wrapper(*args):
        num_a, num_b = args
        if isinstance(num_a, int) and isinstance(num_b, int):
            return func(num_a, num_b)
        else:
            raise TypeError("Argument a must be int, not str")
    return wrapper


@check_types
def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))
print(add(6, '2'))
print(add(54, 100))