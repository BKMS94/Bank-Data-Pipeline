from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp, lit

def run_bank_etl():
    # 1. Configuración de Spark con Driver para Postgres
    spark = SparkSession.builder \
        .appName("Bank_Data_Pipeline_Final") \
        .config("spark.jars", "/opt/airflow/drivers/postgresql-42.7.1.jar") \
        .getOrCreate()

    input_path = "/opt/airflow/data/bank_transactions.csv"
    
    # 2. EXTRACT: Ingesta con inferencia de esquema
    df = spark.read.csv(input_path, header=True, inferSchema=True)

    # 3. TRANSFORM & QUALITY: 
    # Renombramos y filtramos nulos o montos negativos
    df_clean = df.withColumnRenamed("TransactionAmount (INR)", "amount") \
                 .filter((col("amount") > 0) & (col("amount").isNotNull()))
    
    # 4. LINEAGE: Auditoría de datos 
    df_final = df_clean.withColumn("load_timestamp", current_timestamp()) \
                       .withColumn("source_system", lit("Bank_CSV_Source"))

    # 5. LOAD: Carga Idempotente a Postgres
    db_url = "jdbc:postgresql://postgres:5432/airflow"
    db_properties = {
        "user": "airflow",
        "password": "airflow",
        "driver": "org.postgresql.Driver"
    }

    print("Iniciando carga en Postgres con modo Overwrite...")
    df_final.write.jdbc(url=db_url, table="bank_results", mode="overwrite", properties=db_properties)
    
    print(f"¡Proceso completado! Registros cargados: {df_final.count()}")
    spark.stop()