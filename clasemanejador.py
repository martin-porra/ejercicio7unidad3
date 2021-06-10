from claselista import coleccion
from claseinvestigador import investigador
from clasedocenteinvestigador import DocenteInvestigador
from clasedocente import docente
from clasepersonalapoyo import apoyo
from clasepersonal import  personal
class manejador:
    __lista = None

    def __init__(self):
     self.__lista = coleccion()

    def llenar(self,Lista):
      for i in range(len(Lista)):
       dlista = Lista[i]
       class_name = dlista.pop('clase')
       class_=eval(class_name)
       atributos = dlista['atributos']
       unobjeto = class_(**atributos)
       self.__lista.agregarElemento(unobjeto)

    def mostrar(self):
        print('ingrese indice')
        ind = input()
        a =self.__lista.mostrarElemento(ind)
        if isinstance(a,docente):
            print('es docente')
        if isinstance(a,investigador):
            print('es investigador')
        if isinstance(a,DocenteInvestigador):
            print('es docente investigador')
        if isinstance(a,apoyo):
            print('es apoyo')
    def agregar(self, agente):
        if isinstance(agente, personal):
            self.__lista.agregarElemento(agente)
        else:
            print('Error: No se puede agregar el agente')
    def insertar(self,agente,indice):
        if isinstance(agente,personal):
            self.__lista.insertarElemento(agente,indice)
        else:
            print('Error: no se puede agregar el auto')
    def crearagente(self):
        print('ingrese datos del agente a añadir')
        cuil = input('cuil ')
        apellido = input('apellido ')
        nombre = input('nombre ')
        basico = input('sueldo basico ')
        antiguedad = input('antiguedad ')
        band = True
        while band == True:
         print('que tipo de agente quiere crear?')
         print('1-docente, 2-investigador, 3-investigador docente, 4-apoyo')
         op = input()
         if op == '1':
          carrera = input('carrera ')
          cargo = input('cargo ')
          catedra = input('catedra ')
          agente = docente(cuil,apellido,nombre,basico,antiguedad,carrera,cargo,catedra)
          band = False
         elif op == '2':
          area = input('area ')
          tipo = input('tipo ')
          agente = docente(cuil, apellido, nombre, basico, antiguedad, area,tipo)
          band = False
         elif op == '3':
          categoria = input('categoria')
          extra = input('extra')
          agente = docente(cuil, apellido, nombre, basico, antiguedad, categoria,extra)
          band = False
         elif op == '4':
          categoria = input('categoria')
          agente = docente(cuil, apellido, nombre, basico, antiguedad, categoria)
          band = False
         else:
          print('opcion incorrecta')
          op = input('1-docente, 2-investigador, 3-investigador docente, 4-apoyo')
        return agente

    def ordenar(self):
        cota = self.__lista.max() - 1
        k = 1
        while k != -1:
            k = -1
            for i in range(cota):
                agente1 = self.__lista.mostrarElemento(i)
                agente2 = self.__lista.mostrarElemento(i + 1)
                dato1 = agente1.getApellido()
                dato2 = agente2.getApellido()
                if dato1 > dato2:
                    self.__lista.cambiarelemento(agente2, i)
                    self.__lista.cambiarelemento(agente1, i + 1)
                    k = i
            cota = k

    def listadoporcarrera(self, carrera):
            self.ordenar()
            for agente in self.__lista:
                if isinstance(agente, DocenteInvestigador):
                    if carrera.lower() == agente.getcarrera().lower():
                        print('a')
                        agente.mostrardatos()

    def mostraerareas(self):
        areas = []
        for agente in self.__lista:
            if isinstance(agente, investigador):
                area = agente.getarea()
                if area not in areas:
                    areas.append(area)
        print('-'*50)
        for area in areas:
            print(area)
    def contararea(self,area):
        invest=0
        doceninv=0
        for agente in self.__lista:
            if isinstance(agente, investigador):
                if agente.getarea() == area:
                 invest =1+invest
            if isinstance(agente,DocenteInvestigador):
                if agente.getarea() == area:
                    doceninv =1+doceninv
        print('cantidad de investigadores en esta area: ' + str(invest-doceninv))
        print('cantidad de docentes investigadores en esta area: ' + str(doceninv))

    def listado(self):
        self.ordenar()
        for agente in self.__lista:
         print('-'*50)
         print(agente.getNombre())
         print(agente.getApellido())
         print(agente.gettipo())
         print(agente.calcsueldo())
    def categoria(self,cate):
        importe = 0
        for agente in self.__lista:
          if isinstance(agente, DocenteInvestigador):
              if agente.getcate().lower() == cate.lower():
                  print('-'*50)
                  print(agente.getApellido())
                  print(agente.getNombre())
                  print(agente.getextra())
                  importe+=agente.getextra()
        print(' total de dinero que la Secretaría de Investigación debe solicitar al Ministerio: '+ str(importe))

    def guardarJSON(self):
        listaJSON = [agente.toJSON() for agente in self.__lista]
        return listaJSON




