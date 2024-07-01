texto = "matemática"
# acesso por índice
print(texto[-1])
print(texto[len(texto) - 1])
print("-----------")
# repeticao com for
for c in texto:
    print(c)
print("-----------")

# Comparações entre strings
print("Matemática" == texto)
print(texto.upper())
print("Matemática".upper() == texto.upper())
print(texto.lower())
print("Matemática".lower() == texto.lower())
print("-----------")
# Verificar se está contida
texto = " matemática  "
frase = "A nota de Matemática de Pedro foi 7.8"
if texto.lower().strip() in frase.lower():
    print("Achou", texto)
else:
    print("Não tá aqui")
print("-----------")
# Particionar uma string
partes = frase.split()
print(partes)
