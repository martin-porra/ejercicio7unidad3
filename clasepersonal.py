import abc
from abc import ABC


class personal(ABC):
    _cuil = ''
    _apellido = ''
    _nombre = ''
    _basico = 0
    _antiguedad = 0

    def __init__(self, cuil='', apellido='', nombre='', basico=0, antiguedad=0, carrera='', cargo='', catedra='',
                 area='', tipo=''):
        self._cuil = cuil
        self._apellido = apellido
        self._nombre = nombre
        self._basico = basico
        self._antiguedad = antiguedad

    def getNombre(self):
        return self._nombre
    def getApellido(self):
        return self._apellido

    @abc.abstractmethod
    def gettipo(self):
        pass

    @abc.abstractmethod
    def calcsueldo(self):
        pass

    def mostrardatos(self):
        print('-----------------------------------')
        print(self._cuil)
        print(self._apellido)
        print(self._nombre)
        print(self._basico)
        print(self._antiguedad)
    def toJSON(self):
        dic = dict(
            clase=self.__class__.__name__,
            atributos=dict(
                cuil=self._cuil,
                apellido=self._apellido,
                nombre=self._nombre,
                basico=self._basico,
                antiguedad=self._antiguedad))
        return dic
