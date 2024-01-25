"""
En este ejemplo se abordara el teorema del limite central. Basicamente
este teorema establece que la suma o el promedio de casi cualquier conjunto
de variables independientes generadas al azar se aproxima a la distribución
normal. Se utiliza generalmente para obtener la media de casi cualquier
coleccion de datos sin importar la distribución y variedad de datos que se
disponga.
Como nos muestra este ejemplo, al graficar la distribución de las medias de 
las distribuciones Binomial, Poisson, Geométrica y Exponencial.
Todas ellas responden a la famosa forma de campana de la Distribución Normal
"""
prob = 1.0
asistentes = 50

for i in range(asistentes):
    prob = prob * (365-i)/365

print( "Probabilidad de que exista una misma fecha de cumpleaños es {0:.2f}"
      .format(1 - prob))