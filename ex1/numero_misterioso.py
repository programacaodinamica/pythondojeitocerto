import random

numero = random.randint(0, 1000)

chute = int(input("Advinhe o valor (entre 0 e 1000): "))

while chute != numero:
    if chute > numero:
        print("Seu chute é MAIOR que o valor")
    else:
        print("Seu chute é MENOR que o valor")
    chute = int(input("Advinhe o valor: "))

print(f"Parabéns, o número era {numero}!!!")