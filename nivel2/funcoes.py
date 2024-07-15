# Exemplos de funções que já utilizamos
num = int(input("Digite um número: "))
num = num + 3
print(num)

# Exemplos de definição de novas funções
# função com 1 argumento
def multiplicar_por_7(n):
    res = 7 * n
    return res

r =  multiplicar_por_7(10)
print("Resultado é", r)

# função com dois argumentos
def media_simples(a, b):
    return (a + b) / 2

print(media_simples(10, 8))
res = multiplicar_por_7(6)
print(res)
a = 8
b = 32
print(media_simples(b, a))

# Exemplo de função sem argumento
def pedir_inscricao():
    print("Inscreva-se no canal Programação Dinâmica")

pedir_inscricao()
