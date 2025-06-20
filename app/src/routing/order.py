from typing import List, Dict
from fastapi import APIRouter

from src.entity.order import Order
from src.usecase.realtime_fs import RealTimeFS
from src.usecase.ingestion import IngestionSources


router = APIRouter(tags=['Order'])

@router.post("/order-event/")
async def order_event(order: Order):
   IngestionSources().ingest_order(order)
   return {'message': 'Ingestion successfull'}


