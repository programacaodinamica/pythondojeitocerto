disciplinas = ("matemática", "português", 
               "filosofia", "história",
               "física", "geografia",
               "química", "bilogia")
notas = [7.8, 8.2, 9.5, 5.7,
         9.8, 10, 6.4, 7.0]

for i in range(len(notas)):
    print(f"A nota da {disciplinas[i]} foi {notas[i]}")
