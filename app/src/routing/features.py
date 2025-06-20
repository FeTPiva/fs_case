from fastapi import APIRouter
from typing import List, Dict
from src.usecase.realtime_fs import RealTimeFS

router = APIRouter(tags=['Real-time Features'])


@router.get("/real-time-fs/get/{feature_name}/{key}", tags=['Real-time Features'])
def get_realtime_feature(feature_name:str, key:str ):
    value = RealTimeFS().read_realtime_feature(feature_name, key)
    return {"key": key, "value": value}
    

@router.get("/real-time-fs/list", tags=['Real-time Features'])
def list_realtime_feature():
    return RealTimeFS().list_real_time_features()


