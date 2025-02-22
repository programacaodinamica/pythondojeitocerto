voto_valido = 20
# obrigatorio = 18 >= voto_valido <= 69 # Verifica se está dentro do intervalo
obrigatorio = 18 <= voto_valido <= 69
# obrigatorio = (18 <= voto_valido) and (voto_valido <= 69)
print(obrigatorio)

if obrigatorio:
    print ("aprovado")
else: 
    print ("reprovado")