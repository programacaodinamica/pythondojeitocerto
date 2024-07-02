texto = "   102.78a    "
aux = texto.strip()
partes = aux.split('.')
eh_numero = True
if len(partes) <= 2:
    for parte in partes:
        if not parte.isdigit():
            eh_numero = False
else:
    eh_numero = False

if eh_numero:
    print("É número")
else:
    print("NÃO é número")