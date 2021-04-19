'''
NAME
        Calculo del contenido de AGCT

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

GitHub
        https://github.com/JESUS-2120/Python_class/blob/master/src/contenido_ATCG.py

DESCRIPTION
        Dada una secuencia de DNA (AGCT) este programa calcula el contenido de cada una de las bases dentro
        de la secuencia introducida por el usuario.

CATEGORY
        Genomic-Sequence

INPUT
        Este programa recibe como input una secuencia de DNA (AGCT) introducida por el usuario ya sea en
        mayusculas o en minusculas.

OUTPUT
     Este programa retorna como output la cantidad de cada una de las 4 bases en la secuencia introducida por el usuario.

EXAMPLES
       Input
     ADN = 'AAAAATCACCTCCGCACCCCACCCTGTCCCAGCCACCTCCACGCTGGGCCGAGCTGCGACTTTACTCTGCTCCGCGACTTTTT'

    Output
    dada la secuencia de ADN los contenidos de A, G, C y T son :
    El contenido de A es: 15
    El contenido de T es: 18
    El contenido de G es: 14
    El contenido de C es: 36
'''

print("\tBienvenido")
dna = input("Introdusca una secuencia de ADN: ")
dna = dna.upper()
print(f"dada la secuencia de ADN los contenidos de A, G, C y T son : ")
contenido_A = dna.count('A')
contenido_T = dna.count('T')
contenido_G = dna.count('G')
contenido_C = dna.count('C')
print(f"El contenido de A es: {contenido_A}\nEl contenido de T es: {contenido_T}")
print(f"El contenido de G es: {contenido_G}\nEl contenido de C es: {contenido_C}")
