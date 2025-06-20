from fastapi import APIRouter
from typing import List, Dict
from fastapi import APIRouter

from src.entity.restaurant import Restaurant
from src.usecase.realtime_fs import RealTimeFS
from src.usecase.ingestion import IngestionSources


router = APIRouter(tags=['Restaurant'])

@router.post("/restaurant-event/")
async def restaurant_event(restaurant: Restaurant):
   IngestionSources().ingest_restaurant(restaurant)
   RealTimeFS().feature_avg_ticket(restaurant)
   return {'message': 'Ingestion successfull'}


