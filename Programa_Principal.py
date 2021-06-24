import Modulos.DNA
from Modulos import Archivo_Fasta
from Modulos import  DNA

print("\t\tBienvenido al programa :)\n")
print("Si desea convertir un archivo .txt a .fasta ingrese 1")
print("Si desea traducir una secuencia de DNA a proteina ingrese  2")
print("Si desea encontrar sitios de restriccion ingrese 3")
opcion = int(input("ELija una opcion: "))

if opcion == 1:
    print(Archivo_Fasta.fasta.__doc__)

    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()

    print("Ingrese la ruta para el output: ")
    ruta_destino = input()

    Modulos.Archivo_Fasta.fasta(ruta_origen,ruta_destino)
else:
    pass

if opcion == 2:
    print(DNA.traduccion.__doc__)

    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()

    print("Ingrese la ruta para el output: ")
    ruta_destino = input()

    Modulos.DNA.traduccion(ruta_origen, ruta_destino)
else:
    pass

if opcion == 3:
    print(DNA.sitios_restriccion.__doc__)

    print("Ingrese la ruta de su archivo de secuencias: ")
    ruta_origen = input()

    Modulos.DNA.sitios_restriccion(ruta_origen)
else:
    pass