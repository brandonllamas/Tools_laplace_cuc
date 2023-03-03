import numpy as np
# control es un paquete de Python que contiene rutinas para el análisis y diseño de sistemas de control
# Un sistema de control es un sistema físico que recibe una entrada y produce una salida
import control as ctl
# matplotlib es una biblioteca de Python que permite crear gráficos de alta calidad
import matplotlib.pyplot as plt

# Definición de la función de transferencia del sistema
R = 1000
C = 1e-6
L = 0.1
num = [1, R*C]
den = [L*R*C, R, 1]
G = ctl.tf(num, den)

# Obtener la respuesta temporal de la función de transferencia a una entrada escalón unitario
t, y = ctl.step_response(G)

# Graficar la respuesta temporal
plt.plot(t, y)
plt.xlabel('Tiempo (s)')
plt.ylabel('Salida')
plt.title('Respuesta temporal a una entrada escalón unitario')
plt.grid(True)
plt.show()
