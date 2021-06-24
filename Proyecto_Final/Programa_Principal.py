'''
NAME
	        Programa_Principal

VERSION
	        1.0

AUTHOR
	        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
            Programa que trabaja tanto con secuencias proteicas como de DNA,
            convierte archivos .txt a .fasta, encuentra sitios de restriccion y traduce
            secuencias de DNA a proteina.

CATEGORY
	         Genomic and Proteomic sequence

INPUT
	          Este programa recibe como input la ruta a un archivo .txt que contenga una
	          secuencia de DNA o aminoacidos segun sea el caso

OUTPUT
	          Este programa retorna como output un archivo en formato fasta si se elige la opcion 1, un
	          archivo con una secuencia de aminoacidos si se elige la opcion 2, la posicion de un sitio
	          de restriccion si se elige la opcion 3.
'''

#Importamos los paquetes necesarios
import Modulos.DNA
from Modulos import Archivo_Fasta
from Modulos import  DNA

#Se introduce al usuario al programa
print("\t\tBienvenido al programa :)\n")
print("Si desea convertir un archivo .txt a .fasta ingrese 1")
print("Si desea traducir una secuencia de DNA a proteina ingrese  2")
print("Si desea encontrar sitios de restriccion ingrese 3")
opcion = int(input("ELija una opcion: "))

#Si se elige la opcion 1 se convierte un archiv .txt a .fasta
if opcion == 1:

    #Se imprime el docstring
    print(Archivo_Fasta.fasta.__doc__)

    #Se solicitan los inputs al usuario
    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()
    print("Ingrese la ruta para el output: ")
    ruta_destino = input()

    #Se llama a la funcion
    Modulos.Archivo_Fasta.fasta(ruta_origen,ruta_destino)
else:
    pass

if opcion == 2:

    # Se imprime el docstring
    print(DNA.traduccion.__doc__)

    # Se solicitan los inputs al usuario
    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()
    print("Ingrese la ruta para el output: ")
    ruta_destino = input()

    #Se llama a la funcion
    Modulos.DNA.traduccion(ruta_origen, ruta_destino)
else:
    pass

if opcion == 3:

    # Se imprime el docstring
    print(DNA.sitios_restriccion.__doc__)

    # Se solicitan el input al usuario
    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()

    #Se llama a la funcion
    Modulos.DNA.sitios_restriccion(ruta_origen)
else:
    pass