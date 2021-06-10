from zope.interface import implementer
from interface import Icoleccion
from clasenodo import Nodo

@implementer(Icoleccion)
class coleccion:
    __cabeza = None
    __actual = None
    __indice = 0
    __tope = 0
    def __init__(self):
       self.__cabeza = None
       self.__actual = None

    def __iter__(self):
      return self

    def __next__(self):
      if self.__indice == self.__tope:
         self.__actual = self.__cabeza
         self.__indice = 0
         raise StopIteration
      else:
        self.__indice += 1
        dato = self.__actual.getdato()
        self.__actual = self.__actual.getsiguiente()
        return dato
    def insertarElemento(self,objeto,indice):
        try:
            indice = int(indice)
            if indice >= 1 and indice <= self.__tope:
                miNodo = Nodo(objeto)
                nodo = self.__cabeza
                i = 1
                while i != indice:
                    anterior = nodo
                    nodo = nodo.getsiguiente()
                    i += 1
                miNodo.setsiguiente(nodo)
                if indice == 1:
                    self.__cabeza = miNodo
                    self.__actual = miNodo
                else:
                    anterior.setsiguiente(miNodo)
                self.__tope += 1
                print('Elemento agregado')
            else:
                print('Posicion fuera de los limites de la lista')
        except ValueError:
            print('Error: La posicion debe ser un entero')

    def agregarElemento(self,objeto):
      nod = Nodo(objeto)
      nod.setsiguiente(self.__cabeza)
      self.__cabeza = nod
      self.__actual = nod
      self.__tope = self.__tope + 1

    def mostrarElemento(self,indice):
        indice = int(indice)
        if indice > self.__tope:
         print('error indice mayor al numero de componentes')
        elif indice < 0:
         print('error indice inaccesible')
        else:
         i = 0
         aux = self.__cabeza
         while i != indice:
          aux = aux.getsiguiente()
          i +=1
         return  aux.getdato()

    def listar(self):
        aux = self.__cabeza
        for x in range(0, self.__tope):
            print('-'*40)
            aux.getdato().mostrar()
            aux = aux.getsiguiente()

    def max(self):
        return self.__tope

    def cambiarelemento(self, elemento, posicion):
        try:
            posicion = int(posicion)
            if posicion >= 0 and posicion < self.__tope:
                i = 0
                nodo = self.__cabeza
                while i != posicion:
                    nodo = nodo.getsiguiente()
                    i += 1
                nodo.setelemento(elemento)
            else:
                print('Error: Posicion fuera de los limites de la lista')
        except ValueError:
            print('Error: Posicion fuera de los limites de la lista')