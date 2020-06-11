# -*- coding: utf-8 -*-
"""
Created on Thu May 21 17:33:23 2020

@author: hpiza
"""

from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import ttk
from tkinter import Button
from tkinter import END

class MyLabel(Label):
    def __init__(self, parent1, text1="MyLabel", x1=0, y1=0):
        super().__init__(parent1, text=text1)
        super().place(x=x1, y=y1, width=150, height=25)
        super().config(anchor="e", font=("Consolas", 11), fg="White", bg="#112255")

class MyEntry(Entry):    
    def __init__(self, parent1, x1=0, y1=0):
        super().__init__(parent1)
        super().place(x=x1, y=y1, width=250, height=25)
        super().config(justify="left", font=("Courier new", 11), fg="#336655", bg="#DDFFEE")

class MyApp(Tk):
    
    def __init__(self):
        super().__init__()
        super().title("Mi primer formulario")
        super().geometry("500x250")
        super().configure(background="#FFBBDD")
        super().resizable(False, False)
        self.__initWidgets()
        super().mainloop()
    
    def __initWidgets(self):
        self.lblNombre    = MyLabel(self, "Nombre:",       40,  30)
        self.lblDomicilio = MyLabel(self, "Domicilio:",    40,  70)
        self.lblEdocivil  = MyLabel(self, "Estado civil:", 40, 110)
        
        self.entNombre    = MyEntry(self, 210, 30)
        self.entDomicilio = MyEntry(self, 210, 70)
        
        self.cmbEdocivil  = ttk.Combobox(self, state="readonly", values=["CASADO", "DIVORCIADO", "SOLTERO", "UNIÓN LIBRE", "VIUDO"])
        self.cmbEdocivil.place(x=210, y=110, width=250, height=25)
        self.cmbEdocivil.config(font=("Courier new", 11))
        self.cmbEdocivil.current(0)
        
        self.btnToUpper   = Button(self, text="A mayúsculas", command=self.textToUpper)
        self.btnToUpper.place(x=210, y=160, width=150, height=30)
        self.btnToUpper.config(font=("Verdana", 10))
        
    
    def textToUpper(self):
        nombre = self.entNombre.get().upper()
        self.entNombre.delete(0, END)
        self.entNombre.insert(0, nombre)
        domicilio = self.entDomicilio.get().upper()
        self.entDomicilio.delete(0, END)
        self.entDomicilio.insert(0, domicilio)
        print(self.cmbEdocivil.get())

MyApp()  # Creando un objeto de tipo MyApp, sin asignarlo a ninguna variable

import os
for i in range(10):
    os.startfile("c:/windows/notepad.exe")


'''
window1 = Tk()
window1.title("Mi primer ventana")
window1.geometry("600x400")
window1.resizable(False, False)
frame1 = Frame(window1, background="yellow")
frame1.place(x = 30, y = 20, width = 200, height = 100)
frame2 = Frame(window1, background="blue")
frame2.place(x = 270, y = 20, width = 100, height = 150)

window1.mainloop()

print("Hola")
window2 = Tk()
window2.title("Mi segunda ventana")
window2.geometry("400x600")
window2.resizable(True, False)
frame3 = Frame(window2, background="#FF0088")
frame3.place(x = 50, y = 50, width = 300, height = 500)
window2.mainloop()
print("Adiós")
'''
