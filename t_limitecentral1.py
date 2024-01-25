"""
En este ejemplo se abordara el teorema del limite central. Basicamente
este teorema establece que la suma o el promedio de casi cualquier conjunto
de variables independientes generadas al azar se aproxima a la distribución
normal. Se utiliza generalmente para obtener la media de casi cualquier
coleccion de datos sin importar la distribución y variedad de datos que se
disponga.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Replication random using numpy
np.random.seed(2131982)
muestra_binomial = []
muestra_exp = []
muestra_possion = []
muestra_geometric = []
mu = .9
lam = 1.0
size=1000

for i in range(1,20000):
    muestra = np.random.binomial(1, mu, size=size)
    muestra_binomial.append(muestra.mean())
    muestra = np.random.exponential(scale=2.0,size=size)
    muestra_exp.append(muestra.mean())
    muestra = np.random.geometric(p=.5, size=size)
    muestra_geometric.append(muestra.mean())
    muestra = np.random.poisson (lam=lam, size=size)
    muestra_possion.append(muestra.mean()) 

df = pd.DataFrame({ 'binomial' : muestra_binomial, 
                     'poission' : muestra_possion,
                     'geometrica' : muestra_geometric,
                    'exponencial' : muestra_exp})

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
df.binomial.hist(ax=axes[0,0], alpha=0.9, bins=1000)
df.exponencial.hist(ax=axes[0,1],bins=1000)
df.poission.hist(ax=axes[1,0],bins=1000)
df.geometrica.hist(ax=axes[1,1],bins=1000)

axes[0,0].set_title('Binomial')
axes[0,1].set_title('Poisson')
axes[1,0].set_title('Geométrica')
axes[1,1].set_title('Exponencial')
plt.show()
