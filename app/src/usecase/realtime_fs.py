from src.external.redis_con import RedisCon
from src.entity.restaurant import Restaurant
import logging

class RealTimeFS():
    def __init__(self):
        pass

    def feature_avg_ticket(self, data: Restaurant):
        '''Creating a real time feature from restaurant avg tickets'''

        key = f"rtf_restaurant:{data.id}"
        feature = {'id':data.id, 'avg_ticket':data.average_ticket}

        RedisCon().insert_multivalue_data(key, feature)
        logging.info("data for feature 'restaurant_feature' inserted sucessfuly  ")


    def read_realtime_feature(self, feature, key):
        '''Read a feature stored on the real-time FS'''
        return RedisCon().get_multivalue_data(f'rtf_{feature}:{key}')
    

    def list_real_time_features(self):
        return RedisCon().scan_keys("rtf_*")


    
            







