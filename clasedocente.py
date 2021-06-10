from clasepersonal import personal

class docente(personal):
    cargos = ['simple', 'exclusivo']
    _carrera = ''
    _cargo = ''
    _catedra = ''

    def __init__(self, cuil='', apellido='', nombre='', basico=0, antiguedad=0, carrera='', cargo='', catedra='',
                 area='', tipo=''):
        super().__init__(cuil, apellido, nombre, basico, antiguedad, carrera, cargo, catedra, area, tipo)
        self._carrera = carrera
        self._cargo = cargo
        self._catedra = catedra
    def catedra(self):
        return self.catedra()

    def mostrardatos(self):
       super().mostrardatos()
       print(self._carrera)
       print(self._cargo)
       print(self._catedra)

    def getcarrera(self):
      self._carrera

    def gettipo(self):
        return 'Docente'

    def calcsueldo(self):
     sueldo = self._basico * (1 + 0.01 * self._antiguedad)
     if self._cargo.lower() == 'simple':
      porc = 0.1
     elif self._cargo.lower() == 'semiexclusivo':
      porc = 0.2
     else:
      porc = 0.5
     sueldo += porc * self._basico
     return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocente = dict(
            carrera=self._carrera,
            cargo=self._cargo,
            catedra=self._catedra)
        dic['atributos'].update(atribDocente)
        return dic
