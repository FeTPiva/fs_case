from fastapi import APIRouter
from typing import List, Dict
from fastapi import APIRouter

from src.entity.status import Status
from src.usecase.realtime_fs import RealTimeFS
from src.usecase.ingestion import IngestionSources


router = APIRouter(tags=['Status'])

@router.post("/status-event/")
async def status_event(status: Status):
   IngestionSources().ingest_status(status)
   return {'message': 'Ingestion successfull'}


