import redis
import os

class RedisCon():
    def __init__(self):
        self.redis_host = os.getenv("REDIS_HOST", "localhost")
        self.redis_port = int(os.getenv("REDIS_PORT", 6379))

        self.r = redis.StrictRedis( self.redis_host, self.redis_port, decode_responses=True, db=0)
   
    def insert_data(self, key, value):
        self.r.set(key, value)

    def get_data(self, key):
        return self.r.get(key)
    
    def insert_multivalue_data(self, key, value):
        self.r.hset(key, mapping=value)

    def get_multivalue_data(self, key):
        return self.r.hgetall(key.replace('%',':'))
    
    def ingest_raw_data(self, keys, value):
        self.r.hset(f'raw_{keys}', mapping=value)

    def scan_keys(self, pattern):
        cursor = 0
        all_keys = []
        while True:
            cursor, keys = self.r.scan(cursor=cursor, match=pattern, count=1000)
            all_keys.extend(keys)
            if cursor == 0:
                break
        return all_keys

        




