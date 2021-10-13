
"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

m1 = [
    [2, 3, 4],
    [5, 6, 7],
    [2, 2, 2]
]

m2 = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

m3 = [[sum(map(lambda x: x[0] * x[1], zip(m1[i], [c[j] for c in m2]))) for j in range(len(m2[0]))] for i in
      range(len(m1))]

for r in m3:
    print(r)
