import abc

#IVEHICULO
class IVehicle(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(cls, subclass):
        return (                hasattr(subclass, 'arrencar') and 
                callable(subclass.arrencar) and
                hasattr(subclass, 'aturarse') and 
                callable(subclass.aturarse) and 
                hasattr(subclass, 'accelerar') and 
                callable(subclass.accelerar) and  
                hasattr(subclass, 'frenar') and 
                callable(subclass.frenar) or 
                NotImplemented)

    @abc.abstractmethod
    def arrencar(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod    
    def aturarse(self) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def accelerar(self, speed: int) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    def frenar(self, speed: int) -> str:
        raise NotImplementedError

#Coche
class Cotxe(IVehicle):
    def arrencar(self) -> str:
        return "Arrenco en primera"

    def aturarse(self) -> str:
        return "Aturo en punt mort i amb el fre de mà posat"

    def accelerar(self, speed: int) -> str:
        return "Accelero fins a " + str(speed) + " Km/h"

    def frenar(self, speed: int) -> str:
        return "Redueixo la velocitat en " + str(speed) + " Km/h"


#Patinete
class Patinet(IVehicle):

    def arrencar(self) -> str:
        return "Arrenco amb el manillar"

    def aturarse(self) -> str:
        return "Aturo amb el manillar i posant un peu a terra"

    def accelerar(self, speed: int) -> str:
        return "Accelero fins a " + str(speed) + " Km/h"

    def frenar(self, speed: int) -> str:
        return "Com a patinet no m'aturo al semafor i no reduiré la velocitat en " + str(speed) + " Km/h"


#MAIN
def main():
    bmw = Cotxe()
    print(bmw.arrencar())
    print(bmw.accelerar(120))
    print(bmw.frenar(120))
    print(bmw.aturarse())

    bongo = Patinet()
    print(bongo.arrencar())
    print(bongo.accelerar(20))
    print(bongo.frenar(20))
    print(bongo.aturarse())

main()