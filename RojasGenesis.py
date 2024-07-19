import csv
import random
import statistics
import math

trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernandez","Miguel Sanchez"
              "Isabel Gomez","Francisco Diaz","Elena Fernandez"]
trabajadoresconsueldo=[]
def asignarsueldos():
    for i in trabajadores:
        sueldo= random.randint(300000,2500000)
        trabajadoresconsueldo.append({"nombre": i,
                                     "Sueldo": sueldo})
    for i in trabajadoresconsueldo:
        print(i)

def clasificarsueldos():
    menor=[]
    mediano=[]
    superior=[]
    contadormen=0
    contadormay=0
    contadormed=0
    totaldesueldos=0
    for i in trabajadoresconsueldo:
        totaldesueldos+=float(i["Sueldo"])
        if float(i["Sueldo"])<800000:
            menor.append(i)
            contadormen+=1
        elif 800000<float(i["Sueldo"])<2000000:
            mediano.append(i)
            contadormed+=1
        elif float(i["Sueldo"])>2000000:
            superior.append(i)
            contadormay+=1
        else:
            print("Se ha producido un error")
        
    for i in menor:
        print(i)
    print(f"Sueldos menores a 800000. Total {contadormen}")
    for i in mediano:
        print(i)
    print(f"Sueldos entre 800000 y 2000000. Total {contadormen}")
    for i in superior:
        print(i)    
    print(f"Sueldos superiores a 2000000. Total {contadormen}")

    print(f"El total de sueldos es: {totaldesueldos}")
     

def verestadisticas():
    todoslossueldos=[]
    for i in trabajadoresconsueldo:
        todoslossueldos.append(i["Sueldo"])
        sueldoalto= max(todoslossueldos)
        sueldobajo=min(todoslossueldos)
        promediosueldo= statistics.mean(todoslossueldos)
        promediogeometrico= statistics.geometric_mean(todoslossueldos)
        print(f"El sueldo mas alto es: {sueldoalto}")
        print(f"El sueldo mas bajo es: {sueldobajo}")
        print(f"El promedio de sueldo es: {promediosueldo}")
        print(f"El promedio geometricos es: {promediogeometrico}")


def reportesueldos():
    reportesueldo=[]
    for i in trabajadoresconsueldo:
        descafp= float(i["Sueldo"])*0.12
        descsalud=float(i["Sueldo"])*0.07
        sueldoliquido= float(i["Sueldo"]) - descafp - descsalud
        reportesueldo.append({  "Nombre empleado": i["nombre"],
                                "Sueldo base": i["Sueldo"],
                                "Descuento salud":descsalud,
                                "Descuento AFP": descafp,
                                "Sueldo Liquido": sueldoliquido })
        
    with open("reportesueldos.csv", "w", newline="") as file:
        archivocsv= csv.writer(file)
        archivocsv.writerows(reportesueldo)
        
    print("Archivo creado exitosamente")
    print(reportesueldo)


def salirdelprograma():
    print("Finalizando programa ")
    print("Desarrollado por Genesis Rojas")
    print("RUT 28247399-2")
    exit()
while True:
    try:    
        opcion= int(input(""" 
                                1. Asignar sueldos aleatorios
                                2. Clasificar sueldos
                                3. Ver estadísticas.
                                4. Reporte de sueldos
                                5. Salir del programa\n"""))
        if opcion==1:
            asignarsueldos()
        elif opcion==2:
            clasificarsueldos()
        elif opcion==3:
            verestadisticas()
        elif opcion==4:
            reportesueldos()
        elif opcion==5:
            salirdelprograma()
        else:
            print("Ingrese una opcion valida")
    except Exception as ex:
        print(f"Tienes un error {ex}")