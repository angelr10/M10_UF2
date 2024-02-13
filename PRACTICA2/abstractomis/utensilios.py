import abc

#IVEHICULO
class Iutensilios(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (                hasattr(subclass, 'escribir') and 
                callable(subclass.escribir) and
                hasattr(subclass, 'tachar') and 
                callable(subclass.tachar) and 
                hasattr(subclass, 'garabatear') and 
                callable(subclass.garabatear) and  
                hasattr(subclass, 'dibujar') and 
                callable(subclass.dibujar) and 
                hasattr(subclass, 'rellenar') and 
                callable(subclass.rellenar) or 
                NotImplemented)

    @abc.abstractmethod
    def escribir(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod    
    def tachar(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def garabatear(self, speed: int) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def dibujar(self, speed: int) -> str:
        raise NotImplementedError

#Coche
class lapiz(Iutensilios):
    def escribir(self) -> str:
        return "Has escrito con lapiz"

    def tachar(self) -> str:
        return "Has tachado con lapiz"

    def garabatear(self) -> str:
        return "has garabateado con lapiz"

    def dibujar(self) -> str:
        return "has dibujado con lapiz"
    
    def rellenar(self) -> str:
        return "has rellenado con lapiz"
    

#Patinete
class boli(Iutensilios):

    def escribir(self) -> str:
        return "Has escrito con boli"

    def tachar(self) -> str:
        return "Has tachado con boli"

    def garabatear(self) -> str:
        return "has garabateado con boli"

    def dibujar(self) -> str:
        return "has dibujado con boli"
    
    def rellenar(self) -> str:
        return "has rellenado con boli"


#MAIN
def main():
    bolibic = boli()
    print(bolibic.escribir())
    print(bolibic.tachar())
    print(bolibic.garabatear())
    print(bolibic.dibujar())
    print(bolibic.rellenar())

    lapizbic = lapiz()
    print(lapizbic.escribir())
    print(lapizbic.tachar())
    print(lapizbic.garabatear())
    print(lapizbic.dibujar())
    print(lapizbic.rellenar())

main()