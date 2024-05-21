import numpy as np
import csv
from Cabaña import cabaña
from GestorReservas import GestorReservas
class GestorCabañas:
    __arreglocab: np.array
    __cant: int
    def __init__(self):
        self.__arreglocab=np.empty(10, dtype=cabaña)
        self.__cant=0
    def agregarcabaña(self, cab):
        self.__arreglocab[self.__cant]=cab
        self.__cant+=1
    def carga(self):
        archivo=open(r'C:\Users\vzava\OneDrive\Escritorio\python\PRACTICA\Cabañas.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.agregarcabaña(cabaña(int(fila[0]),int(fila[1]),int(fila[2]),int(fila[3]),float(fila[4])))
        archivo.close()
    def busq(self, huesp, gestorR):
        i=0
        band=False
        while i<len(self.__arreglocab):
            if self.__arreglocab[i]>=huesp and not(gestorR.cheqres(self.__arreglocab[i].getnum())):
                    print("num de cabaña sin reservas y capacidad igual o superior a ", huesp, ": ", self.__arreglocab[i].getnum())
            i= i+1
        return
    def busqimp(self, num):
        i=0
        while i<len(self.__arreglocab):
            if self.__arreglocab[i].getnum()==num:
                return self.__arreglocab[i].getimp()
            i+=1

        