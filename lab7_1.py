import numpy as np
import matplotlib.pyplot as plt

# Определение диапазона значений x1
x1 = np.linspace(0, 15, 400)

# Определение ограничений
y1 = (2 * x1 + 10) / 5  # x2 <= (2 * x1 + 10) / 5
y2 = (40 - 4 * x1) / 5  # x2 <= (40 - 4 * x1) / 5
y3 = (5 - x1) / 5       # x2 >= (5 - x1) / 5

# Находим точки пересечения:
intersection1 = (5, 4)
intersection2 = (0, 2)

# Собираем вершины, которые попадают в область допустимых значений
vertices = [intersection1, intersection2]

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

# Вектор градиента
gradient = np.array([1, 2])  # Градиент функции z
origin = np.array([0, 0])  # Начальная точка для вектора

# Рисуем вектор градиента
plt.quiver(*origin, *gradient, scale=3, color='purple', label='Градиент', angles='xy')

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
