from DataBase.Models.typesModel import TypesModel

def get_types_name() -> list[str]:
    query = TypesModel().select(TypesModel.name)

    types = []

    for element in query:
        types.append(element.name)

    return types

def getKd(type):
    query = TypesModel().get(TypesModel.name == type)
    return query.Kd