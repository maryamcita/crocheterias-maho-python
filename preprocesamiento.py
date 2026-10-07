"""
Módulo de Preprocesamiento y Limpieza de Datos — Crocheterias Maho
Contiene funciones reutilizables para carga, manejo de nulos, estandarización de texto
y limpieza específica de precios y valores numéricos.
"""

import pandas as pd


def cargar_datos(filepath: str) -> pd.DataFrame:
    """
    Carga un archivo CSV en un DataFrame de Pandas.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"[OK] Archivo cargado exitosamente desde '{filepath}' ({len(df)} registros)")
        return df
    except Exception as e:
        print(f"[ERROR] Error al cargar el archivo en '{filepath}': {e}")
        raise e


def manejar_nulos(df: pd.DataFrame, estrategia: str = "eliminar", columnas: list = None) -> pd.DataFrame:
    """
    Maneja los valores nulos o vacíos en el DataFrame.
    
    Parámetros:
        df: DataFrame a procesar.
        estrategia: 'eliminar' para borrar filas con nulos, o 'rellenar' para imputar valores por defecto.
        columnas: Lista de columnas específicas a revisar. Si es None, aplica a todo el DataFrame.
    """
    df_clean = df.copy()
    columnas_objetivo = columnas if columnas else df_clean.columns.tolist()

    nulos_iniciales = df_clean[columnas_objetivo].isnull().sum().sum()
    
    if estrategia == "eliminar":
        df_clean = df_clean.dropna(subset=columnas_objetivo)
    elif estrategia == "rellenar":
        for col in columnas_objetivo:
            if df_clean[col].dtype == "object":
                df_clean[col] = df_clean[col].fillna("Sin Registro")
            else:
                df_clean[col] = df_clean[col].fillna(0)

    print(f"[LIMPIEZA] Manejo de nulos ({estrategia}): se procesaron {nulos_iniciales} valores nulos.")
    return df_clean


def estandarizar_texto(df: pd.DataFrame, columnas: list, formato: str = "titulo") -> pd.DataFrame:
    """
    Estandariza columnas de texto removiendo espacios adicionales y ajustando el formato de mayúsculas/minúsculas.
    
    Parámetros:
        df: DataFrame a procesar.
        columnas: Lista de columnas de texto a estandarizar.
        formato: 'minusculas', 'mayusculas', o 'titulo' (Capitalizado).
    """
    df_clean = df.copy()
    
    for col in columnas:
        if col in df_clean.columns:
            serie = df_clean[col].astype(str).str.strip().str.replace(r"\s+", " ", regex=True)
            
            if formato == "minusculas":
                df_clean[col] = serie.str.lower()
            elif formato == "mayusculas":
                df_clean[col] = serie.str.upper()
            elif formato == "titulo":
                df_clean[col] = serie.str.title()
                
    print(f"[TEXTO] Columnas estandarizadas: {columnas} (formato: {formato})")
    return df_clean


def limpiar_moneda(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Limpieza específica de proyecto: remueve el símbolo de moneda ($), elimina puntos de miles,
    espacios en blanco y convierte el valor a numérico float/int.
    """
    df_clean = df.copy()
    
    if columna in df_clean.columns:
        serie_limpia = (
            df_clean[columna]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False)
            .str.strip()
        )
        
        df_clean[columna] = pd.to_numeric(serie_limpia, errors="coerce")
        
    print(f"[MONEDA] Columna '{columna}' convertida a valores numericos limpios.")
    return df_clean
