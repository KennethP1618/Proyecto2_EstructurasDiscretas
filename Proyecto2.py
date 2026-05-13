import os
from datetime import datetime
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
    print("\n")
#Módulo de mensaje de error
def FuncionError():
    os.system("cls")
    print("EL VALOR INGRESADO PUEDE CONTENER ERRORES, PORFAVOR, COMPRUEBE NUEVAMENTE.")
    input("Presione ENTER para continuar...")
#Módulo de descarga del informe completo
def descargarInforme():
    # Operaciones
    intruso       = servidorCritico & listaNegra
    anomaly       = (listaNegra & vpn_autorizado) - servidorCritico
    no_autorizado = servidorCritico - vpn_autorizado
    total         = servidorCritico | listaNegra | vpn_autorizado

    # Ruta a Descargas
    fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    ruta  = os.path.join(os.path.expanduser("~"), "Downloads", f"informe_{fecha}.txt")

    with open(ruta, "w", encoding="utf-8") as f:
        f.write("==== INFORME DE VULNERABILIDADES DE RED ====\n")
        f.write(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        # Detección de intrusos
        f.write("*" * 80 + "\n")
        f.write("INTERSECCIÓN\n")
        f.write(f"IPs en riesgo alto: {len(intruso)}\n")
        f.write("Lista de IPs detectadas:\n")
        for ip in intruso:
            f.write(f"  {ip}\n")
        f.write("*" * 80 + "\n\n")

        # Acceso no autorizado
        f.write("*" * 80 + "\n")
        f.write("DIFERENCIA\n")
        f.write("Acceso no autorizado\n")
        f.write(f"IPs fuera de VPN: {len(no_autorizado)}\n")
        f.write("Lista de IPs detectadas:\n")
        for ip in no_autorizado:
            f.write(f"  {ip}\n")
        f.write("*" * 80 + "\n\n")

        # Monitoreo global
        f.write("*" * 80 + "\n")
        f.write("UNIÓN\n")
        f.write("Monitoreo Global\n")
        f.write(f"Total IPs detectadas: {len(total)}\n")
        f.write("Lista de IPs detectadas:\n")
        for ip in total:
            f.write(f"  {ip}\n")
        f.write("*" * 80 + "\n\n")

        # Anomalía de seguridad
        f.write("*" * 80 + "\n")
        f.write("DIFERENCIA SIMÉTRICA\n")
        f.write(f"Anomalías detectadas: {len(anomaly)}\n")
        if anomaly == set():
            f.write("Anomalías no detectadas.\n")
        else:
            f.write("Lista de IPs detectadas:\n")
            for ip in anomaly:
                f.write(f"  {ip}\n")
        f.write("*" * 80 + "\n")

    print(f"Informe descargado en:\n{ruta}")
#Main
#Variables para los bucles
flag = True
flag_opciones = True
flag_repetir = True
#Menú
while(flag):
    #Control de opciones
    while flag_opciones:
        try:
            os.system("cls")
            print("==== INFORME DE VULNERABILIDAES DE RED=====")
            print("Escoja la opción a ejecutar:\n" \
            "1. Detección de intrusos\n" \
            "2. Acceso no autorizado\n" \
            "3. Listado de todas las IPs\n" \
            "4. Anomalía de seguridad\n" \
            "5. Ver informe completo\n" \
            "6. Descargar informe completo\n" \
            "7. Salir\n")
            opcion = int(input("Ingrese una opción --> "))
            flag_opciones = False
        except:
            FuncionError()
    #Intersección
    if (opcion == 1):
        os.system("cls")
        deteccionIntrusos()
    #Diferencia
    elif (opcion == 2):
        os.system("cls")
        accesoNoAutorizado()
    #Unión
    elif (opcion == 3):
        os.system("cls")
        monitoreoGlobal()
    #Diferencia simétrica
    elif (opcion == 4):
        os.system("cls")
        anomaliaSeguridad()
    #Mostrar todas las operaciones
    elif (opcion == 5):
        os.system("cls")
        deteccionIntrusos()
        accesoNoAutorizado()
        monitoreoGlobal()
        anomaliaSeguridad()
    #Manejo de errores
    elif (opcion == 6):
        os.system("cls")
        descargarInforme()
    #Salida
    elif(opcion == 7):
        flag = False
        break
    #Manejo de errores
    else:
        FuncionError()
    #En caso de realizar otras operaciones
    flag_repetir = True
    while(flag_repetir):
        print("¿DESEA HACER OTRAS OPERACIONES?")
        try:
            repetir = int(input("1. SI\n2. NO\nIngrese una opción --> "))
            if (repetir == 2):
                flag = False
                flag_repetir = False
            elif (repetir == 1):
                flag_opciones = True
                flag_repetir = False
            else:
                FuncionError()
        except:
            FuncionError()
os.system("cls")
print("PROGRAMA FINALIZADO...")