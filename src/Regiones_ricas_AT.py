'''
NAME
        Regiones ricas en AT

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx

DESCRIPTION
        Este programa retorna las regiones ricas en AT de una secuencia de DNA y
        marca error si las secuencias presentan caracteres no correspondientes a
        alguna de las 4 bases (ATCG).

CATEGORY
        Genomic Sequence

INPUT
        Este programa recibe como input una secuencia de DNA introducida por el usuario
        desde la consola

OUTPUT
        En caso de contener caracteres ajenos a las 4 bases (ATCG) se mostrara un error y
        se indicara al usuario cuales son los caracteres incorrectos

Github:
        https://github.com/JESUS-2120/Python_class/blob/master/src/Regiones_ricas_AT.py

FUNCIONES
	    ["Busqueda_Carac", "Contenido_AT"]
	    def Busqueda_Carac(dna_seq):
            try:
                if re.search(r"[^ATGC]", dna_seq):
                  raise e

            except:
                Caracter = re.split(r"[ATGC]", dna_seq)
                print("Su secuencia contiene caracteres raros")
                for char in Caracter:
                    if char:
                     print(f"El caracter extrano es: {char}")
                exit()

        def Contenido_AT(dna_seq):
            Busqueda_Carac(dna_seq)
            DNA = re.split(r"(G|C)", dna_seq)
            print("Las regiones ricas en AT en su secuencia son: \n")
            i = 0
            for region in DNA:
                regiones_ricas = re.search(r"(A|T){5,}", region)
                if regiones_ricas:
                    regiones_ricas = regiones_ricas.group()
                    i += 1
                    print(f"{i}) {regiones_ricas}\n")
EXAMPLES
        Input:
            CTGCATTATATCGTACGAAATTATACGCGCG

        Output:
            Las regiones ricas en AT en su secuencia son:

            1) ATTATAT

            2) AAATTATA
'''

#Importamos la libreria
import re

#Definimos la funcion Busqueda_Carac, la cual toma como parametro la secuencia de DNA
def Busqueda_Carac(dna_seq):
    #Probamos el codigo en busqueda de caracteres raros
    try:
            if re.search(r"[^ATGC]", dna_seq):
                #Si se ecuentra un caracter raro se evoca un error
                raise ValueError

    except:
            #Si se encuentra un caracter raro se le comunica al usuario y se imprimen los caracteres
            #que se encontraron
            Caracter = re.split(r"[ATGC]", dna_seq)
            print("Su secuencia contiene caracteres raros")
            for char in Caracter:
                if char:
                    print(f"El caracter extrano es: {char}")
            #Si se encuentra un caracter raro se mata el programa
            exit()

#Definimos la funcion Contenido_AT la cual toma como parametro la secuencia de DNA
def Contenido_AT(dna_seq):
    #Se llama a la funcion Busqueda_Carac para buscar caracteres raros
    Busqueda_Carac(dna_seq)
    #Se hace una lista con las regiones que contienen AT
    DNA = re.split(r"(G|C)", dna_seq)
    print("Las regiones ricas en AT en su secuencia son: \n")
    i = 0
    #Se evalua si las regiones que contienen AT son ricas
    for region in DNA:
        regiones_ricas = re.search(r"(A|T){5,}", region)
        if regiones_ricas:
            regiones_ricas = regiones_ricas.group()
            i += 1
            #Se imprimen las regiones ricas en AT
            print(f"{i}) {regiones_ricas}\n")

#Se introduce al usuario al programa
print("Este programa muestra las regiones ricas en AT de una secuencia de DNA")
#Se solicita al usuario Una secuencia de DNA
print("Introduzca una secuencia de DNA: ")
#Se guarda el input en la variable dna y se convierte a mayusculas
dna = input()
dna = dna.upper()

#Se llama a la funcion Contenido_AT y se le pasa como parametro la secuencia
Contenido_AT(dna)
