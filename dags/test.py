from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello_world():
    print("Airflow está funcionando correctamente")


with DAG(
    dag_id="test_airflow_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id="hello_task",
        python_callable=hello_world
    )