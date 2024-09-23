# PythonAutomatization

Sistema de microservicios enfocada en la administración, envio y almacenamiento de alarmas a partir de la comunicación entre diferentes sistemas.

## Instalación

Todo el sistema se desarrollo con Python 3.12 y diferentes librerias para el desarrollo rápido de los sistemas deseados, en la secció de recursos se puede ahondar más sobre qué recursos se utilizan en cada uno de los servicios. En esta sección se presenta la forma en que se puede utilizar este sistema de forma local.

### Pre-requisitos

- Docker

#### Aplicaciones de terceros

Este endpoint busca funcionar como puerta para levantar alarmas obtenidas de aplicaciones externas. Por el momento, la aplicación con la que se ha provado el funcionamiento es PingPlotter por lo que se recomienda instalar si va a probar la aplicación.

---

#### Clonar el proyecto

Si usted no ha clonado este proyecto ejecute el siguiente comando en la ruta que desee instalar la aplicación

`git clone https://github.com/RT4DevSpace/PythonAutomatization.git`

---

#### Desarrollo

Si usted es desarrollador trabaje sobre la rama dev y genere su propia rama. Para probar sus cambios ejecute docker-compose para probar sus cambios. 

#### Producción

Si usted solo quiere probar la herramienta, ejecute el siguiente comando

`docker-compose up --build `

## Recursos

[Documentacion](RT4Sentinel\api\docs\pages\documentacion.md)
