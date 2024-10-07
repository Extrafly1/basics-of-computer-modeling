import numpy as np

# Параметры мультипликативного конгруэнтного метода
X0 = 1          # Начальное значение (seed)
a = 1664525     # Множитель (взято из стандартных параметров для МКМ)
m = 2**32       # Модуль (обычно берётся степень 2)
N = 1000        # Длина последовательности

def multiplicative_congruential_method(X0, a, m, N):
    sequence = np.zeros(N)
    X = X0
    for i in range(N):
        X = (a * X) % m
        sequence[i] = X / m
    return sequence

# Генерация последовательности
sequence = multiplicative_congruential_method(X0, a, m, N)

# Вывод первых 10 значений для примера
print(sequence[:10])
