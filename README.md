# 🌦️ Weather Data Engineering Pipeline

## 📌 Project Overview

This project is an end-to-end cloud-based Data Engineering Pipeline that automates weather data ingestion, transformation, storage, orchestration, and analytics.

The pipeline extracts live weather data from the OpenWeatherMap API for multiple Indian cities, stores raw data in Amazon S3 (Bronze Layer), transforms it using Apache Spark in Databricks into Silver and Gold layers, stores curated data in Snowflake Data Warehouse, and orchestrates the entire workflow using Apache Airflow running inside Docker on AWS EC2.

---

# 🏗️ Architecture

```
                  OpenWeatherMap API
                           │
                           ▼
                Python Extraction Script
                           │
                           ▼
                 Local Bronze JSON Files
                           │
                           ▼
                   AWS S3 Bronze Layer
                           │
                           ▼
              Databricks (Apache Spark)
                           │
        ┌──────────────────┴─────────────────┐
        ▼                                    ▼
 S3 Silver Layer (Parquet)          Delta Silver Table
        │
        ▼
Gold Aggregation using Spark
        │
        ├──────────────► S3 Gold Layer
        │
        ▼
 Snowflake Data Warehouse
        │
        ▼
 Power BI / Tableau / Machine Learning
```

---

# 🚀 Features

- Live Weather Data Extraction
- Automatic Data Ingestion
- Bronze, Silver and Gold Lakehouse Architecture
- Data Cleaning using Apache Spark
- Delta Lake Tables
- Amazon S3 Storage
- Snowflake Data Warehouse
- Apache Airflow Workflow Automation
- Docker Containerization
- AWS EC2 Deployment
- Ready for Business Intelligence
- Ready for Machine Learning

---

# 🛠️ Tech Stack

### Programming

- Python

### Cloud

- AWS EC2
- AWS S3

### Data Engineering

- Apache Spark
- Databricks
- Delta Lake
- Apache Airflow

### Containerization

- Docker

### Data Warehouse

- Snowflake

### BI

- Power BI
- Tableau

### Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
weather-data/
│
├── dags/
│     ├── extract/
│     ├── upload_to_s3/
│     ├── airflow_dag.py
│
├── data/
│     ├── bronze/
│     ├── silver/
│     └── gold/
│
├── notebooks/
│     ├── Bronze_to_Silver.py
│     ├── Silver_to_Gold.py
│
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Workflow

## Step 1

Extract weather data from OpenWeatherMap API.

↓

## Step 2

Store raw JSON files locally.

↓

## Step 3

Upload JSON files to Amazon S3 Bronze Layer.

↓

## Step 4

Read Bronze JSON using Apache Spark.

↓

## Step 5

Clean and transform the data.

↓

## Step 6

Store transformed data in

- Silver Delta Table
- Silver Parquet (S3)

↓

## Step 7

Aggregate business metrics

- Average Temperature
- Average Humidity
- Maximum Temperature
- Minimum Temperature
- Wind Speed
- Weather Count

↓

## Step 8

Store Gold Layer

- S3 Gold Parquet
- Snowflake Data Warehouse

↓

## Step 9

Visualize using Power BI/Tableau

or

Train Machine Learning Models

---

# 🥉 Bronze Layer

Stores raw JSON files without modification.

Example:

```
weather_20260720_101501.json
```

---

# 🥈 Silver Layer

Cleaned data containing

- City
- Country
- Latitude
- Longitude
- Temperature
- Humidity
- Pressure
- Wind Speed
- Weather
- Description
- Ingestion Date
- Year
- Month
- Day

Stored as

- Delta Table
- Parquet Files

---

# 🥇 Gold Layer

Business-ready aggregated dataset.

Contains

- Average Temperature
- Average Humidity
- Average Pressure
- Average Wind Speed
- Maximum Temperature
- Minimum Temperature
- Total Records

Stored in

- Amazon S3
- Snowflake Data Warehouse

---

# ☁ AWS Services Used

- EC2
- S3
- IAM
- Security Groups

---

# ❄ Snowflake

Warehouse

```
WEATHER_WH
```

Database

```
WEATHER_DB
```

Schema

```
WEATHER_SCHEMA
```

Table

```
WEATHER_DATA
```

---

# 🔄 Airflow Pipeline

```
Extract Data
      │
      ▼
Upload to S3
      │
      ▼
Bronze → Silver
      │
      ▼
Silver → Gold
      │
      ▼
Load to Snowflake




<img width="2510" height="979" alt="image" src="https://github.com/user-attachments/assets/eba65985-86e0-40c2-982d-14ad6b17fe9f" />

```

---

# 📊 Future Scope

- Real-time Streaming using Kafka
- AWS Glue
- AWS Athena
- Machine Learning Prediction
- Weather Forecast Dashboard
- CI/CD using GitHub Actions
- Kubernetes Deployment

---

# 📈 Skills Demonstrated

- Data Engineering
- ETL Pipeline
- ELT Pipeline
- Apache Spark
- Data Lake
- Delta Lake
- Data Warehouse
- Snowflake
- Airflow
- Docker
- AWS
- Python
- Cloud Computing

---

# 👨‍💻 Author

**Ashvath M**

Final Year B.E Computer Science Engineering

Email: ashavth011@gmail.com

LinkedIn:
(https://www.linkedin.com/in/ashvath-m/)
GitHub:
https://github.com/Ashvath07/

---

# ⭐ If you found this project useful, don't forget to follow me .
