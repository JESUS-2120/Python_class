'''
NAME
        Genes_Drosophila

VERSION
        1.0

AUTHOR
        Victor Jesus Enriquez Castro  <victorec@lcg.unam.mx>

DESCRIPTION
        Este programa lee un archivo que contien nombre de la especie, secuencia del gen, nombre del gen y nivel de
        expresion e imprime a pantalla los nombres de ciertos genes bajo ciertos criterios.

CATEGORY
        Genomic Sequence

INPUT
        El input es un archivo llamado "6-data.csv" ubicado en la carpeta data, no es introducido por el usuario

OUTPUT
        El programa retorna a pantalla un mensaje con los criterios bajo los que se seleccionaron los genes y enseguida
        imprime el nombre de estos

EXAMPLES
        Para kdy647 el contenido de AT es: ALTO
        Para jdg766 el contenido de AT es: MEDIO
        Para kdy533 el contenido de AT es: MEDIO
        Para hdt739 el contenido de AT es: BAJO
        Para hdu045 el contenido de AT es: MEDIO
        Para teg436 el contenido de AT es: MEDIO
        Los genes que pertenecen a Drosophila melanogaster o Drosophila simulans son:
	        ['kdy647', 'jdg766', 'kdy533']
        Los genes que tienen entre 90 y 110 bases de longitud son:
	        ['kdy647', 'kdy533', 'teg436']
        Los genes que presentan un contenido de AT menor al 50% y un nivel de expresion mayor a 200 son:
        	['teg436']
        Los genes cuyo nombre empieza con k o h y no pertencen a Drosophila melanogaster son:
        	['kdy533', 'hdt739', 'hdu045']

GITHUB
        https://github.com/JESUS-2120/Python_class/blob/master/src/Genes_Drosophila.py
'''

#Definimos la funcion contenido_AT, la cual calculara el contenido de AT de cada gene y en base 
#a este retorna un estado ya sea "ALTO", "BAJO" o "MEDIO", esta funcion tiene como parametro la 
#secuencia de DNA de cada gene
def contenido_AT(seq):
    cont = (seq.count("a") + seq.count("t"))/len(seq)
    if cont > .65:
        return "ALTO"
    elif cont < .45:
        return "BAJO"
    elif ((cont >= .45) and (cont <= .65)):
        return "MEDIO"

#Vamos a trabajar con un archivo llamado 6-data.csv ubicado en la carpeta data, por lo que lo abrimos
#y asignamos el contenido a file
file = open("../data/6-data.csv")

#Mediante allines le damos lectura a todas las líneas del documento 
all_lines = file.readlines()

#Y procedemos a cerrar el archivo
file.close()

#Creamos listas vacias para poder guardar los nombres de los genes segun cada criterio
Dm_o_Ds = []
longitud = []
at_cont = []
empieza = []

#Con un for damos lectura a cada linea de las leidas anteriormente
for line in all_lines:
    
    #Separamos las lineas con una coma mediantes split(",")
    spl = line.split(",")

    #Imprimimos en contenido de AT para cada gene del archivo con ayuda de la funcion contenido_AT
    print(f"Para {spl[2]} el contenido de AT es: {contenido_AT(spl[1])}")

    #Mediante un if verificamos la condicion que el gene sea de D. melanogaster o D. simulans, en caso de 
    #cumplirse el nombre de dicho gene se agrega a la lista correspondiente 
    if (spl[0] == "Drosophila melanogaster") or (spl[0] == "Drosophila simulans"):
       Dm_o_Ds.append(spl[2])

    #Mediante un if verificamos la condicion que el gene tenga una longitud de entre 90 y 110m pares de bases,
    #en caso de cumplirse el nombre de dicho gene se agrega a la lista correspondiente
    if (len(spl[1]) >= 90) and (len(spl[1]) <= 110):
       longitud.append(spl[2])

    #Mediante un if verificamos la condicion que el gene tenga un contenido de AT menor al 50% y un nivel de
    #expresion mayor a 200, en caso de cumplirse el nombre de dicho gene se agrega a la lista correspondiente
    if ((((spl[1].count("a") + spl[1].count("t"))/len(spl[1])) < .5) and (int(spl[3]) > 200)):
       at_cont.append(spl[2])

    #Mediante un if verificamos la condicion que el nombre del gene comience con k o h y que no sea de D. melanogaster,
    #en caso de cumplirse el nombre de dicho gene se agrega a la lista correspondiente
    if (((spl[2].startswith("k")) or (spl[2].startswith("h"))) and (spl[0] != "Drosophila melanogaster")):
       empieza.append(spl[2])


#Por ultimo imprimimos a pantalla los resultados con su descripcion correspondiente
print(f"Los genes que pertenecen a Drosophila melanogaster o Drosophila simulans son:\n\t{Dm_o_Ds}")
print(f"Los genes que tienen entre 90 y 110 bases de longitud son:\n\t{longitud}")
print(f"Los genes que presentan un contenido de AT menor al 50% y un nivel de expresion mayor a 200 son:\n\t{at_cont}")
print(f"Los genes cuyo nombre empieza con k o h y no pertencen a Drosophila melanogaster son:\n\t{empieza}")