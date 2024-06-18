import csv

#Encabezado de la tabla
lista=['Nombre','Edad','Comuna'];
#Las filas de la tabla
matriz=[
    ['Esteban',25,'Santiago'],
    ['Maria',30,'Valparaiso'],
    ['Carlos',13,'Puerto Montt'],
    ['Sigrid',25,'Santiago'],
    ['Daniela',30,'La Cisterna'],   
    ['Aylen',22,'La Florida']
];

#Crear el contexto para abrir un nuevo archivo
with open('nuevo_archivo.csv', 'r+', newline='', encoding='UTF-8') as archivo_csv:
    escritor_csv=csv.writer(archivo_csv);
    #Escribir la variable lista en el archivo
    escritor_csv.writerow(lista);
    #Escribir la variable matriz en el archivo
    escritor_csv.writerows(matriz);

#Leer el archivo csv
with open('nuevo_archivo.csv', 'r', encoding='UTF-8') as archivo_csv:
    lector_csv=csv.reader(archivo_csv);
    for x in lector_csv:
        print(x)

with open('nuevo_archivo.csv', 'r', encoding='UTF-8') as archivo_csv:
    lector_csv=csv.DictReader(archivo_csv);
    for fila in lector_csv:
        nombre=fila['Nombre']
        edad=int(fila['Edad'])
        comuna=fila['Comuna']
        if edad>=18:
            rango="Es mayor de edad"
        else:
            rango="Es menor de edad"
        print(f"{nombre} tiene {edad} años, vive en {comuna} y {rango}")