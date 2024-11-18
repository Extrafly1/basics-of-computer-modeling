# import numpy as np
# from scipy.optimize import linprog

# # Пункты поставки (a1, a2, a3, a4)
# supply = np.array([15, 15, 15, 15])

# # Пункты потребления (b1, b2, b3, b4, b5)
# demand = np.array([11, 11, 11, 11, 16])

# # Матрица транспортных затрат
# cost = np.array([
#     [17, 20, 29, 26, 25],
#     [3, 4, 5, 15, 24],
#     [19, 2, 22, 4, 13],
#     [20, 27, 1, 17, 19]
# ])

# # Количество поставок и потребностей
# num_supply = len(supply)
# num_demand = len(demand)

# # Функция цели (затраты)
# c = cost.flatten()

# # Ограничения на поставки
# A_eq = []
# b_eq = []

# # Добавляем ограничения для поставок
# for i in range(num_supply):
#     constraint = np.zeros(num_supply * num_demand)
#     constraint[i * num_demand:(i + 1) * num_demand] = 1
#     A_eq.append(constraint)
#     b_eq.append(supply[i])

# # Добавляем ограничения для потребностей
# for j in range(num_demand):
#     constraint = np.zeros(num_supply * num_demand)
#     for i in range(num_supply):
#         constraint[i * num_demand + j] = 1
#     A_eq.append(constraint)
#     b_eq.append(demand[j])

# # Преобразование в массивы
# A_eq = np.array(A_eq)
# b_eq = np.array(b_eq)

# # Ограничения на неотрицательность
# bounds = [(0, None) for _ in range(num_supply * num_demand)]

# # Решение задачи линейного программирования
# result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# # Вывод результатов
# if result.success:
#     print("Оптимальное распределение:")
#     distribution = result.x.reshape((num_supply, num_demand))
#     print(distribution)
#     print("Минимальные затраты:", result.fun)
# else:
#     print("Не удалось найти оптимальное решение.")

# решите транспортную задачу. имеются четыре пункта 
# поставки одного груза A1, A2, A3, A4, в каждом из 
# которых находиться груз соответственно в количестве 
# a1, a2, a3, a4 тонн и пять пунктов потребления 
# этого груза B1, B2, B3, B4, B5. В пункты B1, 
# B2, B3, B4, B5 требуется доставить соответственно 
# b1, b2, b3, b4, b5 тонн груза. Транспортные расходы 
# при перевозки единиц груза из пункта Ai в пункт Bj 
# расны Cij, где i=1, 2, 3, 4, j=1, 2, 3, 4, 5. Найти 
# такой план закрепления потребителей за постовщиками, 
# чтобы затраты по перевозка были минимальными учитывая 
# a1 = 15, a2 = 15, a3 = 15, a4 = 15, 
# b1 = 11, b2 = 11, b3 = 11, b4 = 11, b5 = 16, 
# C = Cij = (
# (17, 20, 29, 26, 25),
# ( 3,  4,  5, 15, 24),
# (19,  2, 22,  4, 13),
# (20, 27,  1, 17, 19))

from scipy.optimize import linprog

# Данные задачи
supply = [15, 15, 15, 15]  # Поставки: a1, a2, a3, a4
demand = [11, 11, 11, 11, 16]  # Потребности: b1, b2, b3, b4, b5
costs = [  # Матрица транспортных расходов Cij
    [17, 20, 29, 26, 25],
    [3, 4, 5, 15, 24],
    [19, 2, 22, 4, 13],
    [20, 27, 1, 17, 19]
]

# Построение коэффициентов для целевой функции
c = [cost for row in costs for cost in row]  # Векторизация матрицы Cij

# Построение матрицы ограничений
num_sources = len(supply)
num_destinations = len(demand)

# Ограничения на поставки (<= a_i)
A_supply = []
for i in range(num_sources):
    constraint = [0] * (num_sources * num_destinations)
    for j in range(num_destinations):
        constraint[i * num_destinations + j] = 1
    A_supply.append(constraint)
b_supply = supply

# Ограничения на потребности (>= b_j)
A_demand = []
for j in range(num_destinations):
    constraint = [0] * (num_sources * num_destinations)
    for i in range(num_sources):
        constraint[i * num_destinations + j] = 1
    A_demand.append(constraint)
b_demand = demand

# Сборка всех ограничений
A = A_supply + A_demand
b = b_supply + b_demand

# Границы переменных (неотрицательные поставки)
x_bounds = [(0, None) for _ in range(num_sources * num_destinations)]

# Решение задачи линейного программирования
result = linprog(c, A_eq=A, b_eq=b, bounds=x_bounds, method='highs')

# Постобработка результатов
optimal_value = result.fun
optimal_plan = result.x.reshape((num_sources, num_destinations))

optimal_value, optimal_plan
print("Оптимальное значение функции цели:", optimal_value)
print("Оптимальный план закрепления потребителей за постовщиками:")
for i in range(num_sources):
    for j in range(num_destinations):
        print(f"{optimal_plan[i][j]:.0f}", end=' ')
    print()
