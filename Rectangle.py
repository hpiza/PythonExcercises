# -*- coding: utf-8 -*-
"""
Created on Thu May 14 17:52:05 2020

@author: hpiza
"""
class Rectangle:
    
    __rectangleCount = 0
    __minBase   = 1
    __minHeight = 1
    
    def __init__(self, base=1, height=1):       # Método constructor
        # Atributo sin       guión bajo: accesible   desde los objetos, accesible   en las subclases
        # Atributo con un    guión bajo: inaccesible desde los objetos, accesible   en las subclases
        # Atributo con doble guión bajo: inaccesible desde los objetos, inaccesible en las subclases
        self._base   = Rectangle.__minBase
        self._height = Rectangle.__minHeight
        self.setBase(base)
        self.setHeight(height)
        Rectangle.__rectangleCount += 1
        # print("Se crea un rectángulo de ", self._base, "x", self._height)
    
    # getters para leer los atributos
    def getBase(self):
        return self._base

    def getHeight(self):
        return self._height
    
    # setters para modificar los atributos
    def setBase(self, base):
        # Sólo admitimos base si es un float o es un int
        if not isinstance(base, (float, int)):
            return
        if base >= Rectangle.__minBase:
            self._base = base
    
    def setHeight(self, height):
        # Sólo admitimos height si es un float o es un int
        if not isinstance(height, (float, int)):
            return
        if height >= Rectangle.__minHeight:
            self._height = height
    
    def perimeter(self):        # Método de objeto        
        return 2 * (self._base + self._height)

    def area(self):             # Método de objeto
        return self._base * self._height
    
    def display(self):          # Método de objeto
        # Rectángulo de 4.5 x 8.7
        s = "Rectángulo de {:.1f} x {:.1f}".format(self._base, self._height)
        print(s)

    def __str__(self):
        s = "(base={:.1f}, height={:.1f}, area={:.1f}, perimeter={:.1f})".format(
              self._base, self._height, self.area(), self.perimeter())
        # s = str(self._base) + ", " + str(self._height)
        return s

    def count():               # Método de clase
        print("Rectangles created:", Rectangle.__rectangleCount)

# Método de objeto:  objeto.metodo()
# Mëtodo de clase:   Clase.metodo()

def testRectangle():
    rect1 = Rectangle(6)                # Llama al constructor __init__(base=6,   height=1)
    Rectangle.count()
    rect2 = Rectangle(height=7)         # Llama al constructor __init__(base=1,   height=7)
    Rectangle.count()
    rect3 = Rectangle()                 # Llama al constructor __init__(base=1,   height=1)
    Rectangle.count()
    rect4 = Rectangle(5.1, 8.3)         # Llama al constructor __init__(base=5.1, height=8.3)
    Rectangle.count()
    Rectangle.rectangleCount = 15       # no afecta al atributo de clase __rectangleCount
    Rectangle.count()
    
    #print(rect2.__base)      # ERROR: Rectangle no tiene un atributo __base
    #print(rect2.base)        # ERROR: Rectangle no tiene un atributo base
    #print(rect1.height)
    #print(rect1.__height)
    # Las siguientes líneas crean atributos extra, no usados dentro de Rectangle
    rect1.height =  5.467    
    rect2.base   =  8.4     
    rect3.base   = -2.75   
    rect4.height = -9.61
    # De esta manera podemos cambiar base y altura (sólo cambian si son positivos)
    rect1.setHeight(5.467)  # rect1 -->  6.0  x  5.467
    rect2.setBase(8.4)      # rect2 -->  8.4  x  7
    rect3.setBase(-2.75)    # rect3 -->  1.0  x  1.0   (No admitió el cambio)
    rect4.setHeight(-9.61)  # rect4 -->  5.1  x  8.3   (No admitió el cambio)
    rect1.setBase("hola")
    rect1.setHeight(20)
    
    print("Bases:", rect1.getBase(), rect2.getBase(), rect3.getBase(), rect4.getBase())
    print("Alturas:", rect1.getHeight(), rect2.getHeight(), rect3.getHeight(), rect4.getHeight())
    rect1.display()         # self -> rect1
    rect2.display()         # self -> rect2
    rect3.display()         # self -> rect3
    rect4.display()         # self -> rect4
    
    p1 = rect1.perimeter()
    p2 = rect2.perimeter()
    p3 = rect3.perimeter()
    p4 = rect4.perimeter()
    print("Perímetros: {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(p1, p2, p3, p4))
    a1 = rect1.area()
    a2 = rect2.area()
    a3 = rect3.area()
    a4 = rect4.area()
    print("Areas:      {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(a1, a2, a3, a4))
    
    Rectangle.count()
    
    print(rect1)
    print(rect2)
    print(rect3)
    print(rect4)
    
    s = "[" + str(rect1) + "], [" + str(rect2) + "]"
    
    print(s)
    
    '''
    print(type(rect1))
    print(type(rect2))
    '''