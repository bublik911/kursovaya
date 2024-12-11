from peewee import TextField, FloatField, IntegerField, CharField, BigAutoField

from DataBase.config import BaseModel



class MaterialsModel(BaseModel):
    id = BigAutoField(primary_key=True)
    name = CharField(unique=True, max_length=100)
    NHo = FloatField()
    Sigma = IntegerField()

