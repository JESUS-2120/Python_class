def fasta(ruta_origen, ruta_destino):

    '''
    La funcion fasta del Modulo_1 recibe como input un archivo que contenga una secuencia ya sea de
    nucleotidos o aminoacidos con el formato:
    seq_1 = AATTTGG--CCTTAA
    seq_2 = QEGH--AR
    y devuelve como output dichas secuencias en un formato fasta ubicado en la ruta indicada por el usuario
    '''

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

    all_lines = file.readlines()

    file.close()

    fasta = open(ruta_destino, "w")

    for line in all_lines:
        spl = line.split("=")
        fasta.write("> " + spl[0] + "\n" + spl[1].upper().replace('"', '').replace('-', ''))

    print(f"\nEl archivo fasta se ha creado con exito y puede encontrarlo en {ruta_destino} bajo el nombre de sequences.fasta")