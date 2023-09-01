import pandas as pd
import numpy as np

# Cargar los datos desde el archivo CSV
data = pd.read_csv("Panamericanos_Lima.csv")

def obtener_sumatoria_columna(columna):
    return data[columna].sum()

def obtener_numero_elementos():
    return len(data)

def obtener_media_columna(columna):
    return data[columna].mean()

def obtener_media_redondeada_columna(columna, decimales=2):
    return round(obtener_media_columna(columna), decimales)

def obtener_mediana_columna(columna):
    return data[columna].median()

def obtener_moda_columna(columna):
    return data[columna].mode()[0]

def obtener_percentiles_columna(columna, percentiles=[25, 50, 80, 85]):
    return np.percentile(data[columna], percentiles)

def obtener_varianza_columna(columna):
    return data[columna].var()

# Ejemplos de uso con las columnas específicas:
print("Sumatoria de la columna 'Oro':", obtener_sumatoria_columna("Oro"))
print("Número de elementos:", obtener_numero_elementos())
print("Media de la columna 'Plata':", obtener_media_columna("Plata"))
print("Media redondeada de la columna 'Plata':", obtener_media_redondeada_columna("Plata"))
print("Mediana de la columna 'Bronce':", obtener_mediana_columna("Bronce"))
print("Moda de la columna 'Total':", obtener_moda_columna("Total"))
print("Percentiles (25, 50, 80, 85) de la columna 'Total':", obtener_percentiles_columna("Total"))
print("Varianza de la columna 'Total':", obtener_varianza_columna("Total"))
