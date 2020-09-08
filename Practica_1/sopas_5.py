import pandas as pd
import matplotlib.pyplot as plt

# Abrir el .csv
sopas = pd.read_excel('Sopas.xls')

# Generar la matriz en base a los atributos del sopas
pd.plotting.scatter_matrix(sopas)

# Generar el histograma
sopas.hist()

# Mostrar el gráfico
plt.show()
