from tkinter import *
from tkinter import ttk

import peewee

from DataBase.Repositories.materialsRepository import get_materials_name, get_NHo, get_Sigma
from DataBase.Repositories.seRepository import create_se
from DataBase.Repositories.detRepository import create_det
from DataBase.Repositories.typesRepository import get_types_name, getKd
from DataBase.Models.seModel import seModel

def CalculateKd(type):
  return getKd(type)

def CalculateNHo(material):
  return get_NHo(material)

def CalculateSigma(material):
  return get_Sigma(material)

def CalculateNHE(t, n):
  return 60 * t * n

def CalculateKnl(t, n, material):
  return (CalculateNHo(material)/CalculateNHE(t, n))**0.1666666666

def CalculateSigmaNPInMPa(t, n, material):
  return CalculateSigma(material) * CalculateKnl(t, n, material)

def Calculate(t, n, material, type, u, fi, t_1):
  kd = CalculateKd(type)
  sigma =  CalculateSigmaNPInMPa(t, n, material)
  dw = kd * (t_1/ (u * fi * sigma**2))** 0.33333333333
  try:
    se = create_se(kd, CalculateNHo(material), CalculateSigma(material), CalculateKnl(t, n, material), CalculateSigmaNPInMPa(t, n, material), dw)
  except peewee.IntegrityError:
    se = seModel.get(seModel.dw == round(dw, 2))
  create_det(se, u, t, fi, CalculateNHE(t, n))
  return dw




def calculate_button_click():
  tch = int(tchBox.get())
  n = int(nBox.get())
  u = float(uBox.get())
  fi = float(fiBox.get())
  t_1 = float(t_1Box.get())
  material = combobox1.get()
  type = combobox2.get()
  ansD.set(Calculate(tch, n, material, type, u, fi, t_1))

if __name__ == '__main__':
  root = Tk()
  root.title('Kurlenko IDB-22-02')
  root.geometry('600x600')

  #Заголовок
  lbl1 = Label(root, text='Проектировочный расчет циллиндрической передачи', font=('Arial', 16))
  lbl1.place(x=30,y=5)

  #Выберите материал
  lb2 = Label(root, text="Выберите материал", font=('Arial', 10))
  lb2.place(x=30,y=40)
  materials = get_materials_name()
  combobox1 = ttk.Combobox(root, values=materials)
  combobox1.place(x=30,y=60)

  #Введите вид колес
  lb3 = Label(root, text="Выберите вид колес", font=('Arial', 10))
  lb3.place(x=30,y=80)
  types = get_types_name()
  combobox2 = ttk.Combobox(root, values=types)
  combobox2.place(x=30,y=100)

  #Введите крутящий момент на шестерне
  t_1Box = StringVar()
  lb4 = Label(root, text="Введите крутящий момент на шестерне", font=('Arial', 10))
  lb4.place(x=30,y=130)
  e1 = Entry(root, textvariable=t_1Box)
  e1.place(x=30,y=150)

  #Введите φbd от 0,2 до 1,2
  fiBox = StringVar()
  lb5 = Label(root, text="Введите φbd от 0,2 до 1,2", font=('Arial', 10))
  lb5.place(x=30,y=180)
  e2 = Entry(root, textvariable=fiBox)
  e2.place(x=30,y=200)

  #Введите число n
  nBox = StringVar()
  lb6 = Label(root, text="Введите число n", font=('Arial', 10))
  lb6.place(x=30,y=230)
  e3 = Entry(root, textvariable=nBox)
  e3.place(x=30,y=250)

  #Введите число tch
  tchBox = StringVar()
  lb7 = Label(root, text="Введите число tch", font=('Arial', 10))
  lb7.place(x=30,y=290)
  e4 = Entry(root, textvariable=tchBox)
  e4.place(x=30,y=310)

  #Введите число u
  uBox = StringVar()
  lb8 = Label(root, text="Введите число u", font=('Arial', 10))
  lb8.place(x=30,y=360)
  e5 = Entry(root, textvariable=uBox)
  e5.place(x=30,y=390)

  #вывод
  ansD = StringVar()
  lb8 = Label(root, text="Диаметр шестерни", font=('Arial', 10))
  lb8.place(x=280,y=40)
  e5 = Entry(root, textvariable=ansD)
  #ansD.set()
  e5.place(x=280, y=60)

  #Рассчитать
  count = Button(text="Рассчитать", width=10, height=2, command=calculate_button_click)
  count.place(x=30,y=450)

  root.mainloop()