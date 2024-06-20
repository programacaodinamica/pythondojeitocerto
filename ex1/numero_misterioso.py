numero = 42

chute = int(input("Advinhe o valor: "))

while chute != numero:
    if chute > numero:
        print("Seu chute é MAIOR que o valor")
    else:
        print("Seu chute é MENOR que o valor")
    chute = int(input("Advinhe o valor: "))

print(f"Parabéns, o número era {numero}!!!")