# def somar_fracoes(num1, den1, num2, den2):
#     if den1 == den2:
#         num_r = num1 + num2
#         den_r = den1
#     else:
#         den_r = den1 * den2
#         num_r = (num1 * den2) + (num2 * den1)
#     return (num_r, den_r)
MENOR = -1
IGUAL = 0
MAIOR = 1

def ler_fracao():
    numerador = int(input("Digite o numerador da fração: "))
    denominador = int(input("Digite o denominador da fração: "))
    return (numerador, denominador)

def exibir_fracao(fracao):
    numerador = fracao[0]
    denominador = fracao[1]
    print(f"A fração é: {numerador}/{denominador}")

def somar_fracoes(fracao1, fracao2):
    num1, den1 = fracao1
    num2, den2 = fracao2
    if den1 == den2:
        num_r = num1 + num2
        den_r = den1
    else:
        den_r = den1 * den2
        num_r = (num1 * den2) + (num2 * den1)
    return (num_r, den_r)

# Solução não ideal
# def comparar(fracao1, fracao2):
#     num1, den1 = fracao1
#     num2, den2 = fracao2
#     # denominador comum
#     # den_r = den1 * den2
#     num1_r = num1 * den2
#     num2_r = num2 * den1
#     if num1_r < num2_r:
#         return MENOR
#     elif num1_r == num2_r:
#         return IGUAL
#     else:
#         return MAIOR

def menor_que(fracao1, fracao2):
    num1, den1 = fracao1
    num2, den2 = fracao2
    num1_r = num1 * den2
    num2_r = num2 * den1
    return num1_r < num2_r

def igual_a(fracao1, fracao2):
    num1, den1 = fracao1
    num2, den2 = fracao2
    return num1 * den2 == num2 * den1

def maior_que(fracao1, fracao2):
    num1, den1 = fracao1
    num2, den2 = fracao2
    num1_r = num1 * den2
    num2_r = num2 * den1
    return num1_r > num2_r

def menor_ou_igual(fracao1, fracao2):
    menor = menor_que(fracao1, fracao2)
    igual = igual_a(fracao1, fracao2)
    return menor or igual

def maior_ou_igual(fracao1, fracao2):
    maior = maior_que(fracao1, fracao2)
    igual = igual_a(fracao1, fracao2)
    return maior or igual


if __name__ == '__main__':
    fracao1 = ler_fracao()
    fracao2 = ler_fracao()
    resultado = somar_fracoes(fracao1, fracao2)
    exibir_fracao(resultado)

    if maior_que(fracao1, fracao2):
        print(f"A fracao {fracao1} é maior que a {fracao2}")
    elif igual_a(fracao1, fracao2):
        print(f"A fracao {fracao1} é igual a {fracao2}")
    else: 
        print(f"A fracao {fracao1} é menor que a {fracao2}")
    # res_comp = comparar(fracao1, fracao2)
    # if res_comp == MAIOR:
    #     print(f"A fracao {fracao1} é maior que a {fracao2}")
    # elif res_comp == IGUAL:
    #     print(f"A fracao {fracao1} é igual que a {fracao2}")
    # else:
    #     print(f"A fracao {fracao1} é menor que a {fracao2}")
