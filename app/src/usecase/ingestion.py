from src.external.redis_con import RedisCon
import logging
from src.entity.restaurant import Restaurant
from src.entity.consumer import Consumer
from src.entity.order import Order
from src.entity.status import Status
from typing import Union

class IngestionSources():
    '''
    Class responsible for the ingestion of multiple sources without complex data transformation
    '''
    def __init__(self):
        pass
    
    @staticmethod
    def ingest_raw_data(
        data: Union[Restaurant, Status, Consumer, Order],
        datasource_name:str,
        data_source_id:str
        ):

        '''generic function to ingest data on redis'''

        try:
            RedisCon().insert_multivalue_data(f'raw_{datasource_name}:{data_source_id}', value=data.model_dump())

        except Exception as e:
            logging.error(f'error ingesting {datasource_name}. Details: \n {e}')
            raise e
           

    def ingest_restaurant(self, restaurant: Restaurant):
        '''Ingests restaurant data from a emulated stream into redis'''
        self.ingest_raw_data(restaurant, 'restaurant', restaurant.id )
   
    
    def ingest_status(self, status: Status):
        '''Ingests status data from a emulated stream into redis'''
        self.ingest_raw_data(status, 'status', status.status_id)


    def ingest_order(self, order: Order):
        '''Ingests order data from a emulated stream into redis'''
        order.items = str(order.items)
        order.order_scheduled = str(order.order_scheduled)
        order.order_scheduled_date = str(order.order_scheduled_date)
        self.ingest_raw_data(order, 'order', order.order_id)


    def ingest_consumer(self, consumer: Consumer):
        '''Ingests order data from a emulated stream into redis'''
        self.ingest_raw_data(consumer, 'consumer', consumer.customer_id)
