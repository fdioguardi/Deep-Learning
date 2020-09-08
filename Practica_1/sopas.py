# En este ejercicio deberá implementar la función `calcular` y verificar su correcto funcionamiento

import pandas as pd
import numpy as np


def verificar_resultado(expected, calculated, title):
    # Verifica si {expected} es igual a {calculated} con unna tolerancia de 1e-2 (dos decimales)
    tolerance = 1e-2
    title = title.ljust(35)
    if np.abs(expected-calculated) > tolerance:
        print(f"- {title}: error (esperaba {expected}, obtuve {calculated:.2f})")
    else:
        print(f"+ {title}: bien  (esperaba {expected}, obtuve {calculated:.2f}).")


def calcular(dataframe):

    ###### 1) Calcular el valor promedio del atributo GRASA ######
    # COMPLETAR
    promedio_grasa = np.mean(dataframe["GRASA"])

    ###### FIN COMPLETAR ######

    ######  2) Contar la cantidad sopas del tipo "CC" ######
    # COMPLETAR
    cant_tipo_cc = len(dataframe.query("TIPO == 'CC'"))

    ###### FIN COMPLETAR ######

    ######  3) Encontrar la sopa con más sodio (y el valor) ######

    # COMPLETAR

    # Implementacion 1
    max_sodio_indice = dataframe["SODIO"].idxmax()
    max_sodio = dataframe["SODIO"][max_sodio_indice]

    # También se puede calcular el maximo con: dataframe["SODIO"].max()

    ###### FIN COMPLETAR ######

    return promedio_grasa, cant_tipo_cc, max_sodio, max_sodio_indice


dataframe = pd.read_excel('Sopas.xls')

filas, columnas = dataframe.shape
print(
    f"El conjunto de datos tiene:\n\t {filas} filas o ejemplos\n\t {columnas} columnas o atributos")
print("Las columnas son: ", list(dataframe.columns))
print("\n")


promedio_grasa, cant_tipo_cc, max_sodio, max_sodio_indice = calcular(dataframe)
print("=== Resultado de los cálculos: ===")
verificar_resultado(2.4, promedio_grasa, "promedio_grasa")
verificar_resultado(15, cant_tipo_cc, "cant_tipo_cc")
verificar_resultado(970, max_sodio, "max_sodio")
verificar_resultado(6, max_sodio_indice, "max_sodio_indice")
