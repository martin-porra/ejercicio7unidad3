from clasedocente import docente
from claseinvestigador import investigador


class DocenteInvestigador(investigador, docente):
    categorias = ['I', 'II', 'III', 'IV', 'V']
    __categoria = ''
    __extra = 0

    def __init__(self, cuil='', apellido='', nombre='', basico=0, antiguedad=0, carrera='', cargo='', catedra='',
                 area='', tipo='', categoria='', extra=0):
        super().__init__(cuil, apellido, nombre, basico, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoria = categoria
        self.__extra = extra
    def mostrardatos(self):
     super().mostrardatos()
     print(self.__categoria)
     print(self.__extra)
    def getcarrera(self):
     return self._carrera
    def getcate(self):
        return self.__categoria
    def gettipo(self):
        return 'Docente Investigador'
    def getextra(self):
        return self.__extra

    def calcsueldo(self):
        sueldo = docente.calcsueldo(self)
        sueldo += self.__extra
        return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocenteInvestigador = dict(
            categoria=self.__categoria,
            extra=self.__extra)
        dic['atributos'].update(atribDocenteInvestigador)
        return dic