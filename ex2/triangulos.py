def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a > (b + c):
        return False
    if b > (a + c):
        return False
    if c > (a + b):
        return False
    return True

def perimetro(a, b, c):
    if triangulo_valido(a, b, c):
        return a + b + c
    return -1

def area(a, b, c):
    p = perimetro(a, b, c) / 2
    if p > 0:
        area = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
        return area
    return -1
