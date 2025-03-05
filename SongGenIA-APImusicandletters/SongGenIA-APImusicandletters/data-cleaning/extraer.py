import pandas as pd
from tqdm import tqdm

# Cargar el archivo Excel
dataset = "archivo_filtrado.xlsx"
df = pd.read_excel(dataset)

# Número total de filas
total_rows = len(df)

# Número de filas por archivo
rows_per_file = total_rows // 3

# Dividir el DataFrame en tres partes
df1 = df.iloc[:rows_per_file]
df2 = df.iloc[rows_per_file:rows_per_file * 2]
df3 = df.iloc[rows_per_file * 2:]

# Guardar los archivos en la carpeta donde se ejecuta el script
files = [("DATASET_LETRAS_PART1.xlsx", df1), 
         ("DATASET_LETRAS_PART2.xlsx", df2), 
         ("DATASET_LETRAS_PART3.xlsx", df3)]

for filename, data in tqdm(files, desc="Guardando archivos", unit="archivo"):
    data.to_excel(filename, index=False)

print("Archivos generados correctamente en la carpeta del script.")