import numpy as np

# Параметры
num_customers = 400  # Количество клиентов
mean_arrival_time = 0.1  # Среднее время между прибытием клиентов (экспоненциальное)
mean_service_time = 0.5  # Среднее время обслуживания (экспоненциальное)
max_queue_length = 5  # Максимальная длина очереди

# Инициализация очередей для двух автоматов
queues = [[], []]  # Две очереди
lost_customers = 0  # Количество потерянных клиентов
total_wait_time = 0  # Общее время ожидания
total_service_time = 0  # Общее время обслуживания
arrival_times = []  # Время прибытия клиентов
departure_times = []  # Время отъезда клиентов

# Имитация процесса обслуживания клиентов
for i in range(num_customers):
    # Генерация времени между прибытием клиентов
    if i == 0:
        arrival_time = 0
    else:
        arrival_time += np.random.exponential(mean_arrival_time)

    # Определение, в какую очередь встать
    queue_lengths = [len(queues[0]), len(queues[1])]

    # Если обе очереди заполнены
    if queue_lengths[0] >= max_queue_length and queue_lengths[1] >= max_queue_length:
        lost_customers += 1  # Клиент потерян
        continue

    # Выбор очереди
    if queue_lengths[0] < queue_lengths[1]:
        chosen_queue = 0
    elif queue_lengths[0] > queue_lengths[1]:
        chosen_queue = 1
    else:
        chosen_queue = 0  # Предпочтение первому автомату при равных очередях

    # Добавление клиента в очередь
    queues[chosen_queue].append(arrival_time)

    # Обработка клиента
    if len(queues[chosen_queue]) == 1:  # Если это первый клиент в очереди
        # Генерируем время обслуживания
        service_duration = np.random.exponential(mean_service_time)
        departure_time = arrival_time + service_duration
        departure_times.append(departure_time)
        total_service_time += service_duration
    else:
        # Обновляем время отъезда для следующих клиентов
        departure_time = departure_times[-1] + np.random.exponential(mean_service_time)
        departure_times.append(departure_time)

    total_wait_time += (departure_times[-1] - arrival_time) - service_duration

# Статистика
average_queue_length = [len(queue) for queue in queues]
average_wait_time = total_wait_time / num_customers if num_customers > 0 else 0
average_time_in_service = total_service_time / num_customers if num_customers > 0 else 0
percentage_lost_customers = (lost_customers / num_customers) * 100 if num_customers > 0 else 0
# Вывод результатов
print(f"Среднее число клиентов в очереди 1: {average_queue_length[0]}")
print(f"Среднее число клиентов в очереди 2: {average_queue_length[1]}")
print(f"Процент клиентов, которые отказались от обслуживания: {percentage_lost_customers:.2f}%")
print(f"Среднее время пребывания клиента на заправке: {average_time_in_service:.2f} времени единиц")
