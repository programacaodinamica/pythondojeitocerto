import os

# endereço absoluto vs relativo
absoluto ="/Users/hallpaz/Workspace/pgdinamica/pjc2/nivel2/caminhos.py"
relativo = "nivel2/caminhos.py"
# obtendo endereço absoluto
DATA_DIR = "data"
print(os.path.abspath(DATA_DIR))
# adicionando o nome de um arquivo a um endereço
caminho = os.path.join(os.path.abspath(DATA_DIR), "lados.txt")
print(caminho)

# obtendo o conteúdo de uma pasta
print(os.listdir("nivel2"))

modulos_python = []
for nome in os.listdir("nivel2"):
    if nome.endswith(".py"):
        modulos_python.append(nome)
print(modulos_python)

# construindo um caminho mais complexo
print(os.path.join(
    os.path.abspath('.'), 'data', 'lados.txt'
))

# criando um novo diretório
OUTPUT_DIR = "saidas"
nomearquivo = "mensagem.txt"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

with open(os.path.join(OUTPUT_DIR, nomearquivo), 'w') as arq:
    arq.write("Inscreva-se no canal Programação Dinâmica")