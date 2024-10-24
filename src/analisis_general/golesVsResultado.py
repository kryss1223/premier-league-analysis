import pandas as pd

#Carga el dataset desde la carpeta 'data'
data_path = 'data\pl_2018_2019.csv'
df = pd.read_csv(data_path)

#Muestra las primeras filas del dataset para comprobar que se ha cargado bien
print(df.groupby('HTR')['FTR'].value_counts(normalize=True))


#Analisis exaustivo de probabilidad de ganar segun el resultado del primer tiempo

# Caso 1: Marcan en el primer tiempo y ganan
marca_y_gana = df[(df['HTHG'] > 0) & (df['FTR'] == 'H')]

# Caso 2: No marcan en el primer tiempo y no ganan (pierden o empatan)
no_marca_no_gana = df[(df['HTHG'] == 0) & (df['FTR'] != 'H')]

# Caso 3: No marcan en el primer tiempo y empatan
no_marca_empata = df[(df['HTHG'] == 0) & (df['FTR'] == 'D')]

# Total de partidos
total_partidos = len(df)

# Calcular los porcentajes
prob_marca_y_gana = len(marca_y_gana) / total_partidos * 100
prob_no_marca_no_gana = len(no_marca_no_gana) / total_partidos * 100
prob_no_marca_empata = len(no_marca_empata) / total_partidos * 100

# Mostrar resultados
print(f"Probabilidad de marcar en el 1er tiempo y ganar: {prob_marca_y_gana:.2f}%")
print(f"Probabilidad de no marcar en el 1er tiempo y no ganar: {prob_no_marca_no_gana:.2f}%")
print(f"Probabilidad de no marcar en el 1er tiempo y empatar: {prob_no_marca_empata:.2f}%")
