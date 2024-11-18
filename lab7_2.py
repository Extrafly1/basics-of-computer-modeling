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
        Оптимальное значение целевой функции и вектор решения.
    """
    # Добавляем искусственные переменные
    num_constraints, num_vars = A.shape
    A = np.hstack([A, np.eye(num_constraints)])
    c = np.hstack([c, np.zeros(num_constraints)])
    basis = list(range(num_vars, num_vars + num_constraints))

    # Итеративный процесс
    while True:
        # Определение коэффициентов при свободных переменных
        cb = c[basis]
        z = cb @ A[:, basis] @ np.linalg.inv(A[:, basis]) @ A - c
        z_j = z[:-1]

        # Проверка оптимальности
        if all(z_j <= 0):
            break

        # Выбор входящей переменной (максимальный положительный z_j)
        entering = np.argmax(z_j)
        column = A[:, entering]


