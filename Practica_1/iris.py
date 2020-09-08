import pandas as pd
import matplotlib.pyplot as plt

# Abrir el .csv
iris = pd.read_csv('iris.csv')

# Generar la matriz en base a los atributos del dataframe
pd.plotting.scatter_matrix(iris)

# Generar el histograma
iris.hist()

# Mostrar el gráfico
plt.show()
