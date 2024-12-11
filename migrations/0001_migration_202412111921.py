# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class seModel(peewee.Model):
    id = BigAutoField(primary_key=True)
    kd = IntegerField()
    NHo = FloatField()
    sigmahp = IntegerField()
    kfl = FloatField()
    sigmafp = FloatField()
    dw = FloatField(unique=True)
    class Meta:
        table_name = "semodel"


@snapshot.append
class detModel(peewee.Model):
    id = BigAutoField(primary_key=True)
    seid = snapshot.ForeignKeyField(index=True, model='semodel')
    u = IntegerField()
    t = FloatField()
    fi = FloatField()
    nhe = FloatField()
    class Meta:
        table_name = "detmodel"


@snapshot.append
class MaterialsModel(peewee.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    NHo = FloatField()
    Sigma = IntegerField()
    class Meta:
        table_name = "materialsmodel"


@snapshot.append
class TypesModel(peewee.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=100, unique=True)
    Kd = IntegerField()
    class Meta:
        table_name = "typesmodel"


