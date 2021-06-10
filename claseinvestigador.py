from clasepersonal import personal

class investigador(personal):
    _area = ''
    _tipo = ''

    def __init__(self,cuil='',apellido='',nombre='',basico=0,antiguedad=0,carrera='',cargo='',catedra='',area='',tipo=''):
        super().__init__(cuil,apellido,nombre,basico,antiguedad,carrera,cargo,catedra,area,tipo)
        self._area = area
        self._tipo = tipo


    def mostrardatos(self):
        super().mostrardatos()
        print(self._area)
        print(self._tipo)
    def getcarrera(self):
      self._carrera
    def getarea(self):
        return self._area

    def gettipo(self):
        return 'Investigador'

    def calcsueldo(self):
        sueldo = self._basico * (1 + 0.01 * self._antiguedad)
        return round(sueldo, 2)
    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribInvestigador = dict(
            area = self._area,
            tipo = self._tipo)
        dic['atributos'].update(atribInvestigador)
        return dic