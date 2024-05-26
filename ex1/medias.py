# média simples
n1 = 10
n2 = 4
print("Os números são: ", n1, "e", n2)
ms = (n1 + n2) / 2
print('Media simples:', ms) 
# harmônica
mh = 2 / (1/n1 + 1/n2)
print("media harmônica: ", mh)
# ponderada
p1 = 2
p2 = 4
print("Pesos são:", p1, "e", p2)
mp = (p1 * n1 + p2 * n2) / (p1 + p2)
print("Média ponderada: ", mp)

