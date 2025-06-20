from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import redis
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def extract_and_save_features():
    # connect to Redis
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)

    # read all order keys
    keys = r.keys('raw_order*')
    print(keys)

    data = []
    for key in keys:
        row = r.hgetall(key)
        row['feature_key'] = key
        data.append(row)

    # spark session
    spark = SparkSession.builder \
        .appName("redis_to_parquet") \
        .getOrCreate()

    df = spark.createDataFrame(data).groupBy('cpf').avg('order_total_amount')

    df.write.mode("overwrite").parquet("/data/batch_results/simple_feature")  # saved inside container

default_args = {
    'owner': 'you',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='redis_to_parquet',
    schedule_interval="*/10 * * * *",
    default_args=default_args,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='extract_save_features',
        python_callable=extract_and_save_features
    )
