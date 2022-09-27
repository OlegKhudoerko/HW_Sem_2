# 5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

N = 10
data = []
for i in range(N):
    data.append(i)
print('-> ', data)

import random
for k in range(N):
    i = random.randint(0, N-1)
    temp = data[k]
    data[k] = data[i]
    data[i] = temp
print('-> ', data)
