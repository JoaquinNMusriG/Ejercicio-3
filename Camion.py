class Camion:
    __ID = ''
    __nombreConductor = ''
    __patenteCamion = ''
    __marcaCamion = ''
    __tara = 0

    def __init__ (self, id, nombre, patente, marca, tara):
        self.__ID = id
        self.__nombreConductor = nombre
        self.__patenteCamion = patente
        self.__marcaCamion = marca
        self.__tara = tara

    def __str__(self):
        return 'ID = %s nombreConductor = %s patenteCamion = %s marcaCamion = %s tara = %d'%(self.__ID,self.__nombreConductor,self.__patenteCamion,self.__marcaCamion,self.__tara)

    def getTara(self):
        return self.__tara

    def getNumId (self):
        return self.__ID

    def getConductor(self):
        return self.__nombreConductor

    def getPatente (self):
        return self.__patenteCamion
