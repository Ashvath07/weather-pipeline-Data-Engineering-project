from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from extract.Extract_elt import Extract_elt
from extract.connect_aws import AWSUploader
from extract.trigger_databricks import trigger_databricks_job

weather = Extract_elt()
aws = AWSUploader()

default_args = {
    "owner": "Ashvath",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}

with DAG(
    dag_id="weather_pipeline",
    default_args=default_args,
    description="Weather Pipeline",
    start_date=datetime(2026, 7, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    extract_task = PythonOperator(
        task_id="extract_weather_data",
        python_callable=weather.extract_weather,
    )

    upload_task = PythonOperator(
        task_id="upload_to_s3",
        python_callable=aws.connect_aws,
    )

    databricks_task = PythonOperator(
        task_id="trigger_databricks",
        python_callable=trigger_databricks_job,
    )

    extract_task >> upload_task >> databricks_task