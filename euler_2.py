# МЕТОД ЭЙЛЕРА

import numpy as np
from tools import plot_many, matrix

# ========== НАЧАЛЬНЫЕ ЗНАЧЕНИЯ =============
start_time = 0.0
end_time = 10.0
step = 1e-3

t_vector = np.arange(start_time, end_time + step, step)
samples = len(t_vector) # 10001

X0 = matrix([1.0, 0.0])
COEF_MATRIX = matrix([[0.0, 1.0], [-20.0, -0.5]]) # ЗАДАНННАЯ МАТРИЦА


#========== МЕТОД ЭЙЛЕРА (НУЖЕН МАЛЕНЬКИЙ ШАГ) 


# ОПРЕДЕЛЯЕМ МТАРИЦУ НУЛЕЙ ДЛЯ РЕШЕНИЯ
size_matrix = (samples, 2)
X = np.zeros(size_matrix, dtype=float)
X[0] = X0

for n in range(samples - 1):
    dXdt = COEF_MATRIX @ X[n] # Производная в текущей точке
    X[n+1] = X[n] + step*dXdt # Шаг Эйлера

x1, x2 = X[:, 0], X[:, 1]

plot_many(y_axis = t_vector,funcs = (x1,x2),
          title=f"Метод Эйлера: X'(t) = A*X(t), Шаг - {step}", 
          xlab = 't, с', ylab = 'x(t)' )
plot_many(y_axis = x1 ,funcs = (x2,) ,
          title="Фазовый портрет: траектория x1(x2(t))", 
          xlab = 'x2(t)', ylab = 'x1(t)' )

