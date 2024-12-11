from DataBase.Models.materialsModel import MaterialsModel

def get_materials_name() -> list[str]:
    query = MaterialsModel().select(MaterialsModel.name)

    materials = []

    for element in query:
        materials.append(element.name)

    return materials


def get_NHo(material):
    query = MaterialsModel().get(MaterialsModel.name == material)
    return query.NHo


def get_Sigma(material):
    query = MaterialsModel().get(MaterialsModel.name == material)
    return query.Sigma