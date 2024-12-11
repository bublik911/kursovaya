from peewee import BigAutoField, IntegerField, FloatField, ForeignKeyField

from DataBase.config import BaseModel

from DataBase.Models.seModel import seModel


class detModel(BaseModel):
    seid = ForeignKeyField(seModel)
    u = IntegerField()
    t = FloatField()
    fi = FloatField()
    nhe = FloatField()