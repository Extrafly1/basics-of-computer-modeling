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

import matplotlib.pyplot as plt
import numpy as np

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

from scipy.optimize import linprog

# Решение задачи линейного программирования
result = linprog(c, A_eq=A, b_eq=b, bounds=x_bounds, method='highs')

# Постобработка результатов
optimal_value = result.fun
optimal_plan = result.x.reshape((num_sources, num_destinations))

# Визуализация оптимального плана в виде тепловой карты
fig, ax = plt.subplots(figsize=(10, 6))

# Создание тепловой карты (heatmap)
cax = ax.matshow(optimal_plan, cmap="coolwarm", aspect="auto")

# Настройка подписей осей
ax.set_xticks(np.arange(num_destinations))
ax.set_yticks(np.arange(num_sources))
ax.set_xticklabels([f"B{i+1}      {demand[i]}" for i in range(num_destinations)])
ax.set_yticklabels([f"A{i+1} \n\n\n {supply[i]}" for i in range(num_sources)])

# Добавление цветовой шкалы
fig.colorbar(cax)

# Отображение значений в ячейках
for i in range(num_sources):
    for j in range(num_destinations):
        ax.text(j, i, f"груз {optimal_plan[i][j]:.1f} \n\n\n{costs[i][j]:.1f}", ha="center", va="center", color="black")

# Заголовок и метки осей
ax.set_title("Оптимальный план закрепления потребителей за постовщиками")
ax.set_xlabel("Пункты потребления")
ax.set_ylabel("Пункты поставки")

# Показываем график
plt.tight_layout()
plt.show()

# Второй график: Распределение затрат на перевозку
total_costs = np.sum(optimal_plan * np.array(costs))

# Создание графика с затратами
fig, ax = plt.subplots(figsize=(10, 6))
bars = []

for i in range(num_sources):
    for j in range(num_destinations):
        cost = optimal_plan[i, j] * costs[i][j]
        bars.append((f"A{i+1} -> B{j+1}", cost))

# Распределение затрат
labels, costs_values = zip(*bars)

ax.barh(labels, costs_values, color="lightblue")
ax.set_xlabel("Затраты на перевозку")
ax.set_title("Распределение затрат на перевозку между пунктами поставки и потребления")

# Добавляем легенду с оптимальным значением функции цели
ax.legend([f"Оптимальное значение функции цели: {optimal_value:.2f}"], loc="upper right")

plt.tight_layout()
plt.show()

