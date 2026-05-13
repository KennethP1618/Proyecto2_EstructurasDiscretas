# Sistema de Detección de Vulnerabilidades en Redes mediante Teoría de Conjuntos utilizando Python 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Estado](https://img.shields.io/badge/Estado-Completado-green) ![Área](https://img.shields.io/badge/Área-Seguridad%20en%20Redes-red)

> Proyecto académico que aplica operaciones de teoría de conjuntos para el análisis y detección de vulnerabilidades en redes de computadoras.

---

## Descripción

Este sistema simula un entorno de monitoreo de seguridad en redes, donde se gestionan tres conjuntos principales de direcciones IP:

| Conjunto | Descripción |
|---|---|
| `vpn_autorizado` | IPs con acceso autorizado a la red mediante VPN |
| `servidorCritico` | IPs que han accedido al servidor crítico |
| `listaNegra` | IPs catalogadas como maliciosas o sospechosas |

Mediante operaciones de teoría de conjuntos, el sistema identifica intrusos, accesos no autorizados y anomalías de seguridad, generando un informe descargable con los resultados.

---

## Operaciones de Conjuntos Aplicadas

### 1. Detección de Intrusos — Intersección (A ∩ B)
Identifica las IPs que están simultáneamente en el servidor crítico **y** en la lista negra.

```
intruso = servidorCritico ∩ listaNegra
```

### 2. Acceso No Autorizado — Diferencia (A - B)
Detecta IPs que accedieron al servidor crítico pero **no** están autorizadas en la VPN.

```
no_autorizado = servidorCritico - vpn_autorizado
```

### 3. Monitoreo Global — Unión (A ∪ B ∪ C)
Consolida todas las IPs conocidas en los tres conjuntos.

```
total = servidorCritico ∪ listaNegra ∪ vpn_autorizado
```

### 4. Anomalía de Seguridad — Diferencia de conjuntos
Detecta IPs que están en la lista negra y en la VPN, pero que no han tocado el servidor crítico — comportamiento anómalo.

```
anomaly = (listaNegra ∩ vpn_autorizado) - servidorCritico
```

---

## Requisitos

- Python 3.x
- No requiere librerías externas — solo módulos estándar (`os`, `datetime`)

---

## Instalación y Uso

**1. Descarga el repositorio:**
> Visita el repositorio en GitHub: [Proyecto2_EstructurasDiscretas](https://github.com/KennethP1618/Proyecto2_EstructurasDiscretas) → botón verde **`Code`** → **`Download ZIP`** → extrae la carpeta en tu computadora.

**2. Ejecuta el programa:**
> Abre la carpeta extraída, busca el archivo `main.py` y ejecútalo con doble clic.

> Si el doble clic no funciona, haz clic derecho sobre `main.py` → **"Abrir con"** → **Python**.

**3. Selecciona una opción del menú:**
```
==== INFORME DE VULNERABILIDADES DE RED =====
Escoja la opción a ejecutar:
1. Detección de intrusos
2. Acceso no autorizado
3. Listado de todas las IPs
4. Anomalía de seguridad
5. Ver informe completo
6. Descargar informe completo
7. Salir
```

> La opción **6** genera un archivo `.txt` con el informe completo y lo descarga automáticamente en la carpeta **Descargas** del sistema.

---

## Estructura del Proyecto

```
📦 proyecto/
 ┣ 📄 main.py         # Código principal del sistema
 ┗ 📄 README.md       # Documentación del proyecto
```

---

## Ejemplo de Salida

```
********************************************************************************
INTERSECCIÓN
IPs en riesgo alto: 3
Lista de IPs detectadas:
  200.50.10.1
  172.16.10.10
  10.0.0.51
********************************************************************************
```

---

## Conceptos Teóricos

Este proyecto aplica los siguientes conceptos de **Teoría de Conjuntos**:

- **Unión (∪):** Elementos que pertenecen a al menos uno de los conjuntos.
- **Intersección (∩):** Elementos comunes entre dos o más conjuntos.
- **Diferencia (-):** Elementos que pertenecen a un conjunto pero no al otro.
- **Diferencia Simétrica (△):** Elementos que pertenecen a uno u otro conjunto, pero no a ambos.

---
