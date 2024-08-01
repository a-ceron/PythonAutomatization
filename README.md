# PythonAutomatization
<<<<<<< HEAD

Sistema de microservicios enfocada en la administración, envio y almacenamiento de alarmas a partir de la comunicación entre diferentes sistemas.

## Instalación

Todo el sistema se desarrollo con Python 3.12 y diferentes librerias para el desarrollo rápido de los sistemas deseados, en la secció de recursos se puede ahondar más sobre qué recursos se utilizan en cada uno de los servicios. En esta sección se presenta la forma en que se puede utilizar este sistema de forma local.

### Pre-requisitos

- PingPlotter
- Docker
- Clonar este proyecto

---

#### Clonar el proyecto

Si usted no ha clonado este proyecto ejecute el siguiente comando en la ruta que desee instalar la aplicación

`git clone https://github.com/RT4DevSpace/PythonAutomatization.git`

---



#### Desarrollo

Si usted quiere contribuir al desarrollo de este proyecto debe seguir los siguientes pasos.

EN DESARROLLO...

#### Pruebas

Si usted quiere evaluar que el sistema se ejecute de forma correcta ejecute el siguiente comando, que realiza una serie de tareas para evaluar los diferentes métodos que existen en la aplicación.

EN DESARROLLO...

#### Producción

Si usted solo quiere probar la herramienta, ejecute el siguiente comando

`docker-compose up --build `

## Recursos

[FastAPI](./docs/pages/fastapi.md)

[TeleBot](/docs/pages/telebot.md)

[DataBase](./docs/pages/database.md)
=======
Desarrollo de codigo Python para automatizar procesos, notificaciones y alarmas; además de dar un seguimiento a los flujos de trabajo


## PingPlotter
PingPlotter es una herramienta para monitorear, solucionar conflictos de red y realizar diagnósticos. También es utilizada para graficar los datos y las rutas de las señales sobre un periodo de tiempo.

### Ping
Ping es una de las más importantes herramientas de monitoreo de red que responde a la pregunta **¿El destinatario de red esta disponible? además te permite conocer la cantidad de paquetes, que son enviados al destinatario, perdidos y cuánto tiempo toma en ir y regresar.

### Traceroute
Traceroute contiene la ruta que el paquete tomo para llegar al destinatario, cada ruta es llamada **hop**


Para poder ejecutar las acciones es necesario conocer:
1. La dirección a la que se quiere realizar la consulta.
1. La unidad de tiempo, es el intervalo al que se envían los paquetes.
1. Una paleta de colores, que en la parte visual puede servir para identificar los periodos de tiempo en que la información tarda más o menos.

### Resumen
PingPlotter tiene como finalidad presentar de forma amigable la presencia de latencia en los datos y la perdida de paquetes en la comunicación de las redes. Algunas de los errores más comunes a los que se les hace un seguimiento son:
- La perdida de respuesta con el objetivo
- Alta latencia en la respuesta
- Perdida de paquetes de datos
- Congestión en la red

Como alternativa gratuita existe MTR

>>>>>>> 837ceff4354b93b8f65196707585af684266a328
