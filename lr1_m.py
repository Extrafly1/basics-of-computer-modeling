import matplotlib
matplotlib.use('Qt5Agg')
# всё что выше тупо для arch linux

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Данные
x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([2.4, 2.9, 3.0, 3.5, 3.6, 3.7])

# Линейная аппроксимация (y = a * x + b)
def linear_func(x, a, b):
    return a * x + b

# Степенная аппроксимация (y = a * x^b)
def power_func(x, a, b):
    return a * x**b

# Показательная аппроксимация (y = a * exp(b * x))
def exp_func(x, a, b):
    return a * np.exp(b * x)

# Квадратичная аппроксимация (y = a * x^2 + b * x + c)
def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

# Найдем параметры для каждой модели
popt_linear, _ = curve_fit(linear_func, x, y)
popt_power, _ = curve_fit(power_func, x, y)
popt_exp, _ = curve_fit(exp_func, x, y)
popt_quad, _ = curve_fit(quadratic_func, x, y)

# Округление параметров до 0,01
popt_linear = np.round(popt_linear, 2)
popt_power = np.round(popt_power, 2)
popt_exp = np.round(popt_exp, 2)
popt_quad = np.round(popt_quad, 2)

# Вывод параметров для проверки
print(f"Линейная функция: y = {popt_linear[0]} * x + {popt_linear[1]}")
print(f"Степенная функция: y = {popt_power[0]} * x^{popt_power[1]}")
print(f"Показательная функция: y = {popt_exp[0]} * exp({popt_exp[1]} * x)")
print(f"Квадратичная функция: y = {popt_quad[0]} * x^2 + {popt_quad[1]} * x + {popt_quad[2]}")

# Построим графики
x_fit = np.linspace(2, 12, 100)

plt.scatter(x, y, label='Экспериментальные данные', color='red')

# Линейная аппроксимация
plt.plot(x_fit, linear_func(x_fit, *popt_linear), label=f'Линейная y = {popt_linear[0]}x + {popt_linear[1]}')

# Степенная аппроксимация
plt.plot(x_fit, power_func(x_fit, *popt_power), label=f'Степенная y = {popt_power[0]}x^{popt_power[1]}')

# Показательная аппроксимация
plt.plot(x_fit, exp_func(x_fit, *popt_exp), label=f'Показательная y = {popt_exp[0]}exp({popt_exp[1]}x)')

# Квадратичная аппроксимация
plt.plot(x_fit, quadratic_func(x_fit, *popt_quad), label=f'Квадратичная y = {popt_quad[0]}x^2 + {popt_quad[1]}x + {popt_quad[2]}')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.title('Аппроксимация методом наименьших квадратов')
plt.show()
