disciplinas = ("matemática", "português", 
               "filosofia", "história",
               "física", "geografia",
               "química", "bilogia")
notas = [7.8, 8.2, 9.5, 5.7,
         9.8, 10, 6.4, 7.0]

conteudo = ""
for i in range(len(notas)):
    conteudo = (conteudo + 
                f"A nota da {disciplinas[i]} foi {notas[i]}\n")

with open("boletim.txt", 'a') as arq:
    arq.write(conteudo)
