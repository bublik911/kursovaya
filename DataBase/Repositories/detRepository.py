from DataBase.Models.detModel import detModel

def create_det(seid, u, t, fi, nhe):
    detModel().create(seid=seid, u=u, t=t, fi=fi, nhe=nhe)