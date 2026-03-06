
import numpy as np
from scipy.integrate import solve_ivp
from tools import plot_many, matrix, plot_many_xlim

start_time = 0
end_time = 10
step = 1e-3

t_vector = np.arange(start_time, end_time + step, step)
samples = len(t_vector) # 10001

X0 = matrix([1.0,0.5, 0.0])
COEF_MATRIX = matrix([[10, 1.0, 2.0], [-20.0, -0.5, 4.0],[-2.0,8.0,6.0]]) # ЗАДАНННАЯ МАТРИЦА

eig = np.linalg.eigvals(COEF_MATRIX)
mu = eig.real.max() + 1.0        # запас 1.0
COEF_MATRIX = COEF_MATRIX - mu*np.eye(COEF_MATRIX.shape[0])

spectr_mx = np.linalg.eigvals(COEF_MATRIX)
print('Собственные значения, спектр мтарицы:')
print(spectr_mx)

def rhs(t, X):
    return COEF_MATRIX @ X


sol = solve_ivp(rhs, (start_time, end_time), X0, t_eval=t_vector, method="RK45") # type OdeResult
X = sol.y.T # Обращаемся к обхекту sol : y - значение решения, T - транспонируем 
x1, x2, x3 = X[:, 0], X[:, 1], X[:,2]


m = max(max(x1),max(x2),max(x3))
print(m)
plot_many(y_axis=t_vector, funcs=(x1, x2, x3),
          title=f"Метод Рунге-Кутта: X'(t)=A·X(t)",
          xlab="t, c", ylab="x(t)")

