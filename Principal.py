from Camion import Camion
from Cosecha import Cosecha
import csv

def agregarCamiones (listaCamiones, agregarCamion):
    if (agregarCamion[0] != '') & (agregarCamion[1] != '') & (agregarCamion[2] != '') & (agregarCamion[3] != '') & (agregarCamion[4].isdigit()):
         unCamion = Camion(agregarCamion[0],agregarCamion[1],agregarCamion[2],agregarCamion[3],int(agregarCamion[4]))
         listaCamiones.append(unCamion)

def cargarMatriz(matriz, AgregarKg, lista):
    if(AgregarKg[0].isdigit()) & (AgregarKg[1].isdigit()) & (AgregarKg[2].isdigit()):
        matriz.sumarKG(int(AgregarKg[0])-1,int(AgregarKg[1])-1,float(AgregarKg[2]) - lista[int(AgregarKg[0])-1].getTara())

def opcion0(matriz,listCamiones):
    print("Adiós")

def KgDescargados(matriz,listCamiones):
    i = (input('Ingrese el indentificador del camion del que quiere saber la cantidad de Kg descargados: '))
    if (i.isdigit()):
        i=int(i)
        print(i)
        if (i > 0) & (i <= 20):
            print(matriz.getKgDescargados(i-1))
        else:
            print('No hay algún camion con ese identificador')
    else:
        print('El valor ingresado es inválido.')

def mostrarFormato(matriz,listCamiones):
    j = int(input('Ingrese un día: '))
    if (j > 0) & (j <= 45):
        print('PATENTE   CONDUCTOR CANTIDAD DE KILOS\n')
        for i in range(len(listCamiones)):
            print('{:9} {:9} {:<17.2f}'.format(listCamiones[i].getPatente(),listCamiones[i].getConductor(), matriz.getKgDia(i,j-1)))
    else:
        print('No es un numero de día válido.')

switcher = {
    0: opcion0,
    1: KgDescargados,
    2: mostrarFormato,
}

def switch(argument, matriz,lista):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(matriz,lista)

if __name__ == '__main__':
    archivo = open('camiones.csv')
    reader = csv.reader(archivo, delimiter = ';')
    ListaCamiones = []
    for lista in reader:
        agregarCamiones(ListaCamiones, lista)
    archivo.close()
#    for elemento in ListaCamiones:
#        print(elemento)

    archivo = open('cosechado.csv')
    reader = csv.reader(archivo, delimiter = ';')
    matriz = Cosecha()
    for lista in reader:
        cargarMatriz(matriz,lista,ListaCamiones)
    archivo.close()
#    matriz.mostrarMatriz()

    bandera = False
    while not bandera:
        print("")
        print("0 Salir")
        print("1 Dado el número de identificador de un camión mostrar, la cantidad total de kilos descargados.")
        print("2 Dado un número correspondiente a un día mostrar un listado.")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion, matriz,ListaCamiones)
        bandera = int(opcion)==0
