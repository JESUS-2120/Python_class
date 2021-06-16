'''
NAME
        RNA_a_Proteina.py

VERSION
        1.0

AUTHOR
         Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa lee una seucnecia de ARN y devuelve como output la secuencia
        de amoniacidos de la proteina correspondiente

CATEGORY
        Genomic Sequence

INPUT
        Este programa recibe como input una secuencia de ARN

OUTPUT
        ESte programa retorna como output una secuencia de aminoacidos

EXAMPLES
        Input:
                AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

        Output:
                MAMAPRTEINSTRING
'''

#Definimos un diccionario con el codigo genetico
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T',
    'ACC':'T', 'ACG':'T', 'ACT':'T', 'AAC':'N', 'AAT':'N',
    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R',
    'AGG':'R', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'CAC':'H',
    'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
    'CGG':'R', 'CGT':'R', 'GTA':'V', 'GTC':'V', 'GTG':'V',
    'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
    'GGC':'G', 'GGG':'G', 'GGT':'G', 'TCA':'S', 'TCC':'S',
    'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L',
    'TTG':'L', 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

#Solicitamos al usuario una secuencia de RNA
dna = input("Ingrese una cadena de DNA: ")

#Se convierten los caracteres a mayusculas y se reemplazan 'U' por 'T'
dna = dna.upper()
dna = dna.replace("U","T")

#Definimos la variable proteina como una cadena vacia
proteina = ""

#Creamos un loop que recorra la secuencia de RNA
for i in range(0,len(dna),3):

    #Definimos subcadenas de 3 nucleotidos correpondientes a los codones
    triplete = dna[i : i+3]

    #Si se llega a un codon de paro se termina la traduccion y se imprime la proteina
    if gencode[triplete] == "_":
            print(proteina)
            exit()

    #Se concatena a la secuencia de la proteina el siguiente aminoacido
    proteina += gencode[triplete]

