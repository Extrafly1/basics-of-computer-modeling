import numpy as np
import simpy

# Параметры модели
mean_arrival = 1  # Среднее время между заданиями (часы)
mean_setup_time = (0.2 + 0.5) / 2  # Среднее время наладки (часы)
std_setup_time = (0.5 - 0.2) / np.sqrt(12)  # Стандартное отклонение наладки (часы)
mean_processing_time = 0.5  # Среднее время выполнения задания (часы)
std_processing_time = 0.1  # Стандартное отклонение выполнения задания (часы)
mean_failure_interval = 20  # Среднее время до поломки (часы)
std_failure_interval = 2  # Стандартное отклонение времени до поломки (часы)
mean_repair_time = (0.1 + 0.5) / 2  # Среднее время ремонта (часы)
std_repair_time = (0.5 - 0.1) / np.sqrt(12)  # Стандартное отклонение ремонта (часы)

# Модель
class Machine:
    def __init__(self, env):
        self.env = env
        self.queue = []
        self.is_broken = False
        self.processed_jobs = 0
        self.setup_times = []
        self.processing_times = []
        self.breakdowns = 0

    def job(self):
        while self.processed_jobs < 500:
            # Интервал между заданиями
            yield self.env.timeout(np.random.exponential(mean_arrival))
            self.queue.append(self.env.now)

            if not self.is_broken:
                # Наладка станка
                setup_time = np.random.uniform(0.2, 0.5)
                self.setup_times.append(setup_time)
                yield self.env.timeout(setup_time)

                # Выполнение задания
                processing_time = np.random.normal(mean_processing_time, std_processing_time)
                if processing_time < 0:  # Не допускаем отрицательное время
                    processing_time = 0
                self.processing_times.append(processing_time)
                yield self.env.timeout(processing_time)

                # Проверка на поломку (добавим вероятность поломки)
                if np.random.random() < (1 / mean_failure_interval):
                    self.is_broken = True
                    self.breakdowns += 1  # Увеличиваем счетчик поломок
                    # Задание уходит в конец очереди
                    if self.queue:
                        self.queue.append(self.queue.pop(0))

            if self.is_broken:
                # Устранение поломки
                repair_time = np.random.uniform(0.1, 0.5)
                yield self.env.timeout(repair_time)
                self.is_broken = False

            self.processed_jobs += 1


# Симуляция
env = simpy.Environment()
machine = Machine(env)
env.process(machine.job())
env.run()

# Результаты
average_setup_time = np.mean(machine.setup_times)
average_processing_time = np.mean(machine.processing_times)
print(f"Среднее время наладки: {average_setup_time:.2f} ч")
print(f"Среднее время выполнения задания: {average_processing_time:.2f} ч")
print(f"Количество поломок: {machine.breakdowns}")
