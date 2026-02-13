# 🏦 Bank Data Pipeline: Scalable ETL with PySpark & Airflow

## 📌 Descripción del Proyecto
Este proyecto es una solución **End-to-End (E2E)** de Ingeniería de Datos diseñada para procesar y analizar más de **1 millón de transacciones bancarias**. El objetivo es transformar datos financieros crudos en activos estratégicos, garantizando la **idempotencia**, la integridad de la información y el cumplimiento de estándares de calidad exigidos en el sector bancario.

Se implementó una arquitectura distribuida que separa la orquestación del procesamiento masivo, simulando un entorno de producción real utilizando contenedores.

---

## 🛠️ Stack Tecnológico
* **Orquestación:** **Apache Airflow** (Gestión y monitoreo de flujos de trabajo).
* **Procesamiento Big Data:** **Apache Spark (PySpark)** (Motor de procesamiento distribuido para grandes volúmenes).
* **Contenerización:** **Docker & Docker Compose** (Aislamiento de servicios y entorno replicable).
* **Almacenamiento:** **Parquet (Snappy compression)** (Optimización de almacenamiento y velocidad de consulta).
* **Lenguaje y Librerías:** **Python** (Pandas, NumPy, PySpark SQL).
* **Base de Datos de Metadatos:** **PostgreSQL** (Persistencia del historial de ejecución de Airflow).

---

## 🚀 Arquitectura del Pipeline
El flujo de datos se divide en cuatro etapas críticas gestionadas por un DAG (Directed Acyclic Graph) en Airflow:

1. **Ingesta Automatizada:** Carga masiva de archivos CSV desde el Data Lake local hacia el entorno distribuido.
2. **Validación & Data Quality:**
    * Filtrado de anomalías como montos negativos o transacciones incoherentes.
    * Manejo de valores nulos y estandarización de esquemas técnicos.
3. **Procesamiento Distribuido:**
    * Cálculo de balances promedio por ubicación geográfica mediante Spark SQL.
    * Segmentación de clientes basada en comportamiento transaccional masivo.
4. **Carga Optimizada:** Exportación de resultados a archivos Parquet particionados, mejorando el rendimiento de futuras consultas analíticas.

---

## 📂 Estructura del Repositorio

Bank-Data-Pipeline/
├── dags/                   # Definición de flujos y tareas en Airflow
├── src/                    # Scripts de procesamiento PySpark y utilitarios
│   ├── etl_process.py      # Lógica principal de transformación
│   └── utils.py            # Funciones de validación de calidad y limpieza
├── data/                   # Data Lake local (Raw y Processed)
├── docker-compose.yml      # Configuración de servicios (Airflow, Spark, Postgres)
└── README.md               # Documentación del proyecto