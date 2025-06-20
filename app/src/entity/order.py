from pydantic import BaseModel, Field
from typing import List, Optional, Any
from datetime import datetime

#deixando valores default nos fields para facilitar o mock da request. Produtivamente não teria
class Order(BaseModel):
    cpf:int = Field(80532101763)
    customer_id:str = Field('7ba88a68bb2a3504c6bd37a707af57a0b8d6e110a551c719c9e7f71aaf3a99cf')
    customer_name:str = Field('GUSTAVO')
    delivery_address_city:str = Field('FRANCA')
    delivery_address_country:str= Field('BR')
    delivery_address_district:str = Field('JARDIM ESPRAIADO')
    delivery_address_external_id:int = Field(6736655)
    delivery_address_latitude:float = Field(-47.39)
    delivery_address_longitude:float = Field(-20.55)
    delivery_address_state:str= Field('SP')
    delivery_address_zip_code:int= Field(14403)
    items:Any = Field([{"name": "Parmegiana de Filé de Frango (2 pessoas)"}])
    merchant_id:str= Field('a992a079a651e699d9149423761df2427c0e3af0a2a1b5bb6d2bad1cb3a3a265')
    merchant_latitude:float= Field(-47.39)
    merchant_longitude:float= Field(-20.55)
    merchant_timezone:str= Field('America/Sao_Paulo')
    order_created_at:str= Field('2019-01-17T22:50:06.000Z')
    order_id:str= Field('33e0612d62e5eb42aba15b58413137e441fbe906de2febd6a6c721b0e5773b44')
    order_scheduled:Optional[bool] = Field(False)
    order_scheduled_date:Optional[Any] = None
    order_total_amount:float= Field(46.0)
    origin_platform:str= Field('ANDROID')




