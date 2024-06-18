#Se importan las bibliotecas y el archivo .py con las funciones 
import csv
import funcionesactividad as funciones
import time
opcionmainmenu=0
listatrabajadores=[]
#Genera el archivo csv para luego agregar los datos
titulo=['Trabajador', 'Cargo', 'Sueldo bruto', 'Descuento Salud', 'Descuento AFP', 'Sueldo liquido']
with open('Trabajadores.csv', 'w', newline='', encoding='UTF-8') as archivo_csv:
    escritor_csv=csv.writer(archivo_csv);
    escritor_csv.writerow(titulo)
print("\n***Bienvenido a la empresa***\n");
#Comienza el programa 
while opcionmainmenu!=4 or flag==True:
    funciones.menu()
    try:
        opcionmainmenu=int(input("Ingrese una opcion: "));
    except:
        print("\nError, elija un numero valido\n")
    else:
    #Opcion 1: Registrar un trabajador
        if opcionmainmenu==1:
            print("\nRegistrar trabajador\n")
            nombreapellido=input("Ingrese El Nombre y Apellido del trabajor: ");
            listatrabajadores.append(nombreapellido)
            cargo=input("\nIngrese El Cargo del Trabajor: ");
            try:
                sueldobruto=int(input("\nIngrese el sueldo bruto del trabajor: "));
            except:
                print("ERROR, intentelo otra vez!!")
            else:
                descuentosalud=(sueldobruto*0.07).__round__()
                descuentoafp=(sueldobruto*0.12).__round__()
                sueldoliquido=sueldobruto-descuentoafp-descuentosalud
        #Añade los datos del trabajador(a) al csv 
            listatrabajador=[nombreapellido,cargo,sueldobruto,descuentosalud,descuentoafp,sueldoliquido]
            with open('Trabajadores.csv', 'w', newline='', encoding='UTF-8') as archivo_csv:
                escritor_csv=csv.writer(archivo_csv);
                escritor_csv.writerow(titulo);
                escritor_csv.writerow(listatrabajador);
    #Opçion 2: Listar a los trabajadores de la empresa
        elif opcionmainmenu==2:
            funciones.mostrartrabajdores(listatrabajadores);
    #Opcion 3: Imprimir la planilla de trabajadores
        elif opcionmainmenu==3:
            funciones.planilla();
    #Opcion 4: Salir del programa
        elif opcionmainmenu==4:
            funciones.Animacion_salir()
            flag=False
    #Si se elije una opcion inexistente
        else:
            print("Error, Ingrese una opcion valida");
    
