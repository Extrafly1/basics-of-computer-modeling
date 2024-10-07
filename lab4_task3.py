import math
import matplotlib.pyplot as plt

# Линейный конгруэнтный генератор
seed = 1

def next_random():
    global seed
    a = 1103515245
    c = 12345
    m = 2**31
    seed = (a * seed + c) % m
    return seed

# Генерация равномерного распределения
def uniform_distribution(a, b, N):
    random_numbers = []
    for _ in range(N):
        random_num = a + (b - a) * (next_random() / (2**31 - 1))
        random_numbers.append(random_num)
    return random_numbers

# Генерация экспоненциального распределения
def exponential_distribution(lmbda, N):
    if lmbda <= 0:
        raise ValueError("Lambda must be greater than 0")
    random_numbers = []
    for _ in range(N):
        u = next_random() / (2**31 - 1)
        exp_sample = - (1 / lmbda) * math.log(1 - u)
        random_numbers.append(exp_sample)
    return random_numbers

# Генерация нормального распределения
def normal_distribution(mu, sigma, N):
    random_numbers = []
    for _ in range(N):
        uniform_samples = [next_random() / (2**31 - 1) for _ in range(12)]
        normal_sample = sum(uniform_samples) - 6
        normal_value = mu + sigma * (normal_sample / math.sqrt(12))
        random_numbers.append(normal_value)
    return random_numbers

# Вычисление статистики
def calculate_statistics(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return mean, variance

def main():
    N = 1000

    # Параметры для равномерного распределения
    a_uniform = 0
    b_uniform = 10
    uniform_samples = uniform_distribution(a_uniform, b_uniform, N)
    uniform_mean, uniform_variance = calculate_statistics(uniform_samples)
    print(f"Uniform Distribution: Mean = {uniform_mean:.2f}, Variance = {uniform_variance:.2f}")

    # Параметры для экспоненциального распределения
    lmbda_exponential = 1
    exponential_samples = exponential_distribution(lmbda_exponential, N)
    exponential_mean, exponential_variance = calculate_statistics(exponential_samples)
    print(f"Exponential Distribution: Mean = {exponential_mean:.2f}, Variance = {exponential_variance:.2f}")

    # Параметры для нормального распределения
    mu_normal = 0
    sigma_normal = 1
    normal_samples = normal_distribution(mu_normal, sigma_normal, N)
    normal_mean, normal_variance = calculate_statistics(normal_samples)
    print(f"Normal Distribution: Mean = {normal_mean:.2f}, Variance = {normal_variance:.2f}")

    # Визуализация распределений
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.hist(uniform_samples, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.title('Uniform Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 2)
    plt.hist(exponential_samples, bins=30, alpha=0.7, color='green', edgecolor='black')
    plt.title('Exponential Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.subplot(3, 1, 3)
    plt.hist(normal_samples, bins=30, alpha=0.7, color='red', edgecolor='black')
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
