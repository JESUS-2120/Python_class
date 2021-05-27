'''
NAME
        Contenido_de_AT

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION

        Compute the AT content of a DNA sequences

CATEGORY
        Genomic sequence

ARGUMENTS
        -i #, --input=#   read sequence from # (must be in ... format)
        -o #, --output=#  output results to #
                              if not specified, the standard output is used

INPUT FILE FORMAT
        The input file has the next format:
                seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
                seq_2 = "actgatcgacgatcgatcgatcacgact"
                seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"
                seq_4 = "ATTCTGNNNNNNNNNNNNNGTC"

OUTPUT FILE

        Formato fastA incluye el contenido de AT

        > seq_1 at:47.0%
        ATCGTACGATCGATCGATCGCTAGACGTATCG
        > seq_2 at:47.0%
        ACTGATCGACGATCGATCGATCACGACT
        > seq_3 at:52.0%
        ACTGACACTGTACTGTACATGTG
        
USAGE
        Contenido_de_AT.py -i inputfile [-o outputfile]


EXAMPLES

        % python3  Contenido_de_AT.p -i 4_dna_sequences.txt

        InputFile Content:
        seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
        seq_2 = "actgatcgacgatcgatcgatcacgact"
        seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"

        Output:
        > seq_1 at:47.0%
        ATCGTACGATCGATCGATCGCTAGACGTATCG
        > seq_2 at:47.0%
        ACTGATCGACGATCGATCGATCACGACT
        > seq_3 at:52.0%
        ACTGACACTGTACTGTACATGTG

Github:
https://github.com/JESUS-2120/Python_class/blob/master/src/Contenido_de_AT.py

'''

########################################
# IMPORTS
########################################
import argparse
import sys
import os

########################################
# COMMAND LINE OPTIONS
########################################
parser = argparse.ArgumentParser(description="Programa que calcula la secuencia de AT de una secuencia")

parser.add_argument("-i", "--input",
                    metavar="Ruta del archivo input",
                    type=str,
                    help="Archivo con una secuencia de DNA",
                    required=True)

parser.add_argument("-o", "--output",
                    metavar="Ruta del archivo output",
                    type=str,
                    help="Archivo que guardara el contenido de AT de la secuencia input",
                    default="contenido_at_output.txt",
                    required=False)

########################################
# FUNCTIONS
########################################
class AmbiguousBaseError(Exception):
    '''
    Catch de raise error and Only pass, do nothing
    :param str Exception : Error description
    '''
    pass

def get_at_content(seq, round_value = 2):
    '''
    Calculates the AT content of a dna sequence
    :param int seq : sequence for calculating the AT content
    :return float cont: AT content porcentage
    '''
    seq = seq.upper()

    #Validar que la secuencia no tenga Ns
    if seq.count("N") > 0:
        raise AmbiguousBaseError(f'Sequence contains {seq.count("N")} N\'s')

    # Calcula contenido de AT
    at_content = (seq.count("A") + seq.count("T")) / len(seq)
    at_content = (round(at_content, round_value)) * 100

    return at_content


########################################
#   MAIN
########################################

# Leer argumentos
args = parser.parse_args()
input_rout = args.input
output_rout = args.output

# Validar archivo de entrada
try:
    f = open(input_rout)
    f.close
except IOError:
    print("Error! Introduzca el archivo de entrada path/filename: ")
    input_rout = input()

#Leer el archivo de entrada
file = open(input_rout)
all_lines = file.readlines()
file.close()

# Crear archivo de resultados - en formato FastA
output = open(output_rout,"w")

# Para cada secuencia del archivo
for line in all_lines:

    spl = line.split("=")

    # eliminar -, en la secuencia
    sequence = spl[1].upper().replace('"','').replace('-','')

    try:
        # Obtener contenido de at
        at_content = get_at_content(sequence)

        #Guardar en formato FastA
        output.write(">" + spl[0] + "  at: " + str(at_content) + "\n")
        output.write(sequence)

    except AmbiguousBaseError as ex:
        print('skipping invalid sequence for ' + spl[0] + ex.args[0])


print(f"El archivo con el contenido de AT se genero con exito y lo puede encontrar en:\n{output_rout}")
