'''
NAME
        Contenido_de_AT

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa lee un archivo de secuencias de DNA y retorna como output un
        archivo que contenga el contenido de AT para cada secuencia.

CATEGORY
        Genomic sequence

ARGUMENTS
        -i,--input  Ruta del archivo que se utilizara como input, debe contener una secuancia de DNA
        -o,--output  Ruta del archivo que se retornara como output

INPUT
        Archivo txt que contiene secuencias de DNA con el siguiente formato:
        seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
        seq_2 = "actgatcgacgatcgatcgatcacgact"
        seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"
        seq_4 = "ATTCTGNNNNNNNNNNNNNGTC"

OUTPUT
        Archivo txt que contiene las secuencias de DNA con su correspondiente contenido de AT con el
        siguiente formato:
        El contenido de AT de las secuencias en su archivo input es:
        > ATCGTACGATCGATCGATCGCTAGACGTATCG
        47.0%
        > ACTGATCGACGATCGATCGATCACGACT
        47.0%
        > ACTGACACTGTACTGTACATGTG
        52.0%

EXAMPLES
        Terminal:
        python3 PycharmProjects/Python_class/src/Contenido_de_AT.py
        --input PycharmProjects/Python_class/data/4_dna_sequences.txt

        Input:
        seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
        seq_2 = "actgatcgacgatcgatcgatcacgact"
        seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"

        Output:
        El contenido de AT de las secuencias en su archivo input es:
        > ATCGTACGATCGATCGATCGCTAGACGTATCG
        47.0%
        > ACTGATCGACGATCGATCGATCACGACT
        47.0%
        > ACTGACACTGTACTGTACATGTG
        52.0%
Github:
https://github.com/JESUS-2120/Python_class/blob/master/src/Contenido_de_AT.py	



'''

#Importamos las librerias necesarias para recibir los argumentos en la terminal
import argparse
import sys
import os

#Creamos el parser
parser = argparse.ArgumentParser(description="Programa que calcula la secuencia de AT de una secuencia")

#Anadimos los argumentos en este caso --input y --output
parser.add_argument("-i", "--input",
                    metavar="Ruta del archivo input",
                    type=str,
                    help="Archivo con una secuencia de DNA",
                    required=True)

parser.add_argument("-o", "--output",
                    metavar="Ruta del archivo output",
                    type=str,
                    help="Archivo que guardara el contenido de AT de la secuencia input",
                    required=False)

#Definimos una funcion que determine el contenido de AT para cada secuencia que recibe como parametro
# y retornamos el contenido de AT
def get_at_content(seq):
    seq = seq.upper()

    #En caso que una secuencia tenga N se marca un error y se eliminan los archivo tanto el temporal como
    # el que contendria el output
    if seq.count("N") > 0:
        os.remove("PycharmProjects/Python_class/docs/sequences.fasta")
        os.remove("PycharmProjects/Python_class/docs/contenido_at_output.txt")
        raise ValueError(f'Sequence contains {seq.count("N")} N\'s')

    cont = (seq.count("A") + seq.count("T"))/len(seq)
    cont = (round(cont, 2))*100
    return cont

#Ejecutamos el metodo parse_args
args = parser.parse_args()
input_rout = args.input
output_rout = args.output

#Mediante un try verificamos si existe el archivo indicado comom input y en caso contrario se solicita
# la ruta del archivo con el que se desea trabajar
try:
    f = open(input_rout)
except IOError:
    print("Por favor ingrese la direccion de un input")
    print("Ingrese la direccion de un archivo input: ")
    input_rout = input()

#Abrimos el archivo indicado como input y leemos todas las lineas que hay en este mediante all_lines
# y cerramos el archivo
file = open(input_rout)
all_lines = file.readlines()
file.close()

#Vamos a crear un archivo temporal que contenga unicamente las secuencias de DNA y ningun otro simbolo
fasta = open("PycharmProjects/Python_class/docs/sequences.fasta", "w")

#Mediante un if verificamos que el usuario haya ingresado una ruta para el archivo output (no es un argumento obligatorio)
# en caso de no haber ingresado dicho argumento se utiliza una ruta y nombre por default
if len(sys.argv) < 4:
    output_rout = "PycharmProjects/Python_class/docs/contenido_at_output.txt"

#Se crea y abre para escribir el archivo que se entregara como output al usuario
output = open(output_rout,"w")

#Para cada linea del archivo input proporcionado por el usuario nos quedamos unicamente con la parte de la secuencia de DNA
# y las escribimos dentro del archivo temporal denominado sequences.fasta
for line in all_lines:
    spl=line.split("=")
    fasta.write(spl[1].upper().replace('"','').replace('-',''))

#Se cierra el archivo que acabamos de escribir
fasta.close()

#Abrimos el archivo que acabamos de crear y leemos todas las lineas, que en este caso corresponden a la secuencia de DNA
archivo_seq = open("PycharmProjects/Python_class/docs/sequences.fasta")
sequences = archivo_seq.readlines()

#Escrbibimos la primer linea del archivo output, la cual en este caso nos indica que hay en dicho archivo
output.write("El contenido de AT de las secuencias en su archivo input es: \n")

#Vamos a escribir la secuencia seguida de su contenido de AT (en porcentaje) la cual obtenemos con la funcion
# get_at_content(seq) la que recibe como parametro la secuencia de DNA
for seq in sequences:
    output.write(">"+seq)
    output.write(str(get_at_content(seq))+"%"+"\n")

#Removemos el archivo temporal que hemos creado
os.remove("PycharmProjects/Python_class/docs/sequences.fasta")

#Por ultimo le indicamos al usuario que el programa se ejecuto con exito y le indicamos la ruta donde este se ubica
print(f"El archivo con el contenido de AT se genero con exito y lo puede encontrar en:\n{output_rout}")
