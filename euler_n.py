# МЕТОД ЭЙЛЕРА для n

import numpy as np
from tools import plot_many, matrix

# ========== НАЧАЛЬНЫЕ ЗНАЧЕНИЯ =============
n = int(input('Ввведите размерность матрицы: '))
start_time = 0.0
end_time = 0.1
step = 1e-3

t_vector = np.arange(start_time, end_time + step, step)
samples = len(t_vector) # 10001

X0 = np.random.randn(n)
COEF_MATRIX = np.random.randn(n,n) # ЗАДАНННАЯ МАТРИЦА

#========== МЕТОД ЭЙЛЕРА ======================


# ОПРЕДЕЛЯЕМ МТАРИЦУ НУЛЕЙ ДЛЯ РЕШЕНИЯ
size_matrix = (samples, n)
X = np.zeros(size_matrix, dtype=float)
X[0] = X0

for idx in range(samples - 1):
    dXdt = COEF_MATRIX @ X[idx] # Производная в текущей точке
    X[n+1] = X[n] + step*dXdt # Шаг Эйлера

x1, x2 = X[:, 0], X[:, 1]

rows_x = []
for idx in range(X.shape[1]):
    rows_x.append(X[:,idx])

plot_many(y_axis = t_vector,funcs = rows_x,
          title=f"Метод Эйлера: X'(t) = A*X(t), Шаг - {step}", 
          xlab = 't, с', ylab = 'x(t)' )


'''Проверить что я праивльное решение
подставить в систему решения, найти производную'''
dt = t_vector
DXdt_num = np.diff(X,axis=)