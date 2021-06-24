'''
NAME
	        Archivo_Fasta

VERSION
	        1.0

AUTHOR
	        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
            El modulo Archivo_Fasta.py del package Modulos se utiliza para
            convertir archivos con secuencias en formato .txt a .fasta

CATEGORY
	        Fasta Files

USAGE
            import Modulos.Archivo_Fasta
            import Modulos.Archivo_Fasta.[funcion de Archivo_Fasta]
            (En caso que el package haya sido inicializado)
            import Modulos
            Modulos.Archivo_Fasta.[funcion de Archivo_Fasta]

FUNCIONES
            funciones en este modulo: fasta
            fasta(ruta_origen, ruta_destino):

TRY
            Error                                   Solucion
	         El archivo no fue hallado     Verificar que la ruta es correcta e introducirla de nuevo

'''

#Funcion para convertir un archivo con extension .txt a .fasta
def fasta(ruta_origen, ruta_destino):

    '''
    La funcion fasta del Modulo Archivo_Fasta recibe como input un archivo que contenga una secuencia ya sea de
    nucleotidos o aminoacidos con el formato:
    seq_1 = AATTTGG--CCTTAA
    seq_2 = QEGH--AR
    y devuelve como output dichas secuencias en un formato fasta ubicado en la ruta indicada por el usuario
    '''

    #Verificamos que la ruta sea correcta y de no serla se avisara al usuario y se solicitara de nuevo
    try:
        file = open(ruta_origen)
    except IOError:
        print("Lo sentimos, archivo no encontrado :(")
        print("Desea intentarlo de nuevo? [S/N]: ")

        desicion = input()
        desicion = desicion.upper()

        if desicion == "S":
            print("Ingrese la direccion de su archivo de secuencias: ")
            ruta_origen = input()
            file = open(ruta_origen)
        else:
            exit()

    #leemos todas las lineas del archivo
    all_lines = file.readlines()

    #Cerramos el archivo
    file.close()

    #Creamos el archivo output en la ruta indicada por el usuario
    fasta = open(ruta_destino, "w")

    #Se de el formato FASTA
    for line in all_lines:
        spl = line.split("=")
        fasta.write("> " + spl[0] + "\n" + spl[1].upper().replace('"', '').replace('-', ''))

    #Se avisa al usuario la conclusion del proceso
    print(f"\nEl archivo fasta se ha creado con exito y puede encontrarlo en {ruta_destino} bajo el nombre de sequences.fasta")