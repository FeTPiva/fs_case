from fastapi import FastAPI

from src.routing.order import router as order_router
from src.routing.restaurant import router as restaurant_router
from src.routing.redis_debug import router as redis_router
from src.routing.features import router as features_router
from src.routing.consumer import router as consumer_router
from src.routing.status import router as status_router



fast_app = FastAPI(title="Simple Feature Store")

@fast_app.get("/health", tags=["Health Check"])
async def root():    
    return {"message": "API Live!"}

fast_app.include_router(features_router)

fast_app.include_router(restaurant_router)
fast_app.include_router(order_router)
fast_app.include_router(consumer_router)
fast_app.include_router(status_router)

#temp
#fast_app.include_router(redis_router)






