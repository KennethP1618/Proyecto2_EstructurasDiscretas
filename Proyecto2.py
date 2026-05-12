import os
#Direcciones IP
#VPN(Conexiones autorizadas)
vpn_autorizado = {"192.168.1.10", "192.168.1.11", "192.168.1.12",
                  "10.0.0.50", "10.0.0.51", "172.16.10.1"}
#ServidorCritico(Accesos detectados)
servidorCritico = {"192.168.1.10", "10.0.0.50", "192.168.1.55",
                   "172.16.10.10", "200.50.10.1", "10.0.0.51"}
#Lista negra(IPs maliciosas)
listaNegra = {"200.50.10.1", "172.16.10.10", "192.168.1.99", 
             "10.0.0.51", "8.8.8.8"}
#Módulo Detección de intrusos
def deteccionIntrusos():
    intruso = servidorCritico & listaNegra
    #Salida
    print("\n")
    print("*" * 80)
    print("INTERSECCIÓN")
    print(f"IPs en riesgo alto: {len(intruso)}")
    #Salida de las IPs
    print("Lista de IPs detectadas:")
    for interseccion in intruso:
        print(interseccion)
    print("*" * 80)
    print("\n")
#Módulo Anomalía de seguridad
def anomaliaSeguridad():
    anomaly = (listaNegra & vpn_autorizado) - servidorCritico
    print("\n")
    print("*" * 80)
    print("DIFERENCÍA SIMÉTRICA")
    print(f"Anomalías detectadas: {len(anomaly)}")
    #En caso de no detectar anomalías
    if (anomaly == set()):
        print("Anomalías no detectadas.")
    #Anomalías encontradas
    else:
        print("Lista de IPs detectadas:")
        for diferencia_simetrica in anomaly:
            print(diferencia_simetrica)
    print("*" * 80)
    print("\n")
#Módulo de acceso no autorizado
def accesoNoAutorizado():
    no_autorizado= servidorCritico - vpn_autorizado
    print("\n")
    print("*" * 80)
    print("DIFERENCIA")
    print("Acceso no autorizado")
    print(f"IPs fuera de vpn {len(no_autorizado)}")
    #Salida de las IPs
    print("Lista de Ips detectadas:")
    for diferencia in no_autorizado:
        print(diferencia)
    print("*" * 80)
    print("\n")
#Módulo de monitoreo global, muestra todas las IPs
def monitoreoGlobal():
    total= servidorCritico | listaNegra | vpn_autorizado
    print("*" * 80)
    print("UNIÓN")
    print("Monitoreo Global")
    print(f"Total Ips Detectadadas: {len(total)}")
    #Salida de las IPs
    print("Lista de Ips detectadas:")
    for union in total:
        print(union)
    print("*" * 80)
#Main
#Menú
flag = True
while(flag):
    os.system("cls")
    print("==== INFORME DE VULNERABILIDAES DE RED=====")
    print("Escoja la opción a ejecutar:\n" \
    "1. Detección de intrusos\n" \
    "2. Acceso no autorizado\n" \
    "3. Monitoreo global\n" \
    "4. Anomalía de seguridad\n" \
    "5. Ver informe completo\n" \
    "6. Descargar informa completo\n" \
    "7. Salir\n")
    opcion = int(input("Ingrese una opción --> "))
    #Opciones
    if (opcion == 1):
        os.system("cls")
        deteccionIntrusos()
    elif (opcion == 2):
        os.system("cls")
        accesoNoAutorizado()
    elif (opcion == 3):
        os.system("cls")
        monitoreoGlobal()
    elif (opcion == 4):
        os.system("cls")
        anomaliaSeguridad()
    elif (opcion == 5):
        os.system("cls")
        monitoreoGlobal()
    elif (opcion == 6):
        os.system("cls")
        print("TRABAJO EN PROCESO...")
    elif(opcion == 7):
        flag = False
    else:
        print("SE HA INGRESADO UN VALOR NULO. INTÉNTELO NUEVAMENTE...")
    #En caso de realizar otras operaciones
    print("¿DESEA HACER OTRAS OPERACIONES?")
    repetir = int(input("1. SI\n2. NO\nIngrese una opción --> "))
    if (repetir == 2):
        flag = False
os.system("cls")
print("PROGRAMA FINALIZADO...")