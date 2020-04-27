from Camion import Camion
import numpy as np

class Cosecha:
    __matriz = np.zeros((20,45))

    def __init__ (self):
        self.__matriz = np.zeros((20,45))

    def mostrarMatriz (self):
        for row in self.__matriz:
            for elem in row:
                print('%.2f '% (elem), end = '')
            print()

    def sumarKG (self, fila, columna, kilos):
        self.__matriz[fila][columna] += kilos

    def getKgDescargados(self, fila):
        return np.sum(self.__matriz[fila])

    def getKgDia(self, fila, columna):
        return self.__matriz[fila][columna]
