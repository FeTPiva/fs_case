from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import redis
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import logging

#In production would have a file dedicated to etl and another for the dag.
#But since it's just a case and example, I've left it together
def simple_feature():

    r = redis.StrictRedis(host='redis-fs', port=6379, decode_responses=True, db=0)
    logging.info('Redis conected')

    # read all order keys
    keys = r.keys('raw_order*')
    logging.info(f'{keys}')

    data = []
    for key in keys:
        row = r.hgetall(key)
        row['feature_key'] = key
        data.append(row)


    spark = SparkSession.builder.appName("redis_to_parquet").getOrCreate()

    df = (
        spark.createDataFrame(data)
        .withColumn('order_total_amount', col('order_total_amount').cast('double'))
        .groupBy('cpf').avg('order_total_amount')
    )

    df.write.mode("overwrite").parquet("/data/batch_results/simple_feature") 

default_args = {
    'owner': 'you',
    'start_date': datetime(2024, 1, 1),
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='redis_to_parquet',
    schedule_interval="*/10 * * * *", #run every 10 minutes
    default_args=default_args,
    catchup=False
) as dag:
    task = PythonOperator(
        task_id='simple_feature',
        python_callable=simple_feature
    )
