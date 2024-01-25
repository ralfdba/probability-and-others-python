# Probability and others examples using Python
- Python scripts for probability and other
- rfalfarop at gmail dot com
---
### Teoría de probabilidad
La teoría de probabilidad es la rama de las matemáticas que se ocupa de los fenómenos aleatorios y de la incertidumbre. Existen muchos eventos que no se pueden predecir con certeza; ya que su observación repetida bajo un mismo conjunto específico de condiciones puede arrojar resultados distintos, mostrando un comportamiento errático e impredecible. En estas situaciones, la teoría de probabilidad proporciona los métodos para cuantificar las posibilidades, o probabilidades, asociadas con los diversos resultados. Su estudio ha atraído a un gran número de gente, ya sea por su interés intrínseco como por su aplicación con éxito en las ciencias físicas, biológicas y sociales, así como también en áreas de la ingeniería y en el mundo de los negocios.
### Cuantificando la incertidumbre
Ahora bien, en la definición de arriba indicamos que la teoría de probabilidad nos proporciona las herramientas para poder cuantificar la incertidumbre, pero ¿cómo podemos realmente cuantificar estos eventos aleatorios y hacer inferencias sobre ellos? La respuesta a esta pregunta es, a su vez, intuitiva y simple; la podemos encontrar en el concepto del espacio de muestreo.
### El Espacio de muestreo
El espacio de muestreo hace referencia a la idea de que los posibles resultados de un proceso aleatorio pueden ser pensados como puntos en el espacio. En los casos más simples, este espacio puede consistir en sólo algunos puntos, pero en casos más complejos puede estar representado por un continuo, como el espacio en que vivimos. El espacio de muestreo , en general se expresa con la letra S, y consiste en el conjunto de todos los resultados posibles de un experimento. Si el experimento consiste en el lanzamiento de una moneda, entonces el espacio de muestreo será S={cara,seca}, ya que estas dos alternativas representan a todos los resultados posibles del experimento. En definitiva el espacio de muestreo no es más que una simple enumeración de todos los resultados posibles, aunque las cosas nunca suelen ser tan simples como aparentan. Si en lugar de considerar el lanzamiento de una moneda, lanzamos dos monedas; uno podría pensar que el espacio de muestreo para este caso será S={ 2 caras,2 secas,cara y seca}; es decir que de acuerdo con este espacio de muestreo la probabilidad de que obtengamos dos caras es 1 en 3; pero la verdadera probabilidad de obtener dos caras, confirmada por la experimentación, es 1 en 4; la cual se hace evidente si definimos correctamente el espacio de muestreo, que será el siguiente: S={ 2 caras,2 secas,cara y seca,seca y cara}. Como este simple ejemplo nos enseña, debemos ser muy cuidadosos al definir el espacio de muestreo, ya que una mala definición del mismo, puede inducir a cálculos totalmente errados de la probabilidad.
### El concepto de independencia
En teoría de probabilidad, podemos decir que dos eventos son independientes cuando la probabilidad de cada uno de ellos no se ve afecta porque el otro evento ocurra, es decir que no existe ninguna relación entre los eventos. En el lanzamiento de la moneda; la moneda no sabe, ni le interesa saber si el resultado del lanzamiento anterior fue cara; cada lanzamiento es un suceso totalmente aislado el uno del otro y la probabilidad del resultado va a ser siempre 50% en cada lanzamiento.
### Ley de grandes números
si se repite un experimento aleatorio, bajo las mismas condiciones, un número ilimitado de veces; y si estas repeticiones son independientes la una de la otra, entonces la frecuencia de veces que un evento **A** ocurra, convergerá con probabilidad 1 a un número que es igual a la probabilidad de que **A** ocurra en una sola repetición del experimento. Lo que esta ley nos enseña, es que la probabilidad subyacente de cualquier suceso aleatorio puede ser aprendido por medio de la experimentación, simplemente tendríamos que repetirlo una cantidad suficientemente grande de veces. Un error que la gente suele cometer y asociar a esta ley, es la idea de que un evento tiene más posibilidades de ocurrir porque ha o no ha ocurrido recientemente. Esta idea de que las oportunidades de un evento con una probabilidad fija, aumentan o disminuyen dependiendo de las ocurrencias recientes del evento, es un error que se conoce bajo el nombre de la falacia del apostador.
### 3 propiedades de la probabilidad:
- La probabilidad se expresa como un ratio que será un valor positivo menor o igual a 1.
- `
0≤p(A)≤1
`
- La probabilidad de un evento del que tenemos total certeza es 1.
- `
p(S)=1
`
- Si el evento A y el evento B son mutuamente excluyentes.
- `
p(A∪B)=p(A)+p(B)
`
---
### Scripts de ejemplo 01
En este ejemplo, aplicaremos la ley de los grandes números de la probabilidad
para determinar los lanzamientos (a) y su frecuencia para los resultados (b) 
obtenidos
En este ejemplo se logra observar que a medida que se aumenta el número de
repeticiones la frecuencia (b) se va estabilizando
`
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Replication random using numpy
np.random.seed(2131982)
results = []
for a in range( 1,10000 ):
    a = np.random.choice( [0,1], a )
    b = a.mean()
    results.append( b )

#Graph
df = pd.DataFrame( { 'Executions': results } )
df.plot( title='Big Numbers Law', color='r', figsize=( 8,6) )
plt.axhline( 0.5 )
plt.xlabel( 'Executions' )
plt.ylabel( 'Freq' )
plt.show()
`

En este ejemplo, aplicaremos la ley de los grandes números de la probabilidad
para determinar los lanzamientos (a) y su frecuencia para los resultados (b) 
obtenidos
En este ejemplo se logra observar que a medida que se aumenta el número de
repeticiones la frecuencia (b) se va estabilizando en la probabilidad subyacente
del evento, para este ejemplo la probabilidad sera p=1/6
`
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
`
---
### Teoría de conjuntos y probabilidades
Las relaciones que podemos encontrar son:
- **Unión**: La unión de varios eventos simples crea un evento compuesto que ocurre si uno o más de los eventos ocurren. La unión de E y F se escribe E∪F y significa "Ya sea E o F, o ambos E y F".
- **Intersección**: La intersección de dos o más eventos simples crea un evento compuesto que ocurre sólo si ocurren todos los eventos simples. La intersección de E
y F se escribe E∩F y significa "E y F".
- **Complemento**: El complemento de un evento significa todo en el espacio de muestreo que no es ese evento. El complemento del evento E
se escribe varias veces como ∼E, Ec, o E⎯⎯⎯⎯, y se lee como "no E" o "complemento E".
- **Exclusión mutua**: Si los eventos no pueden ocurrir juntos, son mutuamente excluyentes. Siguiendo la misma línea de razonamiento, si dos conjuntos no tienen ningún evento en común, son mutuamente excluyentes.
---
### Teorema del límite central
El otro gran teorema de la teoría de probabilidad es el Teorema del límite central. Este teorema establece que la suma o el promedio de casi cualquier conjunto de variables independientes generadas al azar se aproximan a la Distribución Normal. El Teorema del límite central explica por qué la Distribución Normal surge tan comúnmente y por qué es generalmente una aproximación excelente para la media de casi cualquier colección de datos. Este notable hallazgo se mantiene verdadero sin importar la forma que adopte la distribución de datos que tomemos.
`
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
`
