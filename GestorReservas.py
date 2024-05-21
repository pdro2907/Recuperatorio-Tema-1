from Reserva import reserva
import csv
class GestorReservas:
    __listareservas: list
    def __init__(self):
        self.__listareservas= []
    def agregar(self, res):
        self.__listareservas.append(res)
    def carga(self):
        archivo=open(r'C:\Users\vzava\OneDrive\Escritorio\python\PRACTICA\Reservas.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.agregar(reserva(int(fila[0]),str(fila[1]),int(fila[2]),fila[3],str(fila[4]), int(fila[5]), float(fila[6])))
        archivo.close()
    def lenght(self):
        return len(self.__listareservas)
    def getcab(self, j):
        return self.__listareservas[j].getnumcab()
    def cheqres(self, cab):
        j=0
        band=False
        while j<len(self.__listareservas) and band==False:   
            if self.__listareservas[j].getnumcab()==cab:
                band=True
            j=j+1  
        if band==False:
            return False
        else:
            return True
    def busqfecha(self, fecha, gestorC):
        print("Nro cabaña   importe diario    Cantidad dias    Seña    Importe a cobrar")
        for i in range(len(self.__listareservas)):
            if (self.__listareservas[i].getfecha())==fecha:
                imptotal= gestorC.busqimp(self.__listareservas[i].getnumcab())*self.__listareservas[i].getcantd()+self.__listareservas[i].getimps()
                print(self.__listareservas[i].getnumcab(), "           ", gestorC.busqimp(self.__listareservas[i].getnumcab()), "           ", self.__listareservas[i].getcantd(), "         ", self.__listareservas[i].getimps(), "    ", imptotal)