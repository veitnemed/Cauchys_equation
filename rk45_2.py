# МЕТОД РУНГЕ-КУТТА 4-ого, 5-ого пордка
# Эйлер считает, что на всём маленьком отрезке времени скорость поxти не меняется 
# RK45 два приближения 4-го порядка и 5-го порядка 
# solve_ivp решает проблему Коши, IVP - Initial Value Problem

import numpy as np
from scipy.integrate import solve_ivp
from tools import plot_many, matrix

# =======  ВХОД =======
t0, t1 = 0.0, 10.0
step = 1e-3

A = matrix([[0.0, 1.0], [-20.0, -0.5]])
spectr_mx = np.linalg.eigvals(A)
print(spectr_mx)
X0 = matrix([1.0, 0.0])
t = np.arange(t0, t1 + step, step)

# dX/dt = A @ X
def rhs(t, X):
    return A @ X


sol = solve_ivp(rhs, (t0, t1), X0, t_eval=t, method="RK45") # type OdeResult
X = sol.y.T # Обращаемся к обхекту sol : y - значение решения, T - транспонируем 
x1, x2 = X[:, 0], X[:, 1]

plot_many(y_axis=t, funcs=(x1, x2),
          title=f"Метод Рунге-Кутта: X'(t)=A·X(t), шаг={step}",
          xlab="t, c", ylab="x(t)")

plot_many(y_axis=x1, funcs=(x2,),
          title="Фазовый портрет: x2(x1)",
          xlab="x1(t)", ylab="x2(t)")