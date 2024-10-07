import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import fsolve

# Задаём функции f1(x) и f2(x) для n = 14
n = 11
def f1(x):
    return (10 * x) / n

def f2(x):
    return 10 * (x - 20) / (n - 20) + 20

def dif(x):
    return f1(x) - f2(x)

def dif1(x):
    return f1(x)

def dif2(x):
    return f2(x)

init = 0
inter_x = fsolve(dif, init)[0]
inter_y = f1(inter_x)

inter_a = fsolve(dif1, init)[0]
inter_b = fsolve(dif2, init)[0]

# Построение графика для f2(x)
x_values = np.linspace(0, 40, 500)  # от 0 до 40 с шагом
y_f1 = f1(x_values)
y_f2 = f2(x_values)

# Построение графика
plt.plot(x_values, y_f1, label='f1(x)')
plt.plot(x_values, y_f2, label='f2(x)')
#plt.fill_between(x_values, y_f1, y_f2, where=(y_f1 < y_f2), color='gray', alpha=0.3)
plt.fill_between(x_values, np.minimum(y_f1, y_f2), color='gray', alpha=0.3)
plt.xlim(0, 40)
plt.ylim(0, inter_y)
plt.legend()
plt.title("Графики f1(x) и f2(x)")
plt.xlabel('x')
plt.ylabel('y')

# Указание 2: Определение размеров треугольника

rectangle_area = inter_y * 1/3 * abs(inter_a - inter_b)

# Указание 3: Генерация случайных точек (x, y)
a = 0
b = 40
N = 100000 # Количество случайных точек
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, 30, N)

# Вывод точек на график
plt.scatter(x_random, y_random, color='red', s=1, alpha=0.5)

# Указание 4: Вычисление количества точек внутри фигуры S
M = 0
for i in range(N):
    if f1(x_random[i]) > y_random[i] < f2(x_random[i]):
        M += 1

# Указание 5: Вычисление приближённой площади фигуры методом Монте-Карло
estimated_area = (M / N) * rectangle_area
print(f"Приближённая площадь фигуры: {estimated_area}")

# Точное вычисление площади через интеграл
true_area, _ = quad(lambda x: f2(x) - f1(x), a, b)
print(f"Точная площадь фигуры: {true_area}")

# Указание 6: Оценка абсолютной и относительной погрешности
absolute_error = abs(estimated_area - true_area)
relative_error = (absolute_error / true_area) * 100

print(f"Абсолютная погрешность: {absolute_error}")
print(f"Относительная погрешность: {relative_error}%")

plt.show()
