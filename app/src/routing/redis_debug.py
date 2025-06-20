
from fastapi import APIRouter
from typing import List, Dict
from src.external.redis_con import RedisCon


router = APIRouter(tags=['Redis Debug'])

@router.get("/getValues/{key1}/{key2}", tags=['Redis Debug'])
def get_value2(key1: str = 'raw_restaurant', key2:str = '631df0985fdbbaf27b9b031a8f381924e3483833385748c8f7e1a41a6891d2b9'):
    value = RedisCon().get_multivalue_data(f'{key1}:{key2}')
    return {"key": f'{key1}:{key2}', "value": value}
