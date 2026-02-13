from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Añadimos /opt/airflow al path para que reconozca la carpeta src
sys.path.append('/opt/airflow')
from src.etl_process import run_bank_etl

default_args = {
    'owner': 'brayan_pena',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'bank_transactions_etl',
    default_args=default_args,
    description='Pipeline de transacciones bancarias GNB',
    schedule_interval=None, # Lo ejecutaremos manualmente
    catchup=False
) as dag:

    task_etl = PythonOperator(
        task_id='run_pyspark_job',
        python_callable=run_bank_etl
    )