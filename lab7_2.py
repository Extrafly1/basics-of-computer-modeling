import numpy as np
import matplotlib.pyplot as plt

def simplex_method(c, A, b):
    num_constraints, num_vars = A.shape
    A = np.hstack([A, np.eye(num_constraints)])  # Добавляем искусственные переменные
    c = np.hstack([c, np.zeros(num_constraints)])  # Целевая функция с нулями для искусственных переменных
    basis = list(range(num_vars, num_vars + num_constraints))  # Начальный базис

    while True:
        B = A[:, basis]
        cb = c[basis]
        pi = np.linalg.inv(B) @ cb  # Двойственные цены
        z = c - pi @ A  # Улучшение целевой функции

        print("Текущие значения z:", z)
        print("Базисные переменные:", basis)
        print("Текущая таблица:")
        print("A:\n", A)
        print("b:", b)
        print("c: ", c)
        print("cb:", cb)
        print("z: ", z)
        if all(z >= 0):  # Проверка на оптимальность
            print("z: ", z)
            break

        entering = np.argmin(z)  # Выбор входящей переменной
        column = A[:, entering]

        ratios = []
        for i in range(num_constraints):
            if column[i] > 0:
                print(b[i], " ", column[i])
                ratios.append(b[i] / column[i])
            else:
                ratios.append(np.inf)

        if all(np.isinf(ratios)):  # Проверка на ограниченность
            raise ValueError("Задача не имеет ограниченного решения.")

        leaving = np.argmin(ratios)  # Выбор выходящей переменной

        # Обновление базиса
        basis[leaving] = entering
        pivot = column[leaving]
        b[leaving] /= pivot
        A[leaving, :] /= pivot
        for i in range(num_constraints):
            if i != leaving:
                print(b[i], " ", A[i, :])
                factor = A[i, entering]
                b[i] -= factor * b[leaving]
                A[i, :] -= factor * A[leaving, :]
                print(b[i], " ", A[i, :])


    x = np.zeros(len(c))
    for i, var in enumerate(basis):
        print(b[i])
        x[var] = b[i]

    return -c @ x, x[:num_vars]

# Заданные параметры
c = np.array([3, -4, 1])  # Целевая функция (максимизация)
A = np.array([
    [1, 2, 1],
    [2, 1, 2],
    [3, 1, 2]
])  # Ограничения
b = np.array([10, 6, 12])  # Правые части

optimal_value, solution = simplex_method(c, A, b)
print(f"Оптимальное значение целевой функции: {optimal_value:.2f}")
print(f"Оптимальное решение: {solution}")
