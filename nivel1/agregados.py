# nota_matematica = 7.8
# nota_portugues = 8.2
# nota_filosofia = 9.5
notas = [7.8, 8.2, 9.5]
disciplinas = ["matemática", "português", "filosofia"]
disciplinas.append("história")
notas[0] = notas[0] + 1
notas.append(9)
# print(notas, type(notas), type(notas[0]))
print(f"A nota de {disciplinas[0]} foi {notas[0]}.")
print(f"A nota de {disciplinas[-2]} foi {notas[-2]}.")
print(disciplinas[3])
print(notas[3])

nomes = ("Maria", "João", "Paula")
print(nomes[0], nomes[-1])
# listas são imutáveis
nomes[1] = "Marcelo"