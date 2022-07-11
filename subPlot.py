import matplotlib.pyplot as plt
import numpy as np

""" Subplot permite crear gráficos dentro de una gráfica. Esto lo hace a través de una matriz de gráficos y se puede acceder a ellos a través de índices:"""

x=np.linspace(0,5,11)
y=x**2
#presentando dos graficas a la vez usamos subplot (el primer parametro es el numero de filas, el numero de columnas,y el index)
"""ENTONCES COMO ESTA ES MI PRIMERA GRAFIA ESTARA EN LA FILA 1 COLUMNA 1 E INDICE 1"""
#y este instruccion es para asignarle la posicion a la grafica que estamos pasando como una fila y dos columnas me generan dos indices pues tengo que ir asignando el primero y luego el segundo como se ve
plt.subplot(1,2,1)
#-----------------------------
plt.plot(x,y,'ro-')
"""ENTONCES COMO ESTA ES MI SEGUNDA GRAFICA VA A ESTAR EN LA FILA 1 COLUMNA 2 POSICION QUE ES INDEX 2"""

plt.subplot(1,2,2)
plt.hist(y)
plt.show()
#---------------------- ahora con otras graficas---------------
"""ENTONCES COMO ESTA ES MI PRIMERA GRAFIA ESTARA EN LA FILA 1 COLUMNA 1 E INDICE 1 per oen este caso como son enter comillas dos graficas ya que use otra plt.plot qu ees crear una grafica la metera las dos lineas en la misma grafica"""
#y este instruccion es para asignarle la posicion a la grafica que estamos pasando mirrar el indix
plt.subplot(1,2,1)
#-----------------------------
plt.plot(x,y,'rx-')
plt.plot(y,x,'bD:')
"""ENTONCES COMO ESTA ES MI SEGUNDA GRAFICA VA A ESTAR EN LA FILA 1 COLUMNA 2 POSICION QUE ES INDEX 2"""
plt.subplot(1,2,2)
plt.pie(y)
plt.show()
#--------------- ahra tendre son dos filas y una columna osea cambiamos el orden de la matriz para presentar mas diferentes la graficas ---------- --------------------------
plt.subplot(2,1,1)
plt.plot(x,y,'rx-')
plt.plot(y,x,'bD:')

"""ENTONCES COMO ESTA ES MI SEGUNDA GRAFICA VA A ESTAR EN LA FILA 1 COLUMNA 2 POSICION QUE ES INDEX 2"""
plt.subplot(2,1,2)
plt.pie(y)
plt.show()
