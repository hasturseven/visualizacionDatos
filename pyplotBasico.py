import matplotlib.pyplot as plt
import numpy as np
#importando las librerias plt es para graficcar
x=np.linspace(0,5,11)
#recorda que en un rango de 0 a 5 tomara 11 valores mi variable x ya que use el linspace
y=x**2
#ahora mostrare la grafica que es una grafica de una funcion cuadratica como observaremos

#plt.plot para darle los valores y la construta
#plt.plot(x,y)

#AHORA VAMOS A MODIFICAR LA GRAFICA PARA PRESENTARLA COMO YO QUIERA arriba me la prsentara de una forma basica aca la presentare como yo quiera el 'rx'  la primera linea es que me presente la linea en rojo y el x es que sea en x y el o es en circulos y asi si le agregamos una linea indica continuidad - , y con : indicara consecucion de puntos etc puedo dejarla sola osea los valores o solo el y quye es el color o yD que sran diamantes etc...
plt.plot(x,y,'yx-')
#y el show para ver la grafica
plt.show()
"""AHORA GRAFICARE UN HISTO GRAMA QUE ES HISTORIA DE VALORES DE Y"""
plt.hist(y)
plt.show()

"""graficandolo de otra manera en este caso una grafica de pie"""
plt.pie(y)
plt.show()
"""AHORA CRANDO CORRELACION ENTRE LAS VARIABLES X AND Y"""
plt.scatter(x,y)
plt.show()
"""DISTRIBUCION DE LOS DATOS ME GENERA UNA GRAFICA DE COMO SE ESTAN DISTRIBUYENDO LOS DATOS"""
plt.boxplot(x)
plt.show()
