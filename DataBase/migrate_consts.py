from peewee import IntegrityError, ProgrammingError

from DataBase.Models.typesModel import TypesModel
from misc.consts import *

from DataBase.Models.materialsModel import MaterialsModel

for elem in materials_dict:
    try:
        MaterialsModel().create(name=elem, NHo=materials_dict[elem][0], Sigma=materials_dict[elem][1])
    except ProgrammingError:
        continue
    except IntegrityError:
        continue

for elem in types_dict:
    try:
        TypesModel().create(name=elem, Kd=types_dict[elem])
    except ProgrammingError:
        continue
    except IntegrityError:
        continue