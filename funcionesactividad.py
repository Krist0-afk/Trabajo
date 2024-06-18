import csv
import time
#Declarar variables
descuentosalud=0
descuentoafp=0
listatrabajadores=[]
descuentosalud=0
descuentoafp=0
nombre=""
opcionmainmenu=0
flag=True
#Funcion para mostrar el menu al usuario
def menu():
    print("Herramientas empresa");
    print("=========================\n1.- Registrar trabajador\n2.- Mostrar los trabajdores\n3.- Imprimir planilla de sueldos\n4.- Salir del programa\n=========================");
#Funcion decorativa para cuando el usuario esta saliendo del programa
def Animacion_salir():
    print("Saliendo del programa",end="")
    for h in range(3):
        print(".",flush=True,end="")
        time.sleep(0.5)
#Funcion para mostrar los datos de los trabajadores 
def planilla():
    pregunta = input("¿Desea ver la planilla de un solo trabajador?(si/no) ").lower()
    if pregunta == "si":
        # Muestra la lista de trabajadores
        for trabajador in listatrabajadores:
            print(trabajador, "\n")
        # Busca un trabajador
        nombreplani = input("Ingrese el Nombre del trabajador para poder ver la planilla: ")
        with open('Trabajadores.csv', 'r', encoding='UTF-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            print("")
            for fila in lector_csv:
                if fila['Trabajador'] == nombreplani:
                #Si encuentra el trabajador 
                    print("Trabajador | Cargo | Sueldo bruto | Descuento Salud | Descuento AFP | Sueldo liquido")
                    fnombre = fila['Trabajador']
                    fcargo = fila['Cargo']
                    fsueldobruto = int(fila['Sueldo bruto'])
                    fdescuentosalud = int(fila['Descuento Salud'])
                    fdescuentoafp = int(fila['Descuento AFP'])
                    fsueldoliquido = int(fila['Sueldo liquido'])
                    print(f"{fnombre} | {fcargo} | {fsueldobruto} | {fdescuentosalud} | {fdescuentoafp} | {fsueldoliquido}")
                #Si no lo encuentra
                else:
                    print("No se encontro el trabajador")
                    break;
    elif pregunta == "no":
        with open('Trabajadores.csv', 'r', encoding='UTF-8') as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            print("Trabajador | Cargo | Sueldo bruto | Descuento Salud | Descuento AFP | Sueldo liquido")
            for fila in lector_csv:
                fnombre = fila['Trabajador']
                fcargo = fila['Cargo']
                fsueldobruto = int(fila['Sueldo bruto'])
                fdescuentosalud = int(fila['Descuento Salud'])
                fdescuentoafp = int(fila['Descuento AFP'])
                fsueldoliquido = int(fila['Sueldo liquido'])
                print(f"{fnombre} | {fcargo} | {fsueldobruto} | {fdescuentosalud} | {fdescuentoafp} | {fsueldoliquido}")
#Funcion para mostrar los trabajadores agregados
def mostrartrabajdores(listatrabajadores):
    print("========================================\n")
    for trabajador in listatrabajadores:
        print("-",trabajador, "\n");
    print("========================================\nEstos son todos los nombres de los trabajadores ingresados\n");
def escribir_csv():
    with open('Trabajadores.csv', 'w', newline='', encoding='UTF-8') as archivo_csv:
        escritor_csv=csv.writer(archivo_csv);
