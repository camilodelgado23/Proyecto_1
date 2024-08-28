# proyecto 1

## Por: Camilo Jose Delgado Bolaños - Jose Daniel Carrera - Jhon Sebastian arias soto 


#### Contexto 

Este Dataset fue extraido de la pagina web kaggle una plataforma de competencia de ciencia de datos y una comunidad en línea para científicos de datos y profesionales del aprendizaje automático de Google LLC.

Este Dataset contiene informacion sobre vuelos retrasados en el año 2019 con informacion sobre el clima, aereopuerto entre otros, para un mayor detalle puede visitar la pagina de donde salio en el siguiente enlace: https://www.kaggle.com/datasets/threnjen2019-airline-delays-and-cancellations?select=train.csv

#### Descripcion de columnas Dataset 

1. Información Temporal:

- **month:** Mes del año.
- **day_of_week:** Día de la semana.
- **dep_block_hist:** Bloque de salida.
2. **Variables de Destino (Target):**
- **dep_del15:** Indicador binario de un retraso de salida de más de 15 minutos (1 es sí).
3. **Características del Vuelo:**
- **distance group:** Grupo de distancia que volará la aeronave.
- **segment_number:** Número de segmento en el que se encuentra la aeronave para el día.
- **concurrent_flights:** Número de vuelos simultáneos que salen del aeropuerto en el mismo bloque de salida.
- **number_of_Sseats:** Número de asientos en la aeronave.
- **plane_age:** Antigüedad de la aeronave que sale.
4. **Características del Transportista y Aeropuerto:**
- **carrier_name:** Nombre del transportista.
- **airport_fligths_month:** Promedio de vuelos del aeropuerto por mes.
- **airline_fligths_month:** Promedio de vuelos de la aerolínea por mes.
- **airline_airport_fligths_month:** Promedio de vuelos por mes para la aerolínea y el aeropuerto.
- **avg_monthly_pass_airport:** Promedio de pasajeros para el aeropuerto de salida para el mes.
- **avg_monthly_pass_airline:** Promedio de pasajeros por aerolínea para el mes.
- **flt_attendants_per_pass**: Auxiliares de vuelo por pasajero de la aerolínea.
- **ground_serv_per_pass**: Empleados de servicio en tierra (mostrador de servicio) por pasajero de la aerolínea.
5. **Información Geográfica:**
- **departing_airport:** Aeropuerto de salida.
- **latitude:** Latitud del aeropuerto de salida.
- **longitude:** Longitud del aeropuerto de salida.
- **previous_airport:** Aeropuerto anterior del que salió la aeronave.
6. **Condiciones Meteorológicas:**
- **prcp:** Pulgadas de precipitación del día.
- **snow:** Pulgadas de nevadas del día.
- **snwd:** Pulgadas de nieve en tierra del día.
- **tmax:** Temperatura máxima del día.
- **awnd:** Velocidad máxima del viento del día


#### Herramientas Usadas

- Python: Python Scripting: Para automatizar tareas como la inserción de datos en bases de datos, y la exportación de archivos. Visual Studio Code (VS Code): Como entorno para escribir y ejecutar código Python.

- Jupyter Notebook: Para desarrollo interactivo de código, exploración de datos, y ejecución de scripts.
- Virtual Environment (venv): Para gestionar dependencias y aislar el entorno de desarrollo.

PostgreSQL:

- pgAdmin: Para gestión y administración de bases de datos PostgreSQL

- Git: Para control de versiones y seguimiento de cambios en el proyecto.

- GitHub: Para alojar el repositorio del proyecto, gestionar el control de versiones, y colaborar en el desarrollo del proyecto.

- Power BI: Para la visualizacion de Datos

#### Estructura del Repositorio
La estructura del repositorio es la siguiente

- **Database:**  Carpeta en donde se encuentran loa archivos relacionados con las acciones que interactúan directamente con la Base de Datos en postgreSQL
    - **carga_datasets:** Este es un notebook en el cual cargamos los Datasets a las tablas creadas en el postgreSQL
    - **conexion_DB: E**s un archivo .py en donde realizamos la conexión con nuestra Base de Datos
    - **tablas_dataset:** Es un notebook en donde creamos las tablas en la Database  para posteriormente cargar el dataset
    - **_int_.py:** es un directorio, Python reconoce ese directorio como un paquete, lo que permite que los módulos dentro de ese directorio se puedan importar usando la sintaxis de puntos (.).
- **Datasets:** Carpeta en donde se encuentran todos los Datasets utilizados
    - **train.csv:**  Es el dataset original que contiene información sobre vuelos que han sido trasados
    - **flights_limpio:** Es el dataset ya limpio listo para la vizualisacion de datos 
- **EDA:** Carpeta en donde se encuentran los archivos que leen el dataset en la base de datos
    - **flights_EDA:** Notebook en donde se realiza en EDA al dataset original
    - **flights_ transformado_EDA:** Notebook en donde se hace un eda al dataset ya limpio y transformado con el objetivo de sacar concluciones finales para seguir con la vizualisacion de datos en PowerBI
- **.gitignore:** archivo en donde colocaremos los archivos que no queremos que se suban a nuestro repositorio de GitHub, como lo es nuestro entorno virtual
- **.gitattributes:** Archivo donde almacenamos nuestros 2 datasets para que se puedan subir al repositorio de github sin problema 
- **readme.txt:** archivo en donde ira la descripción y el paso a paso para ejecucion del proyecto
- **requirements.txt:** archivo en donde estarán  todas las librerías/bibliotecas o instalaciones usadas en nuestro proyecto
- **Graficas.pdf:** Archivo pdf en donde3 se encuentran las vizualisaciones finales  en PowerBI 


#### Instrucciones para la ejecucion:

##### Requerimientos
Python: https://www.python.org/downloads/
PostgreSQL: https://www.postgresql.org/
PowerBI: https://www.microsoft.com/es-es/download/details.aspx?id=58494
pgAdmin(Opcional):https://www.pgadmin.org/


Clonamos el repositorio en nuestro entorno

```bash
  git clone https://github.com/camilodelgado23/Proyecto_1.git
```

Vamos al repositorio clonado

```bash
  cd Proyecto_1
```

Instalamos el entrono virtual donde vamos a trabajar

```bash
  python -m venv entorno
```

Iniciamos el entorno

```bash
  .\venv\Scripts\Activate
```

Instalamos las librerias necesarias almacenadas en el archivo requirements.txt

```bash
  pip install -r requirements.txt
```
Creamos la Base de Datos en PostgreSQL

https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2Ff89f0ee0-6df7-499d-965d-87a335bc5d80%2Fimage.png?table=block&id=5f9300c4-66f8-47f7-940d-1e04ad64223d&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=980&userId=&cache=v2


Creamos el archivo credentials.py donde almacenaremos las credenciales para conectarnos a la Base de Datos, puede seguir la siguiente estructura

```bash
    DB_USER = 'tu_usuario'
    DB_PASSWORD = 'tu_contraseña'
    DB_HOST = 'tu_host'
    DB_PORT = 'tu_puerto'
    DB_NAME = 'tu_base_datos'
```
Podemos probar si las credenciales son correctas ejecutando nuestro archivo conexion.py.

#### Para conectarnos a PowerBI 

Nos vamos a PowerBI y lo iniciamos, nos vamos a la pantalla de inicio y le damos a obtener datos donde buscaremos la opción de Base de datos PostgreSQL

https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2Fdf6ee716-6814-4a82-b5a9-f23ff54c2ca5%2Fimage.png?table=block&id=0358baac-ef87-4df1-b5c5-dd70a6b505c1&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1180&userId=&cache=v2

colocamos nuestras credenciales y seleccionamos la tabla en donde tenemos el dataset limpio 