# arquivo = open("mensagem.txt", "r")
# msg = arquivo.read()
# arquivo.close()
# print(msg)

caminho = "/Users/hallpaz/Workspace/pgdinamica/pjc2/mensagem.txt"
# with open(caminho,'r') as arq:
#     m = arq.read()
# print("---------")
# print(m)

# msg = "A nota de Matemática foi 9.0"
# with open("mensagem.txt", "w") as arquivo:
#     arquivo.write(msg)

# # adicionando de forma "fake"
# with open(caminho) as arq:
#     conteudo = arq.read()

# conteudo = conteudo + "\nA nota de História foi 9.7\n"

# with open(caminho, 'w') as arq:
#     arq.write(conteudo)

with open(caminho, 'a') as arq:
    arq.write("A nota de português foi 10")