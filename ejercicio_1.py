import random
import numpy as np

def crear_random(cantidad):
  with open('numeros_prueba.txt', 'w') as file:
    for i in range(cantidad):
      numero_aleatorio = random.randint(100, 1000)
      file.write(str(numero_aleatorio))
      file.write("\n")

def leer_archivo():
    numeros = []
    numeros_impar = []
    with open('numeros_prueba.txt', 'r') as file:
        for linea in file:
            numeros.append(int(linea))
    for numero in numeros:
      if(numero%2 != 0):
        numeros_impar.append(numero)
    return numeros,numeros_impar

def dimension_lista(lista):
    lista = np.array(lista)
    print("y la dimension de la lista es de: " + str(lista.ndim))

def mostrar_datos():
  numeros_random(20)
  numeros = []
  numeros_par = []
  numeros,numeros_impar = leer_archivo()
  print("La lista de numeros impar es: " + str(numeros_impar))
  dimension_lista(numeros_impar)

if __name__ == "__main__":
    main()
