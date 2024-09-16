from typing import List
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class QuartosEnum(str, Enum):
    quartos1 = '1+'
    quartos2 = '2+'
    quartos3 = '3+'
    quartos4 = '4+'

class Imovel(BaseModel):
    email: EmailStr
    preco : PositiveFloat
    metragem: PositiveInt
    quartos: QuartosEnum
    bairro : List[str]