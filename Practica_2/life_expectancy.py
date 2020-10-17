import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

# Abrir csv
who = pd.read_csv('who_life_expectancy.csv')

# Borrar columnas 'Country', 'Adult Mortality', e 'infant deaths'
who = who.drop(['Country', 'Adult Mortality', 'infant deaths'], axis=1)

# Numerizar columna 'Status'
# who.Status = who.Status.astype("category")
# who.Status = who.Status.cat.codes
del who['Status']

# Eliminar filas con valores nulos
who = who.dropna()

# Guardar la columnna 'Life Expectancy' como los resultados a predecir
y = who['Life expectancy ']
who = who.drop('Life expectancy ', axis=1)

# Pasar datos de entrada a numpy y normalizar valores
x = ((who - who.mean()) / who.std())

# Tamaño de datos de entrada
d_in = (17,)
d_out = 1

#
# De aca para abajo es casi igual que el Ejercicio 3
#

# Creación inicial del modelo, inicialización aleatoria
model = keras.Sequential([
    keras.layers.Dense(
        d_out,
        input_shape=d_in,
        activation=None
    )])

# Compilar el modelo con:
# Descenso de gradiente estocástico (SDG) - Optimizador de 0.001
# Error cuadrático medio
model.compile(
    optimizer=keras.optimizers.SGD(lr=0.005),
    loss='mse',
    metrics=[]
)

# Entrenamiento del model
model.fit(x, y, epochs=100, batch_size=16)

# Imprimir el peso de cada variable
w, b = model.get_weights()
plt.bar(x.columns, w[:, 0])
plt.xticks(x.columns, rotation=90)
plt.show()
