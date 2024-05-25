import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
equipos = [
    'Pumas', 'América', 'Chivas', 'Pumas', 'Chivas',
    'Chivas', 'América', 'Toluca', 'Toluca', 'Pumas',
    'Santos', 'Necaxa', 'América', 'América', 'América',
    'Pumas', 'Santos', 'Pumas', 'Pumas', 'Pumas',
    'América', 'Chivas', 'América', 'Pumas', 'Necaxa',
    'Toluca', 'Chivas', 'América', 'Toluca', 'Pumas'
]

# Crear DataFrame
df = pd.DataFrame({'Equipo': equipos})

# Construir tabla de frecuencia
tabla_frecuencia = df['Equipo'].value_counts().reset_index()
tabla_frecuencia.columns = ['Equipo', 'Frecuencia Absoluta']
tabla_frecuencia['Frecuencia Relativa (%)'] = round((tabla_frecuencia['Frecuencia Absoluta'] / len(df)) * 100, 2)

print("----------------------------------------------------------------------")
print("Tabla de Frecuencia:")
print(tabla_frecuencia)
print("----------------------------------------------------------------------")

# Diagrama de barras
plt.figure(figsize=(10, 6))
plt.bar(tabla_frecuencia['Equipo'], tabla_frecuencia['Frecuencia Absoluta'], color='skyblue', edgecolor='black')
plt.title('Diagrama de Barras')
plt.xlabel('Equipo')
plt.ylabel('Frecuencia Absoluta')
plt.grid(axis='y')
plt.show()

# Gráfica circular
plt.figure(figsize=(8, 8))
plt.pie(tabla_frecuencia['Frecuencia Relativa (%)'], labels=tabla_frecuencia['Equipo'], autopct='%1.1f%%', startangle=90, counterclock=False)
plt.title('Gráfica Circular')
plt.show()
