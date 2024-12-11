from peewee import BigAutoField, IntegerField, FloatField

from DataBase.config import BaseModel


class seModel(BaseModel):
    id = BigAutoField(primary_key=True)
    kd = IntegerField()
    NHo = FloatField()
    sigmahp = IntegerField()
    kfl = FloatField()
    sigmafp = FloatField()
    dw = FloatField(unique=True)