from peewee import TextField, FloatField, IntegerField, CharField, BigAutoField

from DataBase.config import BaseModel



class TypesModel(BaseModel):
    id = BigAutoField(primary_key=True)
    name = CharField(unique=True, max_length=100)
    Kd = IntegerField()
