from dotenv import load_dotenv
import os
import sys

load_dotenv()

# Agregar ruta del proyecto
sys.path.append(os.getenv("SRC"))

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

from src.ingestion.sales_generator import generate_sales
from src.storage.s3_uploader import upload_to_s3
from src.warehouse.snowflake_loader import load_to_snowflake


def generate_sales_data():
    sale = generate_sales()
    return sale


def upload_sales(**context):

    data = context["ti"].xcom_pull(task_ids="generate_sales_data")

    file_name = upload_to_s3(data)

    return file_name


def load_sales_to_snowflake(**context):

    file_name = context["ti"].xcom_pull(task_ids="upload_to_s3")

    load_to_snowflake(file_name)


with DAG(
    dag_id="sales_pipeline",
    start_date=datetime(2024,1,1),
    schedule="*/1 * * * *",
    catchup=False
) as dag:

    generate_task = PythonOperator(
        task_id="generate_sales_data",
        python_callable=generate_sales_data
    )

    upload_task = PythonOperator(
        task_id="upload_to_s3",
        python_callable=upload_sales
    )

    snowflake_task = PythonOperator(
        task_id="load_to_snowflake",
        python_callable=load_sales_to_snowflake
    )

    generate_task >> upload_task >> snowflake_task

