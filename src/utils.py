import pyspark.sql.functions as F

def clean_data(df):
    """Estandarización y Calidad de Datos"""
    # Limpiar nombres de columnas 
    for col in df.columns:
        clean_name = col.lower().replace(" ", "_").replace("(", "").replace(")", "")
        df = df.withColumnRenamed(col, clean_name)
    
    # Filtro de negocio: Solo montos positivos
    df = df.filter(F.col("transactionamount_inr") > 0)
    
    # Manejo de nulos básicos
    df = df.fillna({"custlocation": "UNKNOWN", "custgender": "U"})
    
    return df

def clean_column_names(df):
    """Estandariza los nombres de las columnas a minúsculas y sin espacios."""
    for col in df.columns:
        df = df.withColumnRenamed(col, col.lower().replace(" ", "_").replace("(", "").replace(")", ""))
    return df

def validate_financial_data(df):
    """Aplica reglas de Data Quality para el sector bancario."""
    # 1. Eliminar transacciones con montos negativos o cero
    df = df.filter(F.col("transactionamount_inr") > 0)
    
    # 2. Manejo de nulos en ubicación
    df = df.fillna({"custlocation": "NOT_SPECIFIED", "custgender": "U"})
    
    return df