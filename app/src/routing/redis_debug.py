
from fastapi import APIRouter
from typing import List, Dict
from src.external.redis_con import RedisCon


router = APIRouter(tags=['Redis Debug'])

@router.post("/set/{key}/{value}", tags=['Redis Debug'])
def set_value(key: str, value: str):
    RedisCon().insert_data(key, value)
    return {"message": f"Set {key} = {value}"}

@router.get("/get/{key}", tags=['Redis Debug'])
def get_value(key: str):
    value = RedisCon().get_data(key)
    return {"key": key, "value": value}

@router.get("/getValues/{key1}/{key2}", tags=['Redis Debug'])
def get_value2(key1: str, key2:str):
    value = RedisCon().get_multivalue_data(f'{key1}:{key2}')
    return {"key": f'{key1}:{key2}', "value": value}
