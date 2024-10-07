import math
import numpy as np
import matplotlib.pyplot as plt

# Функция для оценки математического ожидания и дисперсии
def calculate_stats(sample):
    mean = np.mean(sample)
    variance = np.var(sample)
    return mean, variance

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

# Генерация выборок
N = 1000
a, b = 6, 11  # для равномерного распределения
lmbda = 3     # для экспоненциального распределения
mu, sigma = 1, 5  # для нормального распределения

# Генерация выборок
uniform_sample, exp_sample, normal_sample = generate_samples(N, a, b, lmbda, mu, sigma)

# Объёмы выборки, для которых мы будем вычислять оценки
sample_sizes = [10, 20, 50, 100, 1000]

# Подготовим списки для хранения оценок математического ожидания и дисперсии
uniform_means, uniform_vars = [], []
exp_means, exp_vars = [], []
normal_means, normal_vars = [], []

# Для каждого объёма выборки вычисляем оценки
for size in sample_sizes:
    # Равномерное распределение
    uniform_mean, uniform_var = calculate_stats(uniform_sample[:size])
    uniform_means.append(uniform_mean)
    uniform_vars.append(uniform_var)
    
    # Экспоненциальное распределение
    exp_mean, exp_var = calculate_stats(exp_sample[:size])
    exp_means.append(exp_mean)
    exp_vars.append(exp_var)
    
    # Нормальное распределение
    normal_mean, normal_var = calculate_stats(normal_sample[:size])
    normal_means.append(normal_mean)
    normal_vars.append(normal_var)

# Построение графиков
plt.figure(figsize=(12, 8))

# Математическое ожидание
plt.subplot(2, 1, 1)
plt.plot(sample_sizes, uniform_means, 'g-o', label='Равномерное')
plt.plot(sample_sizes, exp_means, 'b-o', label='Экспоненциальное')
plt.plot(sample_sizes, normal_means, 'r-o', label='Нормальное')
plt.axhline(y=(a+b)/2, color='g', linestyle='--', label=f'Теоретическое (Равн.): {(a+b)/2}')
plt.axhline(y=1/lmbda, color='b', linestyle='--', label=f'Теоретическое (Эксп.): {1/lmbda}')
plt.axhline(y=mu, color='r', linestyle='--', label=f'Теоретическое (Норм.): {mu}')
plt.title('Математическое ожидание в зависимости от объема выборки')
plt.xlabel('Объем выборки')
plt.ylabel('Математическое ожидание')
plt.legend()

# Дисперсия
plt.subplot(2, 1, 2)
plt.plot(sample_sizes, uniform_vars, 'g-o', label='Равномерное')
plt.plot(sample_sizes, exp_vars, 'b-o', label='Экспоненциальное')
plt.plot(sample_sizes, normal_vars, 'r-o', label='Нормальное')
plt.axhline(y=((b-a)**2)/12, color='g', linestyle='--', label=f'Теоретическая (Равн.): {((b-a)**2)/12}')
plt.axhline(y=1/(lmbda**2), color='b', linestyle='--', label=f'Теоретическая (Эксп.): {1/(lmbda**2)}')
plt.axhline(y=sigma**2, color='r', linestyle='--', label=f'Теоретическая (Норм.): {sigma**2}')
plt.title('Дисперсия в зависимости от объема выборки')
plt.xlabel('Объем выборки')
plt.ylabel('Дисперсия')
plt.legend()

plt.tight_layout()
plt.show()

# Вывод значений для каждого объёма выборки
for i, size in enumerate(sample_sizes):
    print(f"Объем выборки: {size}")
    print(f"Равномерное распределение: Математическое ожидание = {uniform_means[i]:.4f}, Дисперсия = {uniform_vars[i]:.4f}")
    print(f"Экспоненциальное распределение: Математическое ожидание = {exp_means[i]:.4f}, Дисперсия = {exp_vars[i]:.4f}")
    print(f"Нормальное распределение: Математическое ожидание = {normal_means[i]:.4f}, Дисперсия = {normal_vars[i]:.4f}")
    print("-" * 50)
