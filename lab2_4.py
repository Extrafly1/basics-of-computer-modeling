import numpy as np
import matplotlib.pyplot as plt

# Параметры
A = 11
B = 4
p = 11
N = 10000  # Количество случайных точек

# Определение максимальных значений для прямоугольника
phi_vals = np.linspace(0, 2 * np.pi, 100)
rho_max = np.sqrt(p**2 / (A * np.cos(phi_vals)**2 + B * np.sin(phi_vals)**2))
x_max = np.max(rho_max * np.cos(phi_vals))
y_max = np.max(rho_max * np.sin(phi_vals))
a, b = x_max, y_max

# Генерация случайных точек в прямоугольнике
x_points = np.random.uniform(-a, a, N)
y_points = np.random.uniform(-b, b, N)

# Функция для перевода декартовых координат в полярные
def to_polar(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return rho, phi

# Проверка попадания точки в фигуру
def is_inside_figure(x, y, A, B, p):
    rho, phi = to_polar(x, y)
    return rho < np.sqrt(p**2 / (A * np.cos(phi)**2 + B * np.sin(phi)**2))

# Подсчёт точек внутри фигуры
M = sum(is_inside_figure(x, y, A, B, p) for x, y in zip(x_points, y_points))

# Приближённое значение площади фигуры
area_approx = (4 * M) / N * a * b

# Построение графика
phi = np.linspace(0, 2 * np.pi, 100)
rho = np.sqrt(p**2 / (A * np.cos(phi)**2 + B * np.sin(phi)**2))
x_circle = rho * np.cos(phi)
y_circle = rho * np.sin(phi)

plt.figure(figsize=(8, 8))

# Построение прямоугольника
plt.plot([-a, a, a, -a, -a], [-b, -b, b, b, -b], 'k--', label='Прямоугольник')

# Построение фигуры
plt.plot(x_circle, y_circle, 'b-', label='Фигура')

# Отображение случайных точек
colors = ['r' if is_inside_figure(x, y, A, B, p) else 'b' for x, y in zip(x_points, y_points)]
plt.scatter(x_points, y_points, c=colors, s=1, label='Случайные точки')

plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Приближённая площадь фигуры: {area_approx:.4f}')
plt.legend()
plt.grid(True)
plt.show()

# Вывод результатов
print(f"Приближённая площадь фигуры: {area_approx:.4f}")
