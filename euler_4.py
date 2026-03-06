# МЕТОД ЭЙЛЕРА

import numpy as np
from tools import plot_many, matrix, plot_many_xlim

# ========== НАЧАЛЬНЫЕ ЗНАЧЕНИЯ =============
start_time = 0
end_time = 10
step = 1e-3

t_vector = np.arange(start_time, end_time + step, step)
samples = len(t_vector) # 10001

X0 = matrix([1.5, 1.0, 0.5, 0.0,])
COEF_MATRIX = matrix([[10, 1.0, 2.0, 3.0], 
                      [-20.0, -0.5, 4.0, 5.0],
                      [-2.0, 8.0, 6.0, 4.0],
                      [-3.0, 4.0, 4.0, 6.0]]) # ЗАДАНННАЯ МАТРИЦА

eig = np.linalg.eigvals(COEF_MATRIX)
mu = eig.real.max() + 1.0        # запас 1.0
COEF_MATRIX = COEF_MATRIX - mu*np.eye(COEF_MATRIX.shape[0])

spectr_mx = np.linalg.eigvals(COEF_MATRIX)
print('Собственные значения, спектр мтарицы:')
print(spectr_mx)
#========== МЕТОД ЭЙЛЕРА (НУЖЕН МАЛЕНЬКИЙ ШАГ) 


# ОПРЕДЕЛЯЕМ МТАРИЦУ НУЛЕЙ ДЛЯ РЕШЕНИЯ
size_matrix = (samples, 4)
X = np.zeros(size_matrix, dtype=float)
X[0] = X0

for n in range(samples - 1):
    dXdt = COEF_MATRIX @ X[n] # Производная в текущей точке
    X[n+1] = X[n] + step*dXdt # Шаг Эйлера

x1, x2, x3, x4 = X[:, 0], X[:, 1], X[:,2], X[:,3]

plot_many(y_axis = t_vector,funcs = (x1,x2,x3,x4),
          title=f"Метод Эйлера: X'(t) = A*X(t), Шаг - {step}", 
          xlab = 't, с', ylab = 'x(t)' )

'''Проверить что я праивльное решение
подставить в систему решения, найти производную'''
# ====== Проверка решения: производная "по графику" vs A*X ======
dt = step  # шаг по времени


DXdt_num = np.diff(X, axis=0) / dt          # shape: (samples-1, 2)
t_num = t_vector[:-1]                       # время для этих производных

DXdt = (COEF_MATRIX @ X[:-1].T).T     # shape: (samples-1, 2)


err = DXdt_num - DXdt                # shape: (samples-1, 2)

# ====== Графики производных ======
plot_many(
    y_axis=t_num,
    funcs=(DXdt_num[:, 0], DXdt_num[:, 1],DXdt_num[:, 2],DXdt_num[:, 3]),
    title="Производная (численно): dX/dt ",
    xlab="t, c",
    ylab="dX/dt"
)

plot_many(
    y_axis=t_num,
    funcs=(DXdt[:, 0], DXdt[:, 1], DXdt[:, 2], DXdt[:, 3]),
    title="Производная по системе: A·X",
    xlab="t, c",
    ylab="A·X"
)

# ====== График ошибки ======
plot_many_xlim(
    y_axis=t_num,
    funcs=(err[:, 0], err[:, 1], err[:, 2], err[:, 2] ),
    title="График разности",
    #xlab="t, c",
    ylab="Ошибка"
)




