import sys
import os

sys.path.append("/mnt/d/PROYECTOS-DATAENGINNER/airflow-iot-pipeline")

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

from src.ingestion.sensor_reader import read_sensor


def collect_temperature():
    temp = read_sensor()
    print("Temperatura:", temp)


with DAG(
    dag_id="iot_temperature_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="*/5 * * * *",
    catchup=False
) as dag:

    collect_task = PythonOperator(
        task_id="collect_sensor_data",
        python_callable=collect_temperature
    )