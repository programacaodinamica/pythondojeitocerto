class Fracao:
    def __init__(self, num, den):
        self.numerador = num
        self.denominador = den

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

def ler_fracao():
    numerador = int(input("Digite o numerador da fração: "))
    denominador = int(input("Digite o denominador da fração: "))
    return Fracao(numerador, denominador)

if __name__ == '__main__':
    # fracao = Fracao(1, 3)
    fracao = ler_fracao()
    # print(fracao.numerador, fracao.denominador)
    print("A fração é:", fracao)