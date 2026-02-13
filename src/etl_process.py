from pyspark.sql.functions import col, current_timestamp, lit
from src.utils import get_spark_session, setup_logging, check_data_quality

logger = setup_logging()

def run_bank_etl():
    # Usamos el path del driver que genera el docker-compose
    jar_path = "/opt/airflow/drivers/postgresql-42.7.1.jar"
    spark = get_spark_session(app_name="GNB_Banca_Pipeline", jar_path=jar_path)
    
    try:
        logger.info("Iniciando Extracción...")
        df = spark.read.csv("/opt/airflow/data/bank_transactions.csv", header=True, inferSchema=True)

        # Calidad e Idempotencia
        df_final = df.withColumnRenamed("TransactionAmount (INR)", "amount") \
                     .filter((col("amount") > 0) & (col("amount").isNotNull())) \
                     .dropDuplicates(["TransactionId"]) \
                     .withColumn("load_timestamp", current_timestamp())

        db_url = "jdbc:postgresql://postgres:5432/airflow"
        db_properties = {"user": "airflow", "password": "airflow", "driver": "org.postgresql.Driver"}

        df_final.write.jdbc(url=db_url, table="bank_results", mode="overwrite", properties=db_properties)
        logger.info("Carga exitosa en Postgres.")

    finally:
        spark.stop()