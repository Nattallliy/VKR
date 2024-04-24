# Задание 1
# Минимизировать квадратичную форму 0.5*(Ax, x) - (b, x)
# методом скорейшего градиентного спуска

import numpy as np

# Матрица формы
A = np.array([[0.78,  1.08, -1.35],
              [1.08, -1.28,  0.37],
              [-1.35, 0.37, 2.86]])
# Вектор правых частей
b = np.array([0.57,
              1.27,
              0.47])

# Произвольный вектор
x = np.array([1, 1, 1])
# Точность
Eps = 0.001
# Матричное произведение
AA = np.matmul(A, A)
bA = np.matmul(b, A)

def F(x):
    u = np.asarray(x)
    Ax_x = np.dot(np.matmul(AA, u), x)
    b_x = np.dot(bA, x)
    return Ax_x/2 - b_x

def F_p(x):
    u = np.asarray(x)
    Au = np.matmul(AA, u)
    return Au - bA

# Произвольное начальное значение
x1 = 0
x2 = x
c = abs(x2 - x1) >= Eps
while (any(c) or (abs(F(x2) - F(x1)) >= Eps)):
    x1 = x2
    alpha = np.dot(F_p(x), F_p(x))/np.dot(np.matmul(AA, F_p(x)), F_p(x))
    x2 = x1 - alpha*F_p(x1)
    c = abs(x2 - x1) >= Eps

print('Вектор x:')
print(x2[0])
print(x2[1])
print(x2[2])
# print()
# print(0.93*x2[0] + 1.42*x2[1] - 2.55*x2[2])
# print(1.42*x2[0] - 2.87*x2[1] + 2.36*x2[2])
# print(-2.55*x2[0] + 2.36*x2[1] - 1.44*x2[2])
print()
print('Значение функции =', F(x2))