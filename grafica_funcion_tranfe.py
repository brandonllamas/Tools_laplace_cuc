import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Definir la variable 's' como una variable simbólica
s = sp.symbols('s')

# Definir la función de transferencia en términos de 's'
# G = (s*(s-2))/((s+5)*(s**2+6*s+10))
G = ( s + 3) / ((s**3)+2*(s**2)-s-2)
# Ejemplo 2
# G = (s * (s + 3)) / ((s ** 3) + (2 * (s ** 2) - s - 2))

# Encontrar los ceros de la función de transferencia
ceros = sp.solve(G, s)

# Encontrar los polos de la función de transferencia
polos = sp.solve(sp.denom(G), s)

# Convertir los valores simbólicos en números complejos
ceros = [complex(c) for c in ceros]
polos = [complex(p) for p in polos]

# Redondear los valores complejos a 2 decimales
ceros = [round(c.real, 2) + round(c.imag, 2)*1j for c in ceros]
polos = [round(p.real, 2) + round(p.imag, 2)*1j for p in polos]

# Crear un gráfico del plano complejo
fig, ax = plt.subplots()

# Agregar los ceros y polos al gráfico
ax.scatter(np.real(ceros), np.imag(ceros), marker='o', s=50, label='Zeros')
ax.scatter(np.real(polos), np.imag(polos), marker='x', s=50, label='Polos')

# Configurar los ejes del gráfico
ax.axhline(0, color='black', lw=1)
ax.axvline(0, color='black', lw=1)
ax.set_xlabel('Real')
ax.set_ylabel('Imaginario')
ax.set_title('Diagrama de polos y ceros')

# Agregar una leyenda al gráfico
ax.legend()

# Mostrar el gráfico
plt.show()
