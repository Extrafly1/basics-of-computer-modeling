import simpy
import numpy as np

# Параметры задачи
arrival_interval_mean = 0.1  # средний интервал прибытия клиентов
service_time_mean = 0.5      # среднее время обслуживания
queue_limit = 5              # ограничение длины очереди
num_cars = 400

# Глобальные переменные для анализа
lost_clients = 0
total_time_in_system = 0
total_served_clients = 0
queue_lengths = [[], []]
departure_intervals = []

def car_generator(env, stations):
    global lost_clients
    last_departure_time = env.now
    for _ in range(num_cars):
        yield env.timeout(np.random.exponential(arrival_interval_mean))
        shortest_queue = min(stations, key=lambda x: len(x.queue))
        
        if len(shortest_queue.queue) < queue_limit:
            env.process(service_car(env, shortest_queue, last_departure_time))
            last_departure_time = env.now
        else:
            lost_clients += 1

def service_car(env, station, last_departure_time):
    global total_time_in_system, total_served_clients
    arrival_time = env.now
    with station.request() as req:
        yield req
        service_time = np.random.exponential(service_time_mean)
        yield env.timeout(service_time)
        
        total_time_in_system += env.now - arrival_time
        total_served_clients += 1
        queue_lengths[stations.index(station)].append(len(station.queue))
        departure_intervals.append(env.now - last_departure_time)

# Модель
env = simpy.Environment()
stations = [simpy.Resource(env, capacity=1) for _ in range(2)]

env.process(car_generator(env, stations))
env.run()

# Анализ
average_queue_length_1 = sum(queue_lengths[0]) / len(queue_lengths[0])
average_queue_length_2 = sum(queue_lengths[1]) / len(queue_lengths[1])
rejection_rate = (lost_clients / num_cars) * 100
average_departure_interval = sum(departure_intervals) / len(departure_intervals)
average_time_in_station = total_time_in_system / total_served_clients

print("Среднее число клиентов в очереди 1:", average_queue_length_1)
print("Среднее число клиентов в очереди 2:", average_queue_length_2)
print("Процент отказов от обслуживания:", rejection_rate)
print("Средний интервал времени между отъездами клиентов:", average_departure_interval)
print("Среднее время пребывания клиента на заправке:", average_time_in_station)
