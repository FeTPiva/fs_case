#This file objective serves only to emulate streaming of proposed data
#run it only after api, redis etc is up

import os
import gzip
import requests
import time
import json
from io import BytesIO
import logging
from typing import Optional
import csv

class stream_data():
    def __init__(self):
        pass

    def stream_json(self, file_url: str, id:str, url:str, delay=0.005, n=10):
        try:
            response = requests.get(file_url, stream=True)
            response.raise_for_status()

            with gzip.GzipFile(fileobj=response.raw, mode='rb') as gz_file:
                for i, line in enumerate(gz_file):
                    if i >= n:
                        break            

                    try:
                        data = json.loads(line.decode('utf-8'))
                        data_id = data.get(id)
                        print(data_id)
                        if not data_id:
                            print(data)

                        
                        resp = requests.post(
                            url=url,
                            json=data
                        )
                        
                        logging.info(f"[{i+1}] Inserted order:{data_id} (status={resp.status_code})")
                        logging.info(json.dumps(json.loads(resp.text),indent=2))

                        time.sleep(delay)
                    except Exception as e:
                        logging.error(f"Error processing line {i}: {e}")

        except Exception as e:
            logging.error(f"Error downloading or decompressing file: {e}")


    def stream_csv(self,
        file_url: str,
        endpoint_url: str,
        delay: float = 0.005,
        n: int = 10,
        
    ):
        try:
            with requests.get(file_url, stream=True) as response:
                response.raise_for_status()

                with gzip.GzipFile(fileobj=response.raw, mode='rb') as gz_file:
                    decoded_lines = (line.decode('utf-8') for line in gz_file)

                    reader = csv.DictReader(decoded_lines)

                    for i, row in enumerate(reader):
                        if i >= n:
                            break

                        resp = requests.post(endpoint_url, json=row)
                        print(f"[{i+1}] Sent row to {endpoint_url} (status={resp.status_code})")


                        time.sleep(delay)

        except Exception as e:
            print(f"Error: {e}")



#print(requests.get('http://localhost:8000/health').content)
print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#stream_data().stream_json(
#    file_url="https://data-architect-test-source.s3-sa-east-1.amazonaws.com/order.json.gz",
#    id='order_id',
#    delay=0.01,
#    n=10,
#    url='http://localhost:8000/order-event/'
#)
#
#stream_data().stream_json(
#    file_url="https://data-architect-test-source.s3-sa-east-1.amazonaws.com/status.json.gz",
#    id='status_id',
#    delay=0.01,
#    n=10,
#    url='http://localhost:8000/status-event/'
#)

stream_data().stream_csv(
    file_url="https://data-architect-test-source.s3-sa-east-1.amazonaws.com/restaurant.csv.gz",
    endpoint_url="http://localhost:8000/restaurant-event/",
    delay=0.01,
    n=10
)

stream_data().stream_csv(
    file_url="https://data-architect-test-source.s3-sa-east-1.amazonaws.com/consumer.csv.gz",
    endpoint_url="http://localhost:8000/consumer-event/",
    delay=0.01,
    n=10
)


