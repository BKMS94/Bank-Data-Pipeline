from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.etl_process import run_bank_etl

default_args = {
    'owner': 'brayan_peña',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 3,                           
    'retry_delay': timedelta(minutes=15),   
}

with DAG(
    'bank_data_pipeline_v1',
    default_args=default_args,
    description='Pipeline ETL de transacciones bancarias con PySpark y Postgres',
    schedule_interval='@daily',
    catchup=False
) as dag:

    ejecutar_etl = PythonOperator(
        task_id='ejecutar_pyspark_etl',
        python_callable=run_bank_etl
    )