def multiplicative_congruential_method(a, m, X0, N):
    result = []
    current = X0

    for _ in range(N):
        next_number = (a * current) % m  # Вычисляем Xi+1
        result.append(next_number / m)    # Получаем Ri
        current = next_number

    return result

# Пример вызова
a = 265
m = 129
X0 = 122
N = 12
sequence = multiplicative_congruential_method(a, m, X0, N)
print(sequence)
