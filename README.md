# 🏦 Bank Transactions ETL Pipeline (PySpark + Airflow)

Este proyecto implementa un pipeline de datos robusto para la ingesta, transformación y disponibilidad de transacciones financieras. Está diseñado bajo principios de **idempotencia**, **resiliencia** y **calidad de datos**, simulando un entorno de banca comercial regulado.



## 🏗️ Arquitectura del Proyecto
El proyecto utiliza una estructura modular para separar la orquestación de la lógica de negocio, facilitando el mantenimiento y la escalabilidad:

* **`dags/`**: Contiene el orquestador `bank_pipeline_dag.py` que gestiona la ejecución y reintentos del flujo.
* **`src/`**: Núcleo técnico del proyecto con `etl_process.py` para la lógica ETL y `utils.py` para configuraciones transversales.
* **`data/`**: Zona de aterrizaje (Landing Zone) para los archivos fuente `bank_transactions.csv`.
* **`drivers/`**: Almacena el conector JDBC necesario para la persistencia en base de datos.

## 🛠️ Stack Tecnológico
* **Orquestación**: Apache Airflow 2.7.1.
* **Procesamiento**: PySpark 3.5.0 (Computación distribuida).
* **Contenerización**: Docker & Docker Compose.
* **Base de Datos**: PostgreSQL 13 (Data Mart analítico).
* **Lenguaje**: Python 3.9.

## 🚀 Características Principales (Valor Técnico)
1.  **Idempotencia**: Implementación de carga en modo `overwrite` y eliminación de duplicados mediante `TransactionId` para garantizar que ejecuciones repetidas no corrompan el destino.
2.  **Calidad de Datos (Data Quality)**: Filtros de validación para montos negativos y tratamiento de valores nulos antes de la persistencia.
3.  **Trazabilidad y Linaje**: Inserción de metadatos de auditoría
