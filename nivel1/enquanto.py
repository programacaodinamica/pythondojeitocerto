nota = float(input("Digite um valor de nota: "))
# if nota >= 0 and nota <= 10:
#     print(nota)
# else:
#     print("nota inválida")
while nota < 0 or nota > 10:
    nota = float(input("Digite um valor VÁLIDO de nota: "))
    print("vou repetir")
print(nota)