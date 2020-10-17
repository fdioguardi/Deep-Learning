import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

# Abrir csv
covid_df = pd.read_csv('COVID-19_Daily_Testing_-_By_Person.csv')

# Borrar filas NaN
covid_df = covid_df.dropna()

# Ordenar el dataframe según la columna 'Date'
covid_df.sort_values(by=['Date'], inplace=True)

# Borrar columna 'Day'
covid_df = covid_df.drop(['Day', 'Date'], axis=1)

# Insertar columna incremental 'Tiempo'
covid_df.insert(0, 'Tiempo', range(len(covid_df)))

# Creación del modelo
x = covid_df[["People Positive - Age 30-30"]]
x = (x-x.min())/(x.max()-x.min())

y = covid_df[['People Positive - Total']]

model = keras.Sequential([
    keras.layers.Dense(
        1,
        input_shape=(x.shape[1],),
        activation=None
    )
])

# Compilar el modelo
model.compile(
    optimizer=keras.optimizers.SGD(lr=0.001),
    loss='mse',
    metrics=[]
)

# Entrenar el modelo
model.fit(x, y, epochs=100, batch_size=16)

# Predecir
y_predictions = model.predict(x)

# Graficar el resultado en azul vs los datos en rojo
plt.plot(covid_df['Tiempo'], covid_df['People Positive - Total'], 'ro')
plt.plot(covid_df['Tiempo'], y_predictions, 'bo')

plt.xlabel('Tiempo')
plt.ylabel('People Positive - Total')

plt.show()
