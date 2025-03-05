import pandas as pd
from tqdm import tqdm

# Cargar el archivo (modifica la ruta y el nombre del archivo según sea necesario)
file_path = "DATASET LETRAS.xlsx"  # Cambia a .csv si es necesario
df = pd.read_excel(file_path)  # Usa pd.read_csv(file_path) si el archivo es CSV

# Inicializar tqdm para la barra de progreso
tqdm.pandas(desc="Filtrando datos")

# Filtrar solo las filas donde la columna 'language' tenga el valor 'es'
df_filtered = df[df['language'].progress_apply(lambda x: x == 'es')]

# Guardar el resultado en un nuevo archivo con barra de progreso
output_path = "archivo_filtrado.xlsx"  # Cambia a .csv si es necesario

with tqdm(total=len(df_filtered), desc="Guardando archivo") as pbar:
    df_filtered.to_excel(output_path, index=False)
    pbar.update(len(df_filtered))

print(f"Archivo guardado como {output_path}")