import matplotlib.pyplot as plt
import numpy as np
#importando las librerias plt es para graficcar
x=np.linspace(0,5,11)
#recorda que en un rango de 0 a 5 tomara 11 valores mi variable x ya que use el linspace
y=x**2
#ahora mostrare la grafica que es una grafica de una funcion cuadratica como observaremos

#plt.plot para darle los valores y la construta
#plt.plot(x,y)

#AHORA VAMOS A MODIFICAR LA GRAFICA PARA PRESENTARLA COMO YO QUIERA arriba me la prsentara de una forma basica aca la presentare como yo quiera
plt.plot(x,y,'y','rx')
#y el show para ver la grafica
plt.show()
