# решить симплексным методом следующую задачу линейного программирования
# z(x) = -3 * x1 + 4 * x2 - x3  -> max
# {x1 + 2 * x2 + x3 <= 10
# {2 * x1 + x2 + 2 * x3 <= 6
# {3 * x1 + x2 + 2 * x3 <= 12
# xj >= 0, j = 1, 2, 3.

# import numpy as np
# from scipy.optimize import linprog

# # Определение коэффициентов функции цели (максимизация)
# # Изменяем знак на противоположный, так как linprog решает задачу минимизации
# c = [-3, 4, -1]

# # Определение ограничений
# # Неравенства в виде Ax <= b
# A = [
#     [1, 2, 1],    # x1 + 2*x2 + x3 <= 10
#     [2, 1, 2],    # 2*x1 + x2 + 2*x3 <= 6
#     [3, 1, 2]     # 3*x1 + x2 + 2*x3 <= 12
# ]

# b = [10, 6, 12]

# # Ограничения на неотрицательность переменных
# x_bounds = (0, None)  # xj >= 0, j = 1, 2, 3

# # Решение задачи линейного программирования
# result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds]*3, method='highs')

# # Проверка результатов
# if result.success:
#     print("Оптимальное значение функции цели:", -result.fun)  # Изменяем знак обратно
#     print("Оптимальные значения переменных:")
#     print("x1 =", result.x[0])
#     print("x2 =", result.x[1])
#     print("x3 =", result.x[2])
# else:
#     print("Задача не имеет решения.")

import numpy as np

def simplex_method(c, A, b):
    """
    Реализация симплексного метода для решения задачи линейного программирования.
    max z = c @ x при ограничениях Ax <= b и x >= 0.

    Args:
        c (array): Коэффициенты целевой функции.
        A (array): Матрица коэффициентов ограничений.
        b (array): Вектор правых частей ограничений.

    Returns:
        tuple: Оптимальное значение целевой функции и вектор решения.
    """
    # Размеры задачи
    num_constraints, num_vars = A.shape
    
    # Расширяем A, c для учета базисных переменных
    A = np.hstack([A, np.eye(num_constraints)])
    c = np.hstack([c, np.zeros(num_constraints)])
    basis = list(range(num_vars, num_vars + num_constraints))

    while True:
        # Определение коэффициентов при свободных переменных
        B = A[:, basis]
        cb = c[basis]
        
        # Текущие оценки
        pi = np.linalg.inv(B) @ cb
        z = c - pi @ A
        
        # Проверка оптимальности
        if all(z >= 0):  # Если все коэффициенты неотрицательные, решение оптимально
            break

        # Выбор входящей переменной (максимально отрицательный коэффициент)
        entering = np.argmin(z)
        column = A[:, entering]

        # Проверяем на неограниченность
        ratios = []
        for i in range(num_constraints):
            if column[i] > 0:
                ratios.append(b[i] / column[i])
            else:
                ratios.append(np.inf)

        if all(np.isinf(ratios)):
            raise ValueError("Задача не имеет ограниченного решения.")

        # Выбор выходной переменной
        leaving = np.argmin(ratios)
        
        # Обновляем базис
        basis[leaving] = entering

        # Обновляем правую часть b
        pivot = column[leaving]
        b[leaving] /= pivot
        A[leaving, :] /= pivot
        for i in range(num_constraints):
            if i != leaving:
                factor = A[i, entering]
                b[i] -= factor * b[leaving]
                A[i, :] -= factor * A[leaving, :]

    # Оптимальное значение
    x = np.zeros(len(c))
    for i, var in enumerate(basis):
        x[var] = b[i]
    
    return c @ x, x[:num_vars]


# Коэффициенты задачи
c = np.array([-3, 4, -1])  # Целевая функция
A = np.array([
    [1, 2, 1],
    [2, 1, 2],
    [3, 1, 2]
])  # Ограничения
b = np.array([10, 6, 12])  # Правые части

# Решение
optimal_value, solution = simplex_method(c, A, b)
print(f"Оптимальное значение целевой функции: {optimal_value}")
print(f"Оптимальное решение: {solution}")
