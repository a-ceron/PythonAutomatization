# Routes

Las aplicaciones RestAPI pueden crecer de tal forma que se puede volver insostenible la cantidad de rutas y lineas de código presente. Una forma en la que se puede disminuir la complejidad es al crear rutas particulares. La clasificación de estas rutas dependerán de la arquitectura elegida o de la lógica del negocio. 

Para este proyecto se eligió la separación por funcionalidad de la siguiente forma:

- **alarmas**: Contiene la lógica para leer y procesar las alarmas de servicios externos como PingPlotter.
- **tickets**: Contiene la lógica para crear, actualizar y cerrar tickets relacionados con las alarmas.
- **users**: Contiene la lógica para crear, actualizar y borrar usuarios a los que se les asignarán los tickets generados.
- **webhooks**: Contiene la lógica para recibir actualizaciones por parte de los servicios de comunicación como WhatsApp, Telegram o Zendesk.

Para mayor contenido visitar las siguientes referencias

* [R]()oute: Alarmas
* [R]()oute: Users
* [R]()oute: Tickets
* [R]()oute: Webhooks
