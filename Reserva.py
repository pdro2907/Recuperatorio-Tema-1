class reserva:
    __numreserva:int
    __nombre:str
    __numcab:int
    __fecha:str
    __canthuespedes: int
    __cantdias:int
    __importe:float
    def __init__(self,numres,nom, numcab,fecha,canth,cantd,imp):
        self.__numreserva=numres
        self.__nombre=nom
        self.__numcab=numcab
        self.__fecha=fecha
        self.__canthuespedes=canth
        self.__cantdias=cantd
        self.__importe=imp
    def getnumcab(self):
        return self.__numcab
    def getfecha(self):
        return self.__fecha
    def getres(self):
        return self.__numreserva
    def getnom(self):
        return self.__nombre
    def gethuesp(self):
        return self.__canthuespedes
    def getcantd(self):
        return self.__cantdias
    def getimps(self):
        return self.__importe