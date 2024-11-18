# решить симплексным методом следующую задачу линейного программирования
# z(x) = -3 * x1 + 4 * x2 - x3  -> max
# {x1 + 2 * x2 + x3 <= 10
# {2 * x1 + x2 + 2 * x3 <= 6
# {3 * x1 + x2 + 2 * x3 <= 12
# xj >= 0, j = 1, 2, 3.

import numpy as np
import matplotlib.pyplot as plt

def simplex_method(c, A, b):
    num_constraints, num_vars = A.shape
    A = np.hstack([A, np.eye(num_constraints)])
    c = np.hstack([c, np.zeros(num_constraints)])
    basis = list(range(num_vars, num_vars + num_constraints))

    while True:
        B = A[:, basis]
        cb = c[basis]
        pi = np.linalg.inv(B) @ cb
        z = c - pi @ A
        
        if all(z >= 0):
            break

        entering = np.argmin(z)
        column = A[:, entering]

        ratios = []
        for i in range(num_constraints):
            if column[i] > 0:
                ratios.append(b[i] / column[i])
            else:
                ratios.append(np.inf)

        if all(np.isinf(ratios)):
            raise ValueError("Задача не имеет ограниченного решения.")

        leaving = np.argmin(ratios)
        
        basis[leaving] = entering
        pivot = column[leaving]
        b[leaving] /= pivot
        A[leaving, :] /= pivot
        for i in range(num_constraints):
            if i != leaving:
                factor = A[i, entering]
                b[i] -= factor * b[leaving]
                A[i, :] -= factor * A[leaving, :]

    x = np.zeros(len(c))
    for i, var in enumerate(basis):
        x[var] = b[i]
    
    return c @ x, x[:num_vars]

# Заданные параметры
c = np.array([-3, 4, -1])  # Целевая функция
A = np.array([
    [1, 2, 1],
    [2, 1, 2],
    [3, 1, 2]
])  # Ограничения
b = np.array([10, 6, 12])  # Правые части

optimal_value, solution = simplex_method(c, A, b)
print(f"Оптимальное значение целевой функции: {optimal_value}")
print(f"Оптимальное решение: {solution}")

# Визуализация
x1_range = np.linspace(0, 6, 100)
x2_range = np.linspace(0, 6, 100)

# Построим ограничения на плоскости x1, x2
fig, ax = plt.subplots(figsize=(8, 6))

# График ограничений
ax.plot(x1_range, (10 - x1_range) / 2, label=r'$x_1 + 2x_2 \leq 10$', color='b')
ax.plot(x1_range, (6 - 2 * x1_range) / 2, label=r'$2x_1 + x_2 \leq 6$', color='g')
ax.plot(x1_range, (12 - 3 * x1_range) / 2, label=r'$3x_1 + x_2 \leq 12$', color='r')

# Оформление
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_xlabel(r'$x_1$')
ax.set_ylabel(r'$x_2$')
ax.set_title('График ограничений и области допустимых решений')

# Отображаем область допустимых решений
ax.fill_between(x1_range, 0, (10 - x1_range) / 2, where=(10 - x1_range) / 2 >= 0, color='gray', alpha=0.3)
ax.fill_between(x1_range, 0, (6 - 2 * x1_range) / 2, where=(6 - 2 * x1_range) / 2 >= 0, color='gray', alpha=0.3)
ax.fill_between(x1_range, 0, (12 - 3 * x1_range) / 2, where=(12 - 3 * x1_range) / 2 >= 0, color='gray', alpha=0.3)

# Точка оптимума
ax.plot(solution[0], solution[1], 'ro', label=f"Оптимум: ({solution[0]:.2f}, {solution[1]:.2f})")

# Легенда
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()

