import os
#Direcciones IP
#VPN(Conexiones autorizadas)
vpn_autorizado = {"192.168.1.10", "192.168.1.11", "192.168.1.12",
                  "10.0.0.50", "10.0.0.51", "172.16.10.1"}
#ServidorCritico(Accesos detectados)
servidorCritico = {"192.168.1.10", "10.0.0.50", "192.168.1.55",
                   "172.16.10.10", "200.50.10.1", "10.0.0.51"}
#Lista negra(IPs maliciosas)
listaNegra ={"200.50.10.1", "172.16.10.10", "192.168.1.99", 
             "10.0.0.51", "8.8.8.8"}
#Módulo Detección de intrusos
def deteccionIntrusos():
    intruso = servidorCritico & listaNegra & vpn_autorizado
    print(f"IPs en riesgo alto: {len(intruso)}")
    print(intruso)
#Testeo del módulo
os.system("cls")
deteccionIntrusos()