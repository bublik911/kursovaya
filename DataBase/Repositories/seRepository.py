from DataBase.Models.seModel import seModel

def create_se(kd, nho, sihp, kfl, sifp, dw):
    a = seModel().create(kd=kd, NHo=nho, sigmahp=sihp, kfl=kfl, sigmafp=sifp, dw=dw)
    return a