# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:25:50 2020

@author: hpiza
"""

# from Filename import ClassName
from Rectangle import Rectangle

class Box(Rectangle):    
    
    __minDepth = 1
    
    def __init__(self, base=1, height=1, depth=1):  # Método constructor de Box
        super().__init__(base, height)  # Llamada al constructor de Rectangle
        self._depth = Box.__minDepth
        self.setDepth(depth)

    def setDepth(self, depth):
        if not isinstance(depth, (float, int)):
            return
        if depth >= Box.__minDepth:
            self._depth = depth

    def getDepth(self):
        return self._depth

    def volume(self):
        return self._base * self._height * self._depth

    def area(self):
        return 2 * (self._base * self._height + self._depth * self._height + self._base  * self._depth)

    def display(self):
        super().display()   # Llama al método display() de Rectangle
        print("Grosor: {:.1f}".format(self._depth))

# Test class Box
def TestBox():    
    box1 = Box(4, 2, 3)
    box1.setDepth(5)                    # Método setDepth()  creado     en  Box
    print("Depth:", box1.getDepth())
    box1.setDepth(0.5)
    print("Depth:", box1.getDepth())
    box1.setDepth("hola")
    box1.setHeight(3.5)                 # Método setHeight() heredado   de Rectangle
    box1.setBase(5.6)                   # Método setBase()   heredado   de Rectangle
    print("Depth:",  box1.getDepth())   # Método getDepth()  creado     en Box
    print("Base:",   box1.getBase())    # Método getBase()   heredado   de Rectangle
    print("Height:", box1.getHeight())  # Método getHeight() heredado   de Rectangle
    box1.display()                      # Método display()   modificado en Box
    print("Area:",   box1.area())       # Método area()      modificado en Box
    print("Perim:",  box1.perimeter())  # Método perimeter() heredado   de Rectangle
    print(box1)                         # Método __str__()   heredado   de Rectangle
    print("Volumen:", box1.volume())    # Método volume()    creado     en Box

TestBox()
