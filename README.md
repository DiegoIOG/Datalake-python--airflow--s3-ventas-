# Datalake-python--airflow--s3-ventas-

This project implements a simple data pipeline that simulates sales data and ingests it into a Data Lake stored in Amazon S3. The pipeline is orchestrated using Apache Airflow and generates JSON files representing sales transactions every minute.

The goal of this project is to demonstrate a basic data engineering workflow where data is generated, processed, and stored in a cloud-based Data Lake.

## Architecture

The pipeline follows this flow:

Python (Sales Generator)
↓
Apache Airflow (Orchestration)
↓
Amazon S3 (Data Lake Storage)

## Data Format

Each generated JSON file represents a sales transaction with the following structure:

{
  "timestamp": "2026-03-06 13:16:29",
  "product_id": 9,
  "amount": 55.34
}

Fields:

timestamp: Date and time of the transaction

product_id: Unique identifier of the product

amount: Sale amount

## Data Generation

Sales data is generated using a Python script that creates random transactions.
A new JSON file is generated every minute to simulate a continuous data stream.

## Data Lake Storage

Generated files are uploaded to an Amazon S3 bucket named:

datalake-1-

Example structure:

s3://datalake-1-/
    raw/
        sales/
            2026/
            03/
            06/
                sale_2026-03-06-13-16.json
## Project Structure
project/
│
├── dags/
│   └── sales_pipeline_dag.py
│
├── src/
│   ├── aws/
│   │   └── s3_client.py
│   │
│   ├── ingestion/
│   │   └── sales_generator.py
│   │
│   └── storage/
│       └── s3_uploader.py
│
├── logs/
├── tests/
├── venv/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## Description:

dags/
Contains Apache Airflow DAGs used to orchestrate the pipeline.

src/
Contains the main source code for data generation and storage.

ingestion/
Responsible for generating simulated sales data.

storage/
Handles uploading data to Amazon S3.

aws/
Contains utilities for connecting to AWS services.

Airflow Pipeline

The pipeline is executed using an Apache Airflow DAG that runs every minute.

## Tasks:

generate_sales_data
Generates random sales data.

upload_to_s3
Uploads the generated JSON file to the S3 Data Lake.

The tasks are executed sequentially in the DAG.

Environment Setup

The project runs locally using a Python virtual environment.

## Create the virtual environment:

python -m venv venv

Activate the environment:

Linux / macOS

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Python version used in this project:

Python 3.13.4

Environment Variables

AWS credentials are stored in a .env file and loaded using python-dotenv.

## Example configuration:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=your_region
BUCKET_NAME=datalake-1-

The .env file is excluded from version control using .gitignore.

Running Airflow

## To start Apache Airflow in standalone mode:

airflow standalone

This command starts:

Airflow scheduler

Airflow webserver

Local metadata database

Once Airflow is running, the DAG can be triggered from the Airflow web interface.

## Target Users

This project is intended for data engineers who want to understand a basic data ingestion pipeline using Python, Apache Airflow, and Amazon S3.

## Purpose

This repository demonstrates a simple but practical example of a data pipeline used in data engineering workflows for ingesting and storing data in a Data Lake.