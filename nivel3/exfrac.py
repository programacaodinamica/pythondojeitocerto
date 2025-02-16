def ler_fracao():
    numerador = int(input("Digite o numerador da fração: "))
    denominador = int(input("Digite o denominador da fração: "))
    return (numerador, denominador)

def exibir_fracao(fracao):
    numerador = fracao[0]
    denominador = fracao[1]
    print(f"A fração é: {numerador}/{denominador}")

# def somar_fracoes(num1, den1, num2, den2):
#     if den1 == den2:
#         num_r = num1 + num2
#         den_r = den1
#     else:
#         den_r = den1 * den2
#         num_r = (num1 * den2) + (num2 * den1)
#     return (num_r, den_r)

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

if __name__ == '__main__':
    fracao1 = ler_fracao()
    fracao2 = ler_fracao()
    resultado = somar_fracoes(fracao1, fracao2)
    exibir_fracao(resultado)

