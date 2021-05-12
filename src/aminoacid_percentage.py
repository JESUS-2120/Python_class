'''
NAME
        Calculo del porcentaje de una lista de aminoacidos

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa calcula el porcentaje de aminoacidos proporcionados por el usuario
        en una proteína igualmente introducida por el usuario

INPUT
        Este programa recibe como input una seria de aminoacidos dada por el usuario
        (a menos que prefiera la lista por default), asi como una secuencia de aminoacidos

OUTPUT
        Este programa retorna como output el porcentaje de los aminoacidos introducidos por
        el usuario en la proteina

EXAMPLES
        Input
            MSRSLLLRFLLFLLLLPPLP
            (lista por default)

        Output
            Usted decidio hacer conteo de aminiacidos hidrofobicos en la secuencia

        Para la lista de aminoacidos:
        A
        I
        L
        M
        F
        W
        Y
        V
        El porcentaje de esos aminoacidos en la proteina es:

        65.0%

GITHUB
        https://github.com/JESUS-2120/Python_class/blob/master/src/aminoacid_percentage.py

'''


# creamos una funcion test que nos sirve para comprobar que nuestro programa funciona de manera adecuada
def test(proteina_test):
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
    assert porcentaje_aa("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
    return (0)


# Creamos la funcion para obtener el porcentaje de los aminoacidos en la lista dentro de la proteina introducida
# por el usuario, recibe como parametros la proteina y la lista de aminoacidos
def porcentaje_aa(proteina, lista_aa):
    # porcentaje esta inicializado a cero pues es un acumulador que necesita ser inicializado
    porcentaje = 0
    # hay un bucle for para sacar el porcentaje àra cada aminoacido en la lista
    for aminoacid in lista_aa:
        porcentaje += (proteina.count(aminoacid) * 100) / len(proteina)
    # la funcion retorna el valor del porcentaje
    return (porcentaje)


# con un amigable mensaje se introduce al usuario al programa y se pide que ingrese una secuencia de aminoacidos (proteina)
print("Introduzca la secuencia de la proteina: ")
# se guarda la secuencia en la variable proteina y se pasa a mayusculas
proteina = input().upper()

# se pregunta al usuario si desea ingresar su propia lista de aminoacidos o si prefiere trabajar con el default
print(
    "si desea introducir su propia lista de aminoacidos ingrese 1 y para hacerlo con la lista por default (aminoacidos hidrofobicos) ingrese 2: ")
# su eleccion se guarda en opc
opc = int(input())

# en caso que el usuario haya decidido ingrsar su propia lista se ejecuta el if
if opc == 1:
    # se inicializa i a 0 de modo que se pueda iterar para que el usuario introduzca la cantidad de aminoacidos que desee a la lista
    i = 0
    # se registra el numero de aminoacidos que el usuario introducira en la lista
    c = int(input("Ingrese cuantos aa hay en su lista: "))
    # se crea una lista vacia, la cual contendra loa aminoacidos introducidos por el usuario
    lista_aa = []
    # dentro de un bucle while se añaden los elementos en la lista
    while i < c:
        i += 1
        print("Ingrese el animoacido: ")
        aa_user = input().upper()
        lista_aa.append(aa_user)
    print("Para la lista de aminoacidos: ")
    # se imprime la lista indicando al usuario los aminoacidos que se contaron
    for aminoac in lista_aa:
        print(f"{aminoac}")
    print(f"El porcentaje de esos aminoacidos en la proteina es:\n")
    # se llama a la funcion, la cual retorna el porcentaje de los aminoacidos en la proteina
    print(f"{porcentaje_aa(proteina, lista_aa)}%")

# en caso de haber seleccionado la opcion 2 el usuario ya no debe ingresar la lista de aminoacidos pues esta esta designada por default
elif opc == 2:
    print("Usted decidio hacer conteo de aminiacidos hidrofobicos en la secuencia\n")
    # se tiene la lista ya creada con los aminoacidos hidrofobicos
    lista_aa = ['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']
    # se imprime la lista indicando al usuario los aminoacidos que se contaron
    print("Para la lista de aminoacidos: ")
    for aminoac in lista_aa:
        print(f"{aminoac}")
    print(f"El porcentaje de esos aminoacidos en la proteina es:\n")
    # se llama a la funcion, la cual retorna el porcentaje de los aminoacidos en la proteina
    print(f"{porcentaje_aa(proteina, lista_aa)}%")

if test("MSRSLLLRFLLFLLLLPPLP") == 0:
    print("Process done succesfully")
