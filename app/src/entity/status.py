from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

#deixando valores default nos fields para facilitar o mock da request. Produtivamente não teria
class Status(BaseModel):
    created_at:str = Field('2019-01-25T01:05:07.000Z')
    order_id:str = Field('e210d5d53032677fb82956cc4d99526de1ce9b4ce1c2b3f57accce34f7cfb7f6')
    status_id: str = Field('20c610bbd04145be1fabd9450f80e449b71abe4270be959bd6cdd1f15aff582e')
    value:str = Field('CONCLUDED')

