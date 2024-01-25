"""
En este ejemplo, aplicaremos la ley de los grandes números de la probabilidad
para determinar los lanzamientos (a) y su frecuencia para los resultados (b) 
obtenidos
En este ejemplo se logra observar que a medida que se aumenta el número de
repeticiones la frecuencia (b) se va estabilizando en la probabilidad subyacente
del evento, para este ejemplo la probabilidad sera p=1/6
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Replication random using numpy
np.random.seed(2131982)
results = []
for a in range( 1,10000 ):
    a = np.random.choice( [0,1], a, p=[5/6, 1/6] )
    b = a.mean()
    results.append( b )

#Graph
df = pd.DataFrame( { 'Executions': results } )
df.plot( title='Big Numbers Law', color='r', figsize=( 8,6) )
plt.axhline( 1/6 )
plt.xlabel( 'Executions' )
plt.ylabel( 'Freq' )
plt.show()
