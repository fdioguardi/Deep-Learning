import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv('iris.csv')

# Eliminar la columna del nombre (los strings causan problemas con las cuentas)
del iris["name"]

zscore = (iris - iris.mean()) / iris.std()
min_max = (iris - iris.min()) / (iris.max() - iris.min())

print("Normalizado con z-score \n", zscore)
print("Normalizado con min-max \n", min_max)

zscore.hist()
min_max.hist()
plt.show()
