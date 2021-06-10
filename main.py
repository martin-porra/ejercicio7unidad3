from clasemanejador import  manejador
from claseobject import ObjectEncoder
def menu():
 print('[1]- Insertar a agentes a la colección.')
 print('[2]- Agregar agentes a la colección.')
 print('[3]- Tipo de agente almacenado en una posición dada.')
 print('[4]- Docentes investigadores de una carrera ordenados por nombre.')
 print('[5]- Cantidad de Docentes Investigadores e Investigadores según área.')
 print('[6]- Listar todos los agentes ordeandos por apellido.')
 print('[7]- Listar Docentes Investigadores por categoria.')
 print('[8]- Almacenar los datos de todos los agentes en el archivo "personal.json".')

if __name__ == '__main__':
 maneja = manejador()
 encoder = ObjectEncoder()
 lista = encoder.leerJSONArchivo('personal.json')
 maneja.llenar(lista)
 bande = True
 while bande == True:
  menu()
  op = input('ingresar opcion ')
  if op == '1':
   au = maneja.crearagente()
   print('ingrese indice a colocar')
   ind = int(input())
   maneja.insertar(au,ind)
  elif op == '2':
   au = maneja.crearagente()
   maneja.agregar(au)
  elif op == '3':
   maneja.mostrar()
  elif op == '4':
   print('carreras: LCC,LCI')
   print('ingresar carrera para listar datos')
   care = input()
   maneja.listadoporcarrera(care)
  elif op == '5':
   maneja.mostraerareas()
   area = input('ingresar area ')
   maneja.contararea(area)
  elif op == '6':
   maneja.listado()
  elif op == '7':
   print('ingrese una categoria (I, II, III, IV o V)')
   cate = input()
   maneja.categoria(cate)
  elif op == '8':
   listaJSON = maneja.guardarJSON()
   encoder.guardarJSONArchivo(listaJSON, 'personal.json')
   print('Archivo guardado')
  else:
   print('opcion incorrecto')
   bande = False
 print('Fin')

