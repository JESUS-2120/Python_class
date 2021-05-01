'''
NAME
        Creacion de un archivo fasta

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

GitHub
        https://github.com/JESUS-2120/Python_class/blob/master/src/archivo_fasta.py

DESCRIPTION
        Este programa crean un archivo fasta a partir de la secuencia de DNA
        que esta en 4_dna_sequences.txt ubicado en la carpeta data/

CATEGORY
        Genomic sequence

INPUT
        El input de este programa es el archivo 4_dna_sequences.txt ubicado en
        la carpeta data/

OUTPUT
        El output de este programa es un archivo fasta de las secuencias que hay
        en el archivo 4_dna_sequences.txt (input).

EXAMPLES
    Input
    archivo: data/4_dna_sequences.txt
    seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
    seq_2 = "actgatcgacgatcgatcgatcacgact"
    seq_3 = "ACTGAC-ACTGT-ACTGTA----CATGTG"

    Output
    Archivo: src/dna_sequences.fasta
    > seq_1
    ATCGTACGATCGATCGATCGCTAGACGTATCG
    > seq_2
    ACTGATCGACGATCGATCGATCACGACT
    > seq_3
    ACTGACACTGTACTGTACATGTG
'''
'''
Abrimos el archivo 4_dna_sequences.txt ubicado en la carpeta data haciendo
uso de open(), guardamos el contenido dentro de file.
'''
file = open("../data/4_dna_sequences.txt")

'''
mediante el metodo readlines() leeremos todas las lineas en el archivo en forma de lista separando los 
elementos con un salto de linea \n
'''
all_lines = file.readlines()

#Procedemos a cerrar el archivo
file.close()
'''
para crear el archivo fasta abriremos un nuevo archivo con open(), y con el
argumento w indicamos que escribiremos en ese nuevo archivo que hemos creado
'''
fasta = open("../docs/dna_sequences.fasta", "w")

'''
Dado que nuestro archivo input consta de una lista que contiene las secuencias
utilizaremos un ciclo for para procesar cada elemento en la lista, en este caso
cada secuencia, ya que el encabezado esta separado de la secuencia de DNA 
por un signo "=" para poder separarlos (en otra lista) utilizaremos split("=")
de modo que el encabezado y la secuencia sean elementos de una nueva lista 
['seq1','ATGC.....TT'], una vez que tenemos el encabezado y la secuencia separados
podemos escribirlos en el nuevo archivo con el formato deseado mediante el metodo write().
'''

for line in all_lines:
    spl=line.split("=")
    fasta.write("> "+spl[0]+"\n"+spl[1].upper().replace('"','').replace('-',''))

#Por ultimo indicamos al usuario que su archivo ha sido creado y el directorio donde se encuentra
print("\nEl archivo fasta se ha creado con exito y puede encontrarlo en la carpeta docs bajo el nombre de dna_sequences.fasta")
