import database.clean_repeat_number as clean_numbers
import pandas as pd
import os
import json

csvFiles = [
        './database/SMS1.csv',
        './database/SMS2.csv',
        './database/SMS3.csv',
        './database/SMS4.csv',
        './database/SMS5.csv',
        './database/SMS6.csv',
        './database/SMS7.csv',
        './database/SMS8.csv',
        './database/SMS9.csv'
]

def unif_csv():
    # DataFrame vacío para almacenar los datos combinados
    combined_df = pd.DataFrame()

    # Leer y combinar cada archivo CSV
    for file in csvFiles:
        df = pd.read_csv(file)
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Guardar el DataFrame combinado en un nuevo archivo CSV
    output_file = './database/combined_SMS.csv'
    combined_df.to_csv(output_file, index=False)

def clean():
    # Cargar el archivo CSV
    csv_file = './database/combined_SMS.csv'
    df = pd.read_csv(csv_file)

    # Cargar el archivo JSON
    json_file = './results.json'
    with open(json_file, 'r') as f:
        numbers_to_remove = json.load(f)

    # Extraer los números del JSON
    numbers_to_remove = [entry['number'] for entry in numbers_to_remove]

    # Convertir la columna 'Celular' a string para asegurar coincidencias
    df['Celular'] = df['Celular'].astype(str)

    # Filtrar los números que no están en la lista de números a eliminar
    df_filtered = df[~df['Celular'].isin(numbers_to_remove)]

    # Guardar el DataFrame filtrado en un nuevo archivo CSV
    output_file = './database/filtered_SMS.csv'
    df_filtered.to_csv(output_file, index=False)

    print(f"Números eliminados. El archivo filtrado se ha guardado en {output_file}")

# clean_numbers.main()
clean()