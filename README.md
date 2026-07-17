# 🌦️ Weather Data Engineering Pipeline

An end-to-end Data Engineering project that extracts live weather data from OpenWeatherMap API, stores it in AWS S3, processes it using Databricks (Bronze → Silver → Gold architecture), and orchestrates the complete workflow using Apache Airflow running inside Docker.

---

## 🚀 Project Overview

This project demonstrates a modern cloud-based Data Engineering pipeline.

The pipeline performs the following steps:

1. Extract weather data from OpenWeatherMap API
2. Store raw JSON data in AWS S3 (Bronze Layer)
3. Trigger Databricks Workflow
4. Clean and transform the data (Silver Layer)
5. Aggregate the data (Gold Layer)
6. Schedule everything automatically using Apache Airflow
7. Deploy the pipeline using Docker on AWS EC2

---

# 🏗️ Architecture

```
                    OpenWeather API
                           │
                           ▼
                  Python Extraction Script
                           │
                           ▼
                  AWS S3 (Bronze Layer)
                           │
                           ▼
                 Apache Airflow Scheduler
                           │
                           ▼
               Databricks Workflow Trigger
                           │
        ┌──────────────────┴─────────────────┐
        ▼                                    ▼
   Silver Layer                        Gold Layer
(Data Cleaning)                  (Aggregated Data)
        │                                    │
        └──────────────────┬─────────────────┘
                           ▼
                     AWS S3 Storage
                           │
                           ▼
                     Future Dashboard
                 (Power BI / Tableau)
```

---

# 🛠️ Tech Stack

- Python
- Apache Airflow
- Docker
- AWS EC2
- AWS S3
- Databricks
- PySpark
- Delta Lake
- OpenWeatherMap API
- Git & GitHub

---

# 📂 Project Structure

```
weather-data/

│
├── config/
│
├── dags/
│   ├── extract/
│   │      Extract_elt.py
│   │      connect_aws.py
│   │      trigger_databricks.py
│   │
│   ├── Databricks/
│   │      silver_layer.ipynb
│   │      gold_layer.ipynb
│   │
│   └── weather_pipeline.py
│
├── data/
│
├── logs/
│
├── docker-compose.yml
│
├── requirements.txt
│
├── .env.example
│
└── README.md
```

---

# ⚙️ Data Pipeline Flow

### Step 1

Extract live weather data from OpenWeatherMap API.

↓

### Step 2

Store raw JSON files into

AWS S3

```
bronze/
```

↓

### Step 3

Apache Airflow schedules the DAG daily.

↓

### Step 4

Airflow uploads data to AWS S3.

↓

### Step 5

Airflow triggers Databricks Workflow.

↓

### Step 6

Databricks Notebook creates

Silver Layer

- Remove null values
- Standardize columns
- Data Cleaning

↓

### Step 7

Gold Layer

- City-wise weather summary
- Average temperature
- Average humidity
- Average pressure
- Wind statistics

↓

### Step 8

Processed data stored back into AWS S3.

---

# 📸 Screenshots

## Airflow DAG

(Add Screenshot)

---

## AWS S3 Bucket

(Add Screenshot)

---

## Databricks Workflow

(Add Screenshot)

---

## Gold Layer Output

(Add Screenshot)

---

# 🔐 Environment Variables

Create a `.env` file.

```
API_KEY=

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION=

S3_BUCKET=

DATABRICKS_HOST=

DATABRICKS_TOKEN=

JOB_ID=
```

---

# ▶️ Run the Project

Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-pipeline-Data-Engineering-project.git
```

Go inside project

```bash
cd weather-pipeline-Data-Engineering-project
```

Create .env

```
Paste your credentials
```

Run Docker

```bash
docker compose up -d
```

Open Airflow

```
http://localhost:8080
```

Run

```
weather_pipeline
```

---

# ☁️ AWS Services Used

- Amazon EC2
- Amazon S3
- IAM

---

# 📊 Databricks

- Workflow Trigger
- PySpark
- Delta Lake
- Silver Layer
- Gold Layer

---

# 📈 Future Improvements

- ML Weather Prediction
- Real-time Streaming
- Kafka Integration
- Snowflake Data Warehouse
- Power BI Dashboard
- Email Notifications
- CI/CD using GitHub Actions

---

# 👨‍💻 Author

**Ashvath M**

B.E Computer Science Engineering

Data Engineering Enthusiast

GitHub:
https://github.com/Ashvath07

LinkedIn:
(Add Your LinkedIn)
