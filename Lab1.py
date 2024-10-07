import numpy as np
import matplotlib.pyplot as plt

# Данные задачи
x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([2.4, 2.9, 3.0, 3.5, 3.6, 3.7])

# Настройка графика
plt.plot(x[0], y[0], 'k', label="Дано", marker="o")
plt.plot(x[1], y[1], 'k', marker="o")
plt.plot(x[2], y[2], 'k', marker="o")
plt.plot(x[3], y[3], 'k', marker="o")
plt.plot(x[4], y[4], 'k', marker="o")
plt.plot(x[5], y[5], 'k', marker="o")
X = np.linspace(min(x), max(x), 1000)

def linear_approximation(x, y):
    print("---------------------Линейный метод--------------------")
    n = len(x)
    sum_xy = np.sum(x * y)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x ** 2)
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    
    print(f"a = {round(a, 2)}")
    print(f"b = {round(b, 2)}")
    
    for xi, yi in zip(x, y):
        pred_y = a * xi + b
        print(f"x = {xi}; y = {round(pred_y, 2)} | {yi}")
    
    mse = np.sum((a * x + b - y) ** 2)
    print(f"Суммарная погрешность - {mse}")
    
    plt.plot(X, a * X + b, label="Линейный метод")

def power_approximation(x, y):
    print("-------------------Степенная функция----------------------")
    x_log = np.log(x)
    y_log = np.log(y)
    
    n = len(x)
    sum_ln_xln_y = np.sum(x_log * y_log)
    sum_ln_x = np.sum(x_log)
    sum_ln_y = np.sum(y_log)
    sum_ln_x2 = np.sum(x_log ** 2)
    
    a = (n * sum_ln_xln_y - sum_ln_x * sum_ln_y) / (n * sum_ln_x2 - sum_ln_x ** 2)
    beta = np.exp((sum_ln_y - a * sum_ln_x) / n)
    
    print(f"a = {round(a, 2)}")
    print(f"beta = {round(beta, 2)}")
    
    for xi, yi in zip(x, y):
        pred_y = beta * (xi ** a)
        print(f"x = {xi}; y = {round(pred_y, 2)} | {yi}")
    
    mse = np.sum((beta * x ** a - y) ** 2)
    print(f"Суммарная погрешность - {mse}")
    
    plt.plot(X, beta * (X ** a), label="Степенная функция")

def exponential_approximation(x, y):
    print("-------------------Показательная функция-------------------")
    x_log = np.array(x)
    y_log = np.log(y)
    
    n = len(x)
    sum_xln_y = np.sum(x_log * y_log)
    sum_x = np.sum(x_log)
    sum_ln_y = np.sum(y_log)
    sum_x2 = np.sum(x_log ** 2)
    
    a = (n * sum_xln_y - sum_x * sum_ln_y) / (n * sum_x2 - sum_x ** 2)
    beta = np.exp((sum_ln_y - a * sum_x) / n)
    
    print(f"a = {round(a, 2)}")
    print(f"beta = {round(beta, 2)}")
    
    for xi, yi in zip(x, y):
        pred_y = beta * np.exp(a * xi)
        print(f"x = {xi}; y = {round(pred_y, 2)} | {yi}")
    
    mse = np.sum((beta * np.exp(a * x) - y) ** 2)
    print(f"Суммарная погрешность - {mse}")
    
    plt.plot(X, beta * np.exp(a * X), label="Показательная функция")

def quadratic_approximation(x, y):
    print("---------------------Квадратичная функция-----------------")
    A = np.vstack([x ** 2, x, np.ones(len(x))]).T
    coeffs = np.linalg.lstsq(A, y, rcond=None)[0]
    a, b, c = coeffs
    
    print(f"a = {round(a, 2)}")
    print(f"b = {round(b, 2)}")
    print(f"c = {round(c, 2)}")
    
    for xi, yi in zip(x, y):
        pred_y = a * xi ** 2 + b * xi + c
        print(f"x = {xi}; y = {round(pred_y, 2)} | {yi}")
    
    mse = np.sum((a * x ** 2 + b * x + c - y) ** 2)
    print(f"Суммарная погрешность - {mse}")
    
    plt.plot(X, a * X ** 2 + b * X + c, label="Квадратичная функция")

def main():
    print("1) Линейный метод")
    print("2) Степенная функция")
    print("3) Показательная функция")
    print("4) Квадратичная функция")
    print("5) Все методы")
    choice = int(input("Введите метод: "))

    if choice == 1:
        linear_approximation(x, y)
    elif choice == 2:
        power_approximation(x, y)
    elif choice == 3:
        exponential_approximation(x, y)
    elif choice == 4:
        quadratic_approximation(x, y)
    elif choice == 5:
        linear_approximation(x, y)
        power_approximation(x, y)
        exponential_approximation(x, y)
        quadratic_approximation(x, y)
    else:
        print("Неверный выбор")

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
