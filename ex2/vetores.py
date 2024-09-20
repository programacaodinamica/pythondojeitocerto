def somar(v1, v2):
    if len(v1) != len(v2):
        print("Vetores incompatíveis")
        return 0
    res = []
    for i in range(len(v1)):
        res.append(v1[i] + v2[i])
    
    return tuple(res)

def inverter(v):
    res = []
    for i in range(len(v)):
        res.append(-v[i])
    return tuple(res)

def subtrair(v1, v2):
    return somar(v1, inverter(v2))

def multiplicar(vet, num):
    res = []
    for val in vet:
        res.append(num * val)
    return tuple(res)

def prod_escalar(v1, v2):
    if len(v1) != len(v2):
        print("Vetores incompatíveis")
        return None
    soma = 0
    for i in range(len(v1)):
        # soma = soma + v1[i] * v2[i]
        soma += v1[i] * v2[i]
    return soma
        

if __name__ == '__main__':
    a = (2, 5)
    b = (1.5, 7.0)
    num = 4
    print('Soma dos vetores a e b: ', somar(a, b))
    print('Diferença dos vetores a e b: ', subtrair(a, b))
    print(f'Multiplicação de {a} por {num}: ', multiplicar(a, num))
    print('Produto escalar entre a e b: ', prod_escalar(a, b))