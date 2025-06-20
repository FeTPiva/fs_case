from typing import List, Dict
from fastapi import APIRouter

from src.entity.consumer import Consumer
from src.usecase.ingestion import IngestionSources


router = APIRouter(tags=['Consumer'])

@router.post("/consumer-event/")
async def consumer_event(consumer: Consumer):
   IngestionSources().ingest_consumer(consumer)
   return {'message': 'Ingestion successfull'}


