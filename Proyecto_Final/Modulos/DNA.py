'''
NAME
	        DNA

VERSION
	        1.0

AUTHOR
	        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
            El modulo DNA.py del package Modulos se utiliza para
            traducir secuencias de DNA a proteina asi como para
            encontrar sitios de restriccion

CATEGORY
	         Genomic Sequence

USAGE
            import Modulos.DNA
            import Modulos.DNA.[funcion de DNA]
            (En caso que el package haya sido inicializado)
            import Modulos
            Modulos.DNA.[funcion de DNA]

FUNCIONES
            funciones en este modulo: traduccion, sitios_restriccion
                traduccion(ruta_origen, ruta_destino):
                sitios_restriccion(ruta_origen):

TRY
            Error                                   Solucion
	         El archivo no fue hallado     Verificar que la ruta es correcta e introducirla de nuevo

	         Error                                      Solucion
	         La enzima no se halla en el     Verificar que el nombre es correcto e introducirlo de nuevo
	         diccionario

'''

#Funcion para traducir una secuencia de DNA a proteina
def traduccion(ruta_origen, ruta_destino):

    '''
    La funcion traduccion del Modulo DNA recibe como input un archivo (o secuencia introducida por el usuario)
    que contenga una secuencia de nucleotidos y devuelve como output la secuencia de aminoacidos
    correspondiente a la traduccion de la secuencia input en un archivo ubicado en la ruta indicada por el usuario
    '''

    # Definimos un diccionario con el codigo genetico
    gencode = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M', 'ACA': 'T',
        'ACC': 'T', 'ACG': 'T', 'ACT': 'T', 'AAC': 'N', 'AAT': 'N',
        'AAA': 'K', 'AAG': 'K', 'AGC': 'S', 'AGT': 'S', 'AGA': 'R',
        'AGG': 'R', 'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P', 'CAC': 'H',
        'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R',
        'CGG': 'R', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V',
        'GTT': 'V', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E', 'GGA': 'G',
        'GGC': 'G', 'GGG': 'G', 'GGT': 'G', 'TCA': 'S', 'TCC': 'S',
        'TCG': 'S', 'TCT': 'S', 'TTC': 'F', 'TTT': 'F', 'TTA': 'L',
        'TTG': 'L', 'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    # Verificamos que la ruta sea correcta y de no serla se avisara al usuario y se solicitara de nuevo
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

    #Leemos el archivo y gurdamos el contenido en dna
    dna = file.read()

    #Cerramos el archivo
    file.close()


    # Se convierten los caracteres a mayusculas y se reemplazan 'U' por 'T'
    dna = dna.upper()
    dna = dna.replace("U", "T")

    #Se crea el archivo que se retornara como output
    archivo = open(ruta_destino, "w")

    #Se crea la variable proteina y se le asigna un string vacio
    proteina = ""

    # Creamos un loop que recorra la secuencia de RNA
    for i in range(0, len(dna), 3):

        # Definimos subcadenas de 3 nucleotidos correpondientes a los codones
        triplete = dna[i: i + 3]

        # Si se llega a un codon de paro se termina la traduccion y se imprime la proteina
        if gencode[triplete] == "_":
            print(f"Se ha traducido la proteína y puede encontrar el archivo en {ruta_destino}")
            break

        # Se concatena a la secuencia de la proteina el siguiente aminoacido
        proteina += gencode[triplete]

    #escribimos la secuencia de la proteina en el archivo
    archivo.write(proteina)

#Funcion para identificar sitios de restriccion en una secuencia de DNA
def sitios_restriccion(ruta_origen):

    '''
   La funcion sitios_restriccion del Modulo DNA recibe como input un archivo que contenga una secuencia de
   nucleotidos y el nombre de una enzima de restriccion, devuelve como output la posicion de la secuencia
   en la que inicia el sitio de corte
   '''

    #Definimos un diccionario con las enzimas de restriccion
    enzimas_sitios = {'EcoRI' : r'GAATTC', 'BamHI' : r'GGATCC',
                                    'HindIII' : r'AAGCTT' , 'SspI' : r'AATATT',
                                    'SmaI' : r'CCCGGG', 'AvaII' : r'GG(A|T)CC',
                                    'BisI'  : r'GC[ATGC]GC'}

    #Se pide al usuario que ingrese el nombre de una enzima de restriccion
    print("Seleccione una enzima de restriccion para buscar el sitio de corte en la secuencia: ")
    enzima = input()

    #Se verifica que la enzima se encuentre en el diccionario, caso contrario se pide de nuevo el nombre al usuario
    if not (enzima in enzimas_sitios):
        print("La enzima que se eligio no se tiene en los registros")
        print("Desea elegir otra enzima? [S/N]: ")
        eleccion = input()

        if eleccion == "S":
            print("Seleccione una enzima de restriccion para buscar el sitio de corte en la secuencia: ")
            enzima = input()
        else:
            exit()

    else:
        pass

    # Verificamos que la ruta sea correcta y de no serla se avisara al usuario y se solicitara de nuevo
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

    # Leemos el archivo y gurdamos el contenido en dna
    dna = file.read()

    #Cerramos el archivo
    file.close()

    #Convertimos los caracteres a mayusculas
    dna = dna.upper()

    #Se busca en la secuencia el sitio de corte
    sitio_corte = (dna.find(enzimas_sitios[enzima])) + 1

    #Si se encuentra el sitio se le indica al usuario la posicion
    if sitio_corte > 0:
        print(f"El sitio de corte para la enzima {enzima} inicia en la posicion {sitio_corte}")
    else:
        print(f"No existe un sitio de corte para {enzima} en su secuencia")
        exit()