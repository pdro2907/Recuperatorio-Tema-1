class cabaña:
    __numero: int
    __cantidadhabitaciones: int
    __camasgrandes: int
    __camaschicas: int
    __importe: float
    def __init__(self, num, cant,camgrandes,camchicas,imp):
        self.__numero=num
        self.__cantidadhabitaciones=cant
        self.__camasgrandes=camgrandes
        self.__camaschicas=camchicas
        self.__importe=imp
    def __ge__(self, huesp):
        tam=self.__camasgrandes*2+self.__camaschicas
        return tam>=huesp
    def getnum(self):
        return self.__numero
    def getimp(self):
        return self.__importe
