from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

#deixando valores default nos fields para facilitar o mock da request. Produtivamente não teria
class Restaurant(BaseModel):
    id:str = Field('d19ff6fca6288939bff073ad0a119d25c0365c407e9e5dd999e7a3e53c6d5d76')
    created_at:str = Field('2017-01-23T12:52:30.910Z')
    enabled:str = Field('false')
    price_range:int = Field(3)
    average_ticket:float = Field(60.0)
    takeout_time:int = Field(0)
    delivery_time:int = Field(50)
    minimum_order_value:float = Field(30.0)
    merchant_zip_code:int = Field(14025)
    merchant_city:str = Field('RIBEIRAO PRETO')
    merchant_state:str = Field('SP')
    merchant_country:str = Field('BR')

