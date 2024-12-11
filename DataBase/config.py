from peewee import *

db = MySQLDatabase('kursovaya',
                   user='user',
                   password='Users!',
                   charset='utf8mb4')

class BaseModel(Model):
    class Meta:
        database = db
