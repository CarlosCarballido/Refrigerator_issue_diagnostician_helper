# Script para preprocesar los datos

import pandas as pd

def load_data(file_path):
    """
    Carga el archivo CSV de errores y síntomas de la nevera.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"El archivo {file_path} no fue encontrado.")
        return None

def get_error_frequencies(df):
    """
    Obtiene las frecuencias de errores desde el CSV.
    """
    return df['Error Frequency'].values

def diagnose_issue(symptom, df):
    """
    Busca posibles problemas basados en los síntomas observados.
    """
    # Filtrar los errores que coincidan con el síntoma dado
    matches = df[df['Symptoms'].str.contains(symptom, case=False)]
    return matches[['Error Code', 'Error Description', 'Possible Causes', 'Solutions']]
