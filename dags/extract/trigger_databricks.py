import os
import requests
from dotenv import load_dotenv

load_dotenv()


def trigger_databricks_job():

    host = os.getenv("DATABRICKS_HOST").rstrip("/")

    token = os.getenv("DATABRICKS_TOKEN")

    job_id = int(os.getenv("DATABRICKS_JOB_ID"))

    url = f"{host}/api/2.1/jobs/run-now"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    payload = {
        "job_id": job_id
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    print(response.status_code)
    print(response.text)

    response.raise_for_status()

    print("Databricks Job Triggered")


if __name__ == "__main__":
    trigger_databricks_job()