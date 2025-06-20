from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


#deixando valores default nos fields para facilitar o mock da request. Produtivamente não teria
class Consumer(BaseModel):
    customer_id:str = Field('e8cc60860e09c0bb19610b06ced69c973eb83982cfc98e397ce65cba92f70928')
    language:str = Field('pt-br')
    created_at:str = Field('2018-04-05T14:49:18.165Z')
    active:str= Field('true')
    customer_name: str = Field('NUNO')
    customer_phone_area: int = Field(46)
    customer_phone_number: int = Field(816135924)
    