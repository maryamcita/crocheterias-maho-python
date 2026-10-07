# 🧶 Crocheterias Maho — Análisis de Datos en Python (Momento 2)

**Asignatura:** Nuevas Tecnologías 3 — CESDE  
**Profesor:** Santiago  
**Proyecto Integrador:** Aplicación de Análisis de Datos en Python para Crocheterias Maho  

---

## 📌 Descripción del Proyecto

Este repositorio contiene la solución completa para el **Momento 2** del proyecto integrador **Crocheterias Maho**. Consiste en un sistema de procesamiento y análisis de datos en Python estructurado con:

1. **Entorno Virtual (`venv`)**: Para el aislamiento de dependencias.
2. **Datasets CSV Relacionados (`data/`)**: `productos.csv` (catálogo con >50 registros) y `pedidos.csv` (transacciones con >50 registros), que contienen datos deliberadamente inconsistentes (valores nulos, espacios en blanco extra, formato de moneda `$`, variaciones de mayúsculas/minúsculas).
3. **Módulo de Preprocesamiento (`preprocesamiento.py`)**: Funciones reutilizables para la carga, tratamiento de valores nulos, estandarización de texto y conversión/limpieza de precios numéricos.
4. **Script Principal de Análisis (`analisis.py`)**: Ejecuta el preprocesamiento, realiza la combinación de conjuntos de datos (`pd.merge`), agrupaciones (`groupby`), filtrado y responde preguntas estratégicas de negocio.
5. **Git Flow**: Estructura de ramas (`main`, `develop`, `feature/...`, `release/analisis-v1`).

---

## 🚀 Guía de Instalación y Ejecución

Sigue estos pasos para configurar el entorno y ejecutar la aplicación en tu computador local.

### 1. Clonar el repositorio
```bash
git clone https://github.com/maryamcita/crocheterias-maho-python.git
cd crocheterias-maho-python
```

### 2. Configurar el Entorno Virtual (`venv`)

#### En Windows (PowerShell / CMD):
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows PowerShell
.\venv\Scripts\Activate.ps1

# O en Windows CMD:
.\venv\Scripts\activate.bat
```

#### En macOS / Linux:
```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

### 3. Instalar las dependencias del proyecto
Una vez activado el entorno virtual (`(venv)` debe aparecer al inicio de la consola):
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el script principal de análisis
```bash
python analisis.py
```

---

## 📊 Estructura del Proyecto

```text
crocheterias-maho-python/
│
├── data/
│   ├── productos.csv           # Catálogo de productos (>50 registros con datos crudos)
│   └── pedidos.csv             # Histórico de ventas y pedidos (>50 registros con datos crudos)
│
├── preprocesamiento.py         # Módulo con funciones reutilizables de limpieza
├── analisis.py                 # Script principal con la lógica de negocio y merge
├── requirements.txt            # Dependencias del proyecto (pandas)
├── .gitignore                  # Exclusión de venv/ y archivos basura
└── README.md                   # Documentación y guía del proyecto
```

---

## 📚 Respuestas a Preguntas de Evaluación (Momento 2)

### 1. ¿Qué es un DataFrame y por qué lo usamos?
Un **DataFrame** es una estructura de datos bidimensional (organizada en filas y columnas) proporcionada por la librería **Pandas** en Python, similar a una hoja de cálculo de Excel o una tabla en una base de datos relacional. 

**¿Por qué lo usamos en este proyecto?**
- Permite manipular, filtrar, limpiar y agrupar grandes volúmenes de datos de manera altamente eficiente con pocas líneas de código.
- Facilita la realización de operaciones complejas como uniones entre archivos (`pd.merge`) y agregaciones avanzadas (`groupby`).
- Soporta la integración nativa de funciones vectorizadas y manejo directo de valores nulos o tipos de datos inconsistentes.

### 2. ¿Por qué usamos entornos virtuales (`venv`)?
Un **entorno virtual** es un espacio aislado en el sistema que contiene su propia instalación de ejecutable de Python y sus propias librerías instaladas mediante `pip`.

**¿Por qué es indispensable?**
- **Aislamiento de Dependencias**: Evita conflictos entre las versiones de librerías requeridas por distintos proyectos en la misma máquina (por ejemplo, evitar que un proyecto que use Pandas 1.x interfiera con otro que use Pandas 2.x).
- **Reproducibilidad**: Garantiza que cualquier integrante del equipo o docente pueda clonar el repositorio, ejecutar `pip install -r requirements.txt` y obtener exactamente las mismas versiones probadas sin alterar el sistema global.
- **Limpieza del Repositorio**: Evita subir librerías pesadas a GitHub mediante el uso de `.gitignore` para ignorar la carpeta `venv/`.

---

## 🌿 Flujo de Ramas (Git Flow)

- `main`: Rama de producción estable.
- `develop`: Rama de integración principal.
- `feature/preprocesamiento-y-datos`: Rama de desarrollo para el módulo de limpieza y datos.
- `release/analisis-v1`: Rama de preparación de la entrega final v1.0.
