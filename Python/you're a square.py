import math

def is_square(n):
    return n >= 0 and int(math.sqrt(n))**2 == n

n = -25
print(n, "is a square number" if is_square(n) else "is not a square number")