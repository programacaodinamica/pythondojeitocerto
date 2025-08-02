class Fracao:
    def __init__(self, num, den):
        self.numerador = num
        self.denominador = den

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, rhs):
        num1, den1 = self.numerador, self.denominador
        if isinstance(rhs, int):
            num2, den2 = rhs, 1
        else:
            num2, den2 = rhs.numerador, rhs.denominador
        if den1 == den2:
            num_r = num1 + num2
            den_r = den1
        else:
            den_r = den1 * den2
            num_r = (num1 * den2) + (num2 * den1)
        return Fracao(num_r, den_r)
    
    def __radd__(self, lhs):
        if isinstance(lhs, int):
            return self + lhs
        raise TypeError(f"Operação + não suportada entre {type(self)} e {type(lhs)}")
    
    def __neg__(self):
        return Fracao(-self.numerador, self.denominador)
    
    def __sub__(self, rhs):
        return self + (-rhs)
    
    def __rsub__(self, lhs):
        return -self + lhs
    
    def __mul__(self, rhs):
        if isinstance(rhs, int):
            num2, den2 = rhs, 1
        else:
            num2, den2 = rhs.numerador, rhs.denominador
        num = self.numerador * num2
        den = self.denominador * den2
        return Fracao(num, den)
    
    def __rmul__(self, lhs):
        return self * lhs
    
    def __truediv__(self, rhs):
        if isinstance(rhs, int):
            num, den = 1, rhs
        else:
            num, den = rhs.denominador, rhs.numerador
        return self * Fracao(num, den)
    
    def __rtruediv__(self, lhs):
        if isinstance(lhs, int):
            return Fracao(lhs, 1) / self
        raise TypeError(f"Operação / não suportada entre {type(self)} e {type(lhs)}")
    
    def __lt__(self, rhs):
        num1, den1 = self.numerador, self.denominador
        num2, den2 = rhs.numerador, rhs.denominador
        num1_r = num1 * den2
        num2_r = num2 * den1
        return num1_r < num2_r
    
    def __gt__(self, rhs):
        num1, den1 = self.numerador, self.denominador
        num2, den2 = rhs.numerador, rhs.denominador
        num1_r = num1 * den2
        num2_r = num2 * den1
        return num1_r > num2_r
    
    def __eq__(self, rhs):
        num1, den1 = self.numerador, self.denominador
        num2, den2 = rhs.numerador, rhs.denominador
        return num1 * den2 == num2 * den1
    
    def __le__(self, rhs):
        return self < rhs or self == rhs
    
    def __ge__(self, rhs):
        return self > rhs or self == rhs


def ler_fracao():
    numerador = int(input("Digite o numerador da fração: "))
    denominador = int(input("Digite o denominador da fração: "))
    return Fracao(numerador, denominador)

if __name__ == '__main__':
    # fracao = Fracao(1, 3)
    fracao1 = ler_fracao()
    fracao2 = ler_fracao()
    # print(fracao.numerador, fracao.denominador)
    # print("A fração é:", fracao)

    # Operações aritméticas com frações
    print(f"A soma das fracoes {fracao1} e {fracao2} é", fracao1 + fracao2)
    print(f"A diferença das fracoes {fracao1} e {fracao2} é", fracao1 - fracao2)    
    print(f"O produto das fracoes {fracao1} e {fracao2} é", fracao1 * fracao2)
    print(f"{fracao1} dividido por {fracao2} é", fracao1 / fracao2)
    # Comparações entre frações
    print(f"A fração {fracao1} é menor que {fracao2}?", fracao1 < fracao2)
    print(f"A fração {fracao1} é maior que {fracao2}?", fracao1 > fracao2)
    print(f"A fração {fracao1} é igual a {fracao2}?", fracao1 == fracao2)
    print(f"A fração {fracao1} é menor ou igual a {fracao2}?", fracao1 <= fracao2)
    print(f"A fração {fracao1} é maior ou igual a {fracao2}?", fracao1 >= fracao2)

    # Operações entre inteiros e frações
    print(f"A soma de {fracao1} com 7 é", fracao1 + 7)
    print(f"A soma de 7 com {fracao1}", 7 + fracao1)
    print(f"A diferença entre {fracao1} e 7 é", fracao1 - 7)
    print(f"A diferença entre 7 e {fracao1}", 7 - fracao1)
    print(f"A multiplicação de {fracao1} por 7 é", fracao1 * 7)
    print(f"A multiplicação de 7 por {fracao1}", 7 * fracao1)
    print(f"A divisão de {fracao1} por 7 é", fracao1 / 7)
    print(f"A divisão de 7 por {fracao1}", 7 / fracao1)
    
