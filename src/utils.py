import logging
from pyspark.sql import SparkSession

def get_spark_session(app_name="GNB_Banca_Pipeline", jar_path=None):
    """Configura Spark para conectar con Postgres."""
    builder = SparkSession.builder.appName(app_name)
    if jar_path:
        builder = builder.config("spark.jars", jar_path) \
                         .config("spark.driver.extraClassPath", jar_path)
    return builder.getOrCreate()

def setup_logging():
    """Configura logs para trazabilidad (Audit Trail)."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger("ETL_Logger")

def check_data_quality(df, column_name):
    """Perfilamiento rápido para detectar nulos."""
    return df.filter(df[column_name].isNull()).count()