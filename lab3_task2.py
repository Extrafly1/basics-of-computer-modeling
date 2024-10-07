def modified_middle_square_method(R0, R1, N):
    """
    Генерация последовательности псевдослучайных чисел модифицированным методом Неймана.

    :param R0: первое начальное число (например, 0.5836)
    :param R1: второе начальное число (например, 0.2176)
    :param N: количество чисел в последовательности
    :return: список сгенерированных псевдослучайных чисел
    """
    result = [R0, R1]  # Инициализируем список первыми двумя числами
    for _ in range(N - 2):  # Начинаем с третьего числа
        # Вычисляем среднее значение между последними двумя числами
        avg = (result[-2] + result[-1]) / 2
        
        # Возводим среднее в квадрат и убираем точку
        squared = str(avg ** 2).replace('.', '')
        if len(squared) < 8:
            squared = squared.zfill(8)  # Добавляем нули, если строка меньше 8 символов
        
        # Берем четыре средние цифры
        next_number = float('0.' + squared[2:6])
        result.append(next_number)  # Добавляем новое число в список
    
    return result

# Пример вызова
R0 = 0.5836
R1 = 0.2176
N = 6
sequence = modified_middle_square_method(R0, R1, N)
print(sequence)
