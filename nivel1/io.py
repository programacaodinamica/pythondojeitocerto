# palavra = input("Digite uma palavra: ")
# print(palavra)
nota = input("Digite a nota: ")
nota = float(nota)
media = float(input("Digite a média: "))

if nota >= media: 
    print("Aprovado com nota", nota, 
          "(média é", media, ")")
else: 
    print(f'Reprovado com a nota {nota} (média é {media})')