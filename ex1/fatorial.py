# 4! = 4 * 3 * 2 * 1

n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n + 1):
    fatorial = fatorial * i
print(f"Fatorial de {n} é {fatorial} [for]")

fatorial = 1
p = n
while p > 0:
    fatorial = p * fatorial
    p -= 1
print(f"Fatorial de {n} é {fatorial} [while]")
