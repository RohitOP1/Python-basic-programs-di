import math

def find_roots(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        return "No real roots"
    sqrt_delta = math.sqrt(delta)
    return (-b + sqrt_delta) / (2 * a), (-b - sqrt_delta) / (2 * a)

a, b, c = map(float, input("Enter coefficients a, b, c: ").split())
print(find_roots(a, b, c))
