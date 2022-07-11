import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2

#esto de figure se puede ver como un lienso que es donde pintan los artista es de cir como una lamina en java
fig = plt.figure()
#ahora le agregare ES PA POSICION DONDE QUIERO QUE PINTE ESE LIENZO
axes = fig.add_axes([0.1,0.1,0.5,0.9])

#esto de figure se puede ver como un lienso que es donde pintan los artista es de cir como una lamina en java
fig = plt.figure()
#LO DE ADENTRO SON CORDENADAS NO SON LOS VALORES DE X : OSEA SON CORDENADAS COMO DONDE ESTARA UBICADA DENTRO DE LA VENTANA SON LOS DOS PRIMEROS VALORES , Y LOS OTROS DOS VALORES SON EL ANCHO Y LARGO
axes = fig.add_axes([0.1,0.1,0.5,0.9])
#----------------------------------------------------

"""ya en esta parte solo reemplazara los valores del eje por los que toma x and y y le generamos la lnea a zul """
axes.plot(x,y, 'b')
plt.show()

fig = plt.figure()
#LO DE ADENTRO SON CORDENADAS NO SON LOS VALORES DE X OSEA SON CORDENADAS COMO DONDE ESTARA UBICADA DENTRO DE LA VENTANA SON LOS DOS PRIMEROS VALORES , Y LOS OTROS DOS VALORES SON EL ANCHO Y LARGO
axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.17,0.55,0.4,0.3])

# axes.plot(x,y, 'b')
# axes2.plot(y,x, 'r:')
# axes2.set_facecolor('grey')
plt.show()

"""AHORA SI AGREGANDO NUESTRSO VALORES A LOS EJES Y QUE LO GRAFIQUE"""

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.17,0.55,0.4,0.3])

axes.plot(x,y, 'b')
"""AHRORA LE ESTOY DICIENDO GRAFIQUE Y AL AXES 2 DELE OTRO FONDOP"""
axes2.plot(y,x, 'r:')
axes2.set_facecolor('grey')
plt.show()

