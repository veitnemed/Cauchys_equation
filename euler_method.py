# МЕТОД ЭЙЛЕРА

import numpy as np
import matplotlib.pyplot as plt
from tools import plot_many

# ========== НАЧАЛЬНЫЕ ЗНАЧЕНИЯ =============
t0 = 0.0
t1 = 10.0
X0_VECTOR = np.array([1.0,0.0],dtype=float)
COEF_MATRIX = np.array([[0.0,1.0],[-20.0, -0.5]], dtype = float) # ЗАДАНННАЯ МАТРИЦА
#============================================

#========== МЕТОД ЭЙЛЕРА (НУЖЕН МАЛЕНЬКИЙ ШАГ) 
# Параметры
dt = 1e-3
t_vector = np.arange(t0, t1 + dt, dt)
samples = len(t_vector) # 1001

# ОПРЕДЕЛЯЕМ МТАРИЦУ НУЛЕЙ ДЛЯ РЕШЕНИЯ
shape = (samples, 2)
X = np.zeros(shape,dtype=float)
X[0] = X0_VECTOR

for n in range(samples - 1):
    dx = COEF_MATRIX @ X[n] # Производная в текущей точке
    X[n+1] = X[n] + dt*dx # Шаг Эйлера

x1, x2 = X[:, 0], X[:, 1]

plot_many(t_vector,(x1,x2),"Метод Эйлера: X'(t) = A*X(t)" )

