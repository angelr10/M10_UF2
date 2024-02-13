from __future__ import annotations
from abc import ABC, abstractmethod

# AbstractFactory
class UtiensilioEscritura(ABC):
    @abstractmethod
    def creaLapiz(self) -> AbstractLapiz:
        pass
    
    @abstractmethod
    def creaBoli(self) -> AbstractBoli:
        pass
    
    @abstractmethod
    def creaRotulador(self) -> AbstractRotulador:
        pass

# ConcreteFactoryA
class Bic(UtiensilioEscritura):
    def creaLapizBic(self):
        return ConcreteProductA1()
    
    def creaBoliBic(self):
        return ConcreteProductB1()
    
#ConcreteFactoryB
class Pilot(UtiensilioEscritura):
    def creaLapizBic(self):
        return ConcreteProductA2()
    
    def creaBoliBic(self):
        return ConcreteProductB2()




# AbstractProductA
class AbstractLapiz:
    def operacion_a(self):
        pass

# AbstractProductB
class AbstractBoli:
    def operacion_b(self):
        pass

# ConcreteProductA1
class ConcreteProductA1(AbstractProductA):
    def operacion_a(self):
        print("Operación A del producto A1")

# ConcreteProductA2
class ConcreteProductA2(AbstractProductA):
    def operacion_a(self):
        print("Operación A del producto A2")

class ConcreteProductB1(AbstractProductB):
    def operacion_b(self):
        print("Operación B del producto B1")

class ConcreteProductB2(AbstractProductB):
    def operacion_b(self):
        print("Operación B del producto B2")

# Definimos el código del cliente que usa la interfaz abstracta
def client_code(factory):
    producto_a = factory.crear_producto_a()
    producto_b = factory.crear_producto_b()
    producto_a.operacion_a()
    producto_b.operacion_b()

# Creamos dos objetos de tipo ConcreteFactory y los pasamos al código del cliente
factory1 = ConcreteFactory1()
factory2 = ConcreteFactory2()
client_code(factory1)
client_code(factory2)
