from pyspark.sql import *
import redis
from pyspark.sql import SparkSession

def extract_and_save_features():
    # connect to Redis
    r = redis.Redis(host='redis', port=6379, decode_responses=True)

    # read all order keys
    keys = r.keys('raw_order*')

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

