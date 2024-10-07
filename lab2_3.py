import numpy as np
import matplotlib.pyplot as plt

# Параметры
R = 11  # Радиус круга
N = 10000  # Количество случайных точек

# Генерация случайных точек в квадрате со стороной 2R
x_points = np.random.uniform(-R, R, N)
y_points = np.random.uniform(-R, R, N)

# Определение функции для проверки попадания точки в круг
def is_inside_circle(x, y, R):
    return x**2 + y**2 <= R**2

# Подсчёт точек внутри круга
M = sum(is_inside_circle(x, y, R) for x, y in zip(x_points, y_points))

# Приближённое значение числа π
pi_approx = (4 * M) / N

# Истинное значение числа π
pi_true = np.pi

# Абсолютная и относительная погрешности
absolute_error = abs(pi_true - pi_approx)
relative_error = (absolute_error / pi_true) * 100

# Построение графика
theta = np.linspace(0, 2 * np.pi, 100)
circle_x = R * np.cos(theta)
circle_y = R * np.sin(theta)

plt.figure(figsize=(8, 8))

# Построение квадрата
plt.plot([-R, R, R, -R, -R], [-R, -R, R, R, -R], 'k--', label='Квадрат')

# Построение круга
plt.plot(circle_x, circle_y, 'b-', label='Круг')

# Отображение случайных точек
colors = ['r' if is_inside_circle(x, y, R) else 'b' for x, y in zip(x_points, y_points)]
plt.scatter(x_points, y_points, c=colors, s=1, label='Случайные точки')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Приближённое значение π: {pi_approx:.4f}')
plt.legend()
plt.grid(True)
plt.show()

# Вывод результатов
print(f"Приближённое значение числа π: {pi_approx:.4f}")
print(f"Истинное значение числа π: {pi_true:.4f}")
print(f"Абсолютная погрешность: {absolute_error:.6f}")
print(f"Относительная погрешность: {relative_error:.6f}%")
