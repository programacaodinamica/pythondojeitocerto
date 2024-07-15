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

a = float(input("Digite um valor de lado: "))
b = float(input("Digite um valor de lado: "))
c = float(input("Digite um valor de lado: "))

if triangulo_valido(a, b, c):
    print(f"{a}, {b} e {c} formam um triângulo VÁLIDO!")
else:
    print(f"{a}, {b} e {c} NÃO formam um triângulo VÁLIDO!")