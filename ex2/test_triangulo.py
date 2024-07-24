from triangulos import perimetro, area

a = float(input("Digite um valor de lado: "))
b = float(input("Digite um valor de lado: "))
c = float(input("Digite um valor de lado: "))

print(f"Perímetro do triângulo: {perimetro(a, b, c)}")
print(f"Área do triângulo: {area(a, b, c)}")