# решить графически задачу линейного программирования а python:
# z(x) = x1 + 2 * x2  -> max, min.
# {2 * x1 - 5 * x2 >= -10
# {4 * x1 + 5 * x2 <= 40
# {x1 + 5 * x2 >= 5
# {x1 >= 0
# {x2 >= 0

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 15, 400)

y1 = (2 * x1 + 10) / 5  # x2 <= (2 * x1 + 10) / 5
y2 = (40 - 4 * x1) / 5  # x2 <= (40 - 4 * x1) / 5
y3 = (5 - x1) / 5       # x2 >= (5 - x1) / 5

# Находим точки пересечения:
# Пересечение y1 и y2:
# 2 * x1 + 10 = 5 * x2
# 4 * x1 + 5 * x2 = 40
# Решим систему:
# x1 = 5, x2 = 4
intersection1 = (5, 4)

# Пересечение y1 и y3:
# 2 * x1 + 10 = 5 * x2
# x1 + 5 * x2 = 5
# Решим систему:
# x1 = 0, x2 = 2
intersection2 = (0, 2)

# Пересечение y2 и y3:
# 4 * x1 + 5 * x2 = 40
# x1 + 5 * x2 = 5
# Решим систему:
# x1 = 8, x2 = -1 (не входит в область, игнорируем)

# Граничная точка при x1 = 0, x2 >= 0:
# x1 = 0, x2 = 5/5 = 1
boundary_point = (0, 1)

# Собираем вершины, которые попадают в область допустимых значений
vertices = [intersection1, intersection2, boundary_point]

# Вычисляем значения целевой функции z(x) = x1 + 2*x2 для каждой вершины
objective_values = [x[0] + 2 * x[1] for x in vertices]
max_idx = np.argmax(objective_values)
min_idx = np.argmin(objective_values)

# Построим график
plt.figure(figsize=(8, 8))
plt.plot(x1, y1, label='2*x1 - 5*x2 >= -10')
plt.plot(x1, y2, label='4*x1 + 5*x2 <= 40')
plt.plot(x1, y3, label='x1 + 5*x2 >= 5')

# Ограничения x1, x2 >= 0
plt.xlim(0, 15)
plt.ylim(0, 15)

# Заштрихуем недопустимые области
plt.fill_between(x1, y1, 15, color='gray', alpha=0.3)  # для первого ограничения
plt.fill_between(x1, y2, 0, color='gray', alpha=0.3)  # для второго ограничения
plt.fill_between(x1, 0, y3, color='gray', alpha=0.3)  # для третьего ограничения

# Визуализация вершин
vertices_x = [v[0] for v in vertices]
vertices_y = [v[1] for v in vertices]
plt.scatter(vertices_x, vertices_y, color='blue', zorder=5, label='Вершины области')

# Подпись точек экстремумов
plt.scatter(vertices[max_idx][0], vertices[max_idx][1], color='green', zorder=5, label='Максимум')
plt.scatter(vertices[min_idx][0], vertices[min_idx][1], color='red', zorder=5, label='Минимум')

# Добавим подписи
plt.xlabel('x1')
plt.ylabel('x2')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.title('Графическое решение задачи линейного программирования')

plt.show()

# Выводим значения экстремумов
print(f"Максимум z = {objective_values[max_idx]:.2f} в точке {vertices[max_idx]}")
print(f"Минимум z = {objective_values[min_idx]:.2f} в точке {vertices[min_idx]}")
