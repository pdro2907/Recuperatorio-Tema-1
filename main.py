from GestorCabañas import GestorCabañas
from GestorReservas import GestorReservas
def menu(gestorR, gestorC):
    op=input()
    if op=='a':
        canth= int(input())
        gestorC.busq(canth, gestorR)
    elif op=='b':
        fecha= str(input())
        gestorR.busqfecha(fecha, gestorC)
    return

if __name__=='__main__':
    gestorC=GestorCabañas()
    gestorR=GestorReservas()
    gestorC.carga()
    gestorR.carga()
    menu(gestorR, gestorC)