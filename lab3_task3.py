def lemer_method(R0, g, N):
    result = [R0]
    current = R0

    for _ in range(N - 1):
        next_number = (g * current) % 1  # Оставляем только дробную часть
        result.append(next_number)
        current = next_number

    return result

# Пример вызова
R0 = 0.585
g = 927
N = 5
sequence = lemer_method(R0, g, N)
print(sequence)
