'''
NAME
        Busqueda del codon inicial y secuencia transcrita

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa recibe como entrada una secuencia de ADN e indica el codon
        de inicio y la secuencia que se empezará a transcribir, asi como la posicion 
        de la ultima base del codon de paro (ATT, ATC, ACT)

CATEGORY
        Genomic-Sequence

INPUT
        Lee una secuencia de DNA (ATCG) introducida por el usuario

OUTPUT
        Retorna como output las posiciones de inicio y final de la secuencia que sera
        transcrita.

EXAMPLES
    Input
     ADN = 'AAAATACACCTCCGCACCCCACCCTGTCCCAGCCACCTCCACGCTGGGCCGAGCTGCGACTTTACTCTGCTCCGCGACTTTTT'

    Output
    El codon TAC empieza en la posicion  5  y el codon de paro termina en la posicion 61
    La secuencia de RNA:
    UACACCUCCGCACCCCACCCUGUCCCAGCCACCUCCACGCUGGGCCGAGCUGCGACU
'''

print('Bienvenido a su programa de busqueda de codon incial y secuencia transcrita')
print('Introdusca una secuencia de  DNA (A, G, C, T) que contenga un codon de inicio y un codon de paro para asi conocer sus posiciones dentro de esta:')

DNA = input()

posicion_inicio = DNA.find('TAC')
posicion_final = DNA.find('ATT')
if(posicion_final < 0):
    posicion_final = DNA.find('ATC')
if(posicion_final < 0):
    posicion_final = DNA.find('ACT')
posicion_final += 3

ORF = DNA[posicion_inicio:posicion_final]
mRNA = ORF.replace('T','U')

if(posicion_inicio == 0):
     print('No hay una secuencia codificante en la secuencia introducida')
     print('No existe un codon de inicio para hacer un RNA')
else:
     print('El codon de inicio comienza en la posicion: ', posicion_inicio + 1,' y termina en la posicion: ', posicion_final)    
     print('La secuencia del mRNA es: \n' + mRNA)
