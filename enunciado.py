'''
Se desea implementar un algoritmo que permita controlar la temperatura de un servidor web, de manera que se mantenga en
un rango de valores seguros y óptimos para su funcionamiento. Para ello, se cuenta con un sensor de temperatura conectado
al servidor, y se desea utilizar la función de transferencia del sistema para diseñar un controlador que regule la temperatura.

El servidor web cuenta con un sistema de enfriamiento que funciona mediante un ventilador controlado por un circuito RLC
 en serie. La función de transferencia del sistema se puede expresar como:

G(s) = (1 + RCs) / (1 + LRCs^2)

donde R es la resistencia del circuito en ohmios, C es la capacitancia en faradios, L es la inductancia en henrios, y s
es la variable compleja que representa la frecuencia de la señal de entrada.

Para diseñar el controlador, se desea mantener la temperatura del servidor en un rango de 30-35 grados Celsius, con una
precisión de +/- 0.5 grados Celsius y un tiempo de respuesta máximo de 5 segundos. Se desea también que el controlador
sea estable, sin oscilaciones ni sobrecalentamiento.

El controlador diseñado es un controlador PID (Proporcional-Integral-Derivativo) con los siguientes parámetros:

Kp: Ganancia proporcional del controlador. Se ajusta para obtener la precisión deseada.
Ti: Tiempo integral del controlador. Se utiliza para obtener la estabilidad del sistema.
Td: Tiempo derivativo del controlador. Se utiliza para obtener la respuesta rápida del sistema.
N: Filtro de anticipación del controlador. Se utiliza para reducir el tiempo de respuesta del sistema.
La simulación del sistema con controlador se realiza con un tiempo de muestreo Ts de 0.1 segundos y un tiempo final de
la simulación Tf de 10 segundos. El vector de tiempo t se utiliza para graficar los resultados.

Durante la simulación, se mantiene un setpoint de temperatura de 32 grados Celsius. La señal de control u se calcula a
 partir del error de temperatura e, utilizando la ganancia proporcional Kp. Se limita la señal de control a un valor
 máximo de 10 y un valor mínimo de 0. La simulación del sistema se realiza utilizando el método de Euler para evitar problemas
 de estabilidad.

El gráfico resultante muestra la evolución de la temperatura del servidor y el setpoint a lo largo del tiempo.

'''

import numpy as np
import control as ctl
import matplotlib.pyplot as plt

# Definición de la función de transferencia del sistema
# R Significa la resistencia del circuito. Para este ejemplo, se asume que R = 1000 ohmios
R = 1000
C = 1e-6 # C Significa la capacitancia. Para este ejemplo, se asume que C = 1 microfaradio
L = 0.1 # L Significa la inductancia. Para este ejemplo, se asume que L = 0.1 henrios
num = [1, R*C] # Numerador de la función de transferencia
den = [L*R*C, R, 1] # Denominador de la función de transferencia
G = ctl.tf(num, den) # Función de transferencia del sistema

# Diseño del controlador
Ts = 0.1 # Tiempo de muestreo de la simulación. Esto sirve para evitar problemas de estabilidad y para reducir el tiempo de simulación
Tf = 10 # Tiempo final de la simulación en segundos
t = np.arange(0, Tf, Ts) # Vector de tiempo para la simulación. Se utiliza para graficar los resultados
sp = 32 # Setpoint de temperatura en grados Celsius. Es la temperatura que se desea mantener
Kp = 1 # Ganancia proporcional del controlador. Se debe ajustar para obtener la precisión deseada
Ti = 5 # Tiempo integral. El tiempo integral es el que se utiliza para obtener la estabilidad del sistema
Td = 1 # Tiempo derivativo del controlador. El tiempo derivativo es el que se utiliza para obtener la respuesta rápida del sistema
N = 10 # Filtro de anticipación del controlador. El filtro de anticipación es el que se utiliza para reducir el tiempo de respuesta
# del sistema
ctrl = ctl.tf( [Kp*Td*N+Kp*Ti, Kp*(1+Ts/(2*Ti))-2*Kp*Td*N, Kp*(1-Ts/(2*Ti))-Kp*Ti/Ts, Kp*(Ts/(2*Ti))], [1, -1, 0, 0], Ts) # Controlador PID

# Simulación del sistema con controlador
T = np.zeros_like(t) # Vector de temperatura
T[0] = 30 # Temperatura inicial
u = 0 # Señal de control inicial
for i in range(1, len(t)):
    e = sp - T[i-1] # Error de temperatura
    # Señal de control con límites
    u = max(min(u + Kp*e, 10), 0)
    # Simulación del sistema.Para evitar problemas de estabilidad, se utiliza el método de Euler
    T[i] = T[i-1] + Ts*(u - T[i-1]/(R*C))

    # Impresión de resultados
    print("Tiempo: {:.2f} s, Temperatura: {:.2f} C, Señal de control: {:.2f}".format(t[i], T[i], u))

# Graficar resultados
plt.figure()
plt.plot(t, T, label='Temperatura')
plt.plot([0, Tf], [sp, sp], '--', label='Setpoint')
plt.xlabel('Tiempo (s)')
plt.ylabel('Temperatura (C)')
plt.title('Simulación del sistema con controlador PID')
plt.legend()
plt.grid(True)
plt.show()