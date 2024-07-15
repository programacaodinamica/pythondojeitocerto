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

a, b, c = 10, 4, 5
if triangulo_valido(a, b, c):
    print("Triângulo Válido")
else:
    print("NÃO é um triângulo válido")