# Users

Un usuario es aquel individuo que usa de forma habitual un servicio. Para esta aplicación se han de considerar dos usuairos principales:

- Cliente: Es aquel interesado en conocer cualquier fallo relacionado con su comunicación y si ha sido resuelto de forma exitosa
- Worker: Es aquel interesado en conocer cualquier fallo pues será el encargado en resolverlo y actualizar el status del problema. Aquí habrá una subdivición:
  - A1: En la primera linea se tiene a cualquier trabajador cuyas metas sean solucionar problemas
  - A2: Cuando un ticket no ha sido solucionado y ha estado abierto por mucho tiempo pasa a usuarios de segundo nivel, que tendrán que tomar mayores acciones para resolver el ticket.

## Rutas

Para interactuar con las herramientas de usuario se debe usar la siguiente ruta

- [POST] Para crear nuevos usuarios
  - `/api/v1/db/user`
- [GET] Para obtener todos los usuarios
  - `/api/v1/db/users`
- [GET] Para obtener un usuarios
  - `/api/v1/db/user/<pk>`

## Estructuras

Para la petición POST es necesario incluir el siguiente contenido en el cuerpo:

```json
{
    "name": str -> Nombre del usuario
    "email": str -> Correo electronico
    "phone": str -> Número telefónico laboral
  
    "is_agent": bool -> Define el nivel del usuaior, False A1, True A2
}
```
