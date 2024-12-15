import numpy as np

# Параметры
num_tasks = 500  # Количество заданий
mean_task_arrival = 1  # Среднее время между поступлениями заданий (часы)
mean_setup_time = (0.2 + 0.5) / 2  # Среднее время наладки (часы)
mean_execution_time = 0.5  # Среднее время выполнения задания (часы)
std_execution_time = 0.1  # Стандартное отклонение времени выполнения задания (часы)
mean_break_time = 20  # Среднее время между поломками (часы)
std_break_time = 2  # Стандартное отклонение времени между поломками (часы)
mean_repair_time = (0.1 + 0.5) / 2  # Среднее время устранения поломки (часы)

# Начальные условия
current_time = 0  # Текущее время
task_queue = []  # Очередь заданий
total_execution_time = 0  # Общее время выполнения заданий
num_breaks = 0  # Количество поломок

# Моделирование поступления заданий
for _ in range(num_tasks):
    # Генерируем интервал между заданиями
    inter_arrival_time = np.random.exponential(mean_task_arrival)
    current_time += inter_arrival_time
    task_queue.append(current_time)

# Обработка заданий
while task_queue:
    # Берем следующее задание из очереди
    task_time = task_queue.pop(0)

    # Время наладки
    setup_time = np.random.uniform(0.2, 0.5)
    current_time += setup_time

    # Время выполнения задания
    execution_time = np.random.normal(mean_execution_time, std_execution_time)
    current_time += execution_time

    # Учет времени выполнения задания
    total_execution_time += execution_time

    # Генерируем время до поломки
    if np.random.normal(mean_break_time, std_break_time) < 0:
        # Поломка происходит
        num_breaks += 1
        repair_time = np.random.uniform(0.1, 0.5)
        current_time += repair_time
        # Задание удаляется и помещается в начало очереди
        task_queue.insert(0, task_time)  # Возвращаем задание в начало очереди

# Вывод результатов
print(f"Общее время выполнения заданий: {total_execution_time:.2f} часов")
print(f"Количество поломок: {num_breaks}")
print(f"Среднее время выполнения задания: {total_execution_time / num_tasks:.2f} часов")
