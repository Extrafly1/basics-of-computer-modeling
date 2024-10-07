import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

seed = 1

def next_random():
    global seed
    a = 1103515245
    c = 12345
    m = 2**31
    seed = (a * seed + c) % m
    return seed

def uniform_distribution(a, b, N):
    random_numbers = []
    for _ in range(N):
        random_num = a + (b - a) * (next_random() / (2**31 - 1))
        random_numbers.append(random_num)
    return random_numbers

def exponential_distribution(lmbda, N):
    if lmbda <= 0:
        raise ValueError("Lambda must be greater than 0")
    random_numbers = []
    for _ in range(N):
        u = next_random() / (2**31 - 1)
        exp_sample = - (1 / lmbda) * math.log(1 - u)
        random_numbers.append(exp_sample)
    return random_numbers

def normal_distribution(mu, sigma, N):
    random_numbers = []
    for _ in range(N):
        uniform_samples = [next_random() / (2**31 - 1) for _ in range(12)]
        normal_sample = sum(uniform_samples) - 6
        normal_value = mu + sigma * (normal_sample / math.sqrt(12))
        random_numbers.append(normal_value)
    return random_numbers

# Функция для генерации выборок всех распределений
def generate_samples(N, a, b, lmbda, mu, sigma):
    uniform_sample = uniform_distribution(a, b, N)
    exp_sample = exponential_distribution(1/lmbda, N)
    normal_sample = normal_distribution(mu, sigma, N)  # используем стандартный метод для нормального распределения
    return uniform_sample, exp_sample, normal_sample

# Параметры распределений
N = 1000
a, b = 6, 11  # для равномерного распределения
lmbda = 3     # для экспоненциального распределения
mu, sigma = 1, 5  # для нормального распределения

# Генерация выборок
uniform_sample, exp_sample, normal_sample = generate_samples(N, a, b, lmbda, mu, sigma)

# Построение диаграмм накопленных частот (CDF)
plt.figure(figsize=(15, 5))

# Равномерное распределение
plt.subplot(1, 3, 1)
plt.hist(uniform_sample, bins=30, density=True, alpha=0.6, color='g', cumulative=True)
x = np.linspace(a, b, 100)
plt.plot(x, (x - a) / (b - a), 'r--', label='Теоретическая CDF')
plt.title('CDF Равномерное распределение')
plt.legend()

# Экспоненциальное распределение
plt.subplot(1, 3, 2)
plt.hist(exp_sample, bins=30, density=True, alpha=0.6, color='b', cumulative=True)
x = np.linspace(0, np.max(exp_sample), 100)
plt.plot(x, 1 - np.exp(-lmbda * x), 'r--', label='Теоретическая CDF')
plt.title('CDF Экспоненциальное распределение')
plt.legend()

# Нормальное распределение
plt.subplot(1, 3, 3)
plt.hist(normal_sample, bins=30, density=True, alpha=0.6, color='r', cumulative=True)
x = np.linspace(np.min(normal_sample), np.max(normal_sample), 100)
plt.plot(x, stats.norm.cdf(x, mu, sigma), 'g--', label='Теоретическая CDF')
plt.title('CDF Нормальное распределение')
plt.legend()

plt.tight_layout()
plt.show()

# Построение гистограмм и сравнение с теоретическими распределениями
plt.figure(figsize=(15, 5))

# Равномерное распределение
plt.subplot(1, 3, 1)
plt.hist(uniform_sample, bins=30, density=True, alpha=0.6, color='g')
x = np.linspace(a, b, 100)
plt.plot(x, [1/(b - a)] * len(x), 'r--', label='Теоретическая плотность')
plt.title('Гистограмма Равномерное распределение')
plt.legend()

# Экспоненциальное распределение
plt.subplot(1, 3, 2)
plt.hist(exp_sample, bins=30, density=True, alpha=0.6, color='b')
x = np.linspace(0, np.max(exp_sample), 100)
plt.plot(x, lmbda * np.exp(-lmbda * x), 'r--', label='Теоретическая плотность')
plt.title('Гистограмма Экспоненциальное распределение')
plt.legend()

# Нормальное распределение
plt.subplot(1, 3, 3)
plt.hist(normal_sample, bins=30, density=True, alpha=0.6, color='r')
x = np.linspace(np.min(normal_sample), np.max(normal_sample), 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma), 'g--', label='Теоретическая плотность')
plt.title('Гистограмма Нормальное распределение')
plt.legend()

plt.tight_layout()
plt.show()
