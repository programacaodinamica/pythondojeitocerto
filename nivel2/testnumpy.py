import numpy as np

v1 =  np.array([3, 5, 7])
v2 =  np.array([-1, 3, -4])

a =  [3, 5, 7]
b =  [-1, 3, -4]
print(v1 + v2)
# com listas, concatenação
print(a + b)


if __name__ == '__main__':
    a = np.array((2, 5))
    b = np.array((1.5, 7.0))
    num = 4
    print('Soma dos vetores a e b: ', a + b)
    print('Diferença dos vetores a e b: ', a - b)
    print(f'Multiplicação de {a} por {num}: ', num * a)
    print('Produto escalar entre a e b: ', np.dot(a, b))

    print('Média dos valores em a:', a.mean())

    mat1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat2 = np.eye(3, 3)
    print(mat1)
    print(mat2)
    print(mat1 @ mat2)

    print('Maior valor em mat1:', mat1.max())