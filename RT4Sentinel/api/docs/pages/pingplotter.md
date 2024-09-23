## PingPlotter

PingPlotter es una herramienta para monitorear, solucionar conflictos de red y realizar diagnósticos. También es utilizada para graficar los datos y las rutas de las señales sobre un periodo de tiempo.

### Ping

Ping es una de las más importantes herramientas de monitoreo de red que responde a la pregunta **¿El destinatario de red esta disponible? además te permite conocer la cantidad de paquetes, que son enviados al destinatario, perdidos y cuánto tiempo toma en ir y regresar.

### Traceroute

Traceroute contiene la ruta que el paquete tomo para llegar al destinatario, cada ruta es llamada **hop**

Para poder ejecutar las acciones es necesario conocer:

1. La dirección a la que se quiere realizar la consulta.
2. La unidad de tiempo, es el intervalo al que se envían los paquetes.
3. Una paleta de colores, que en la parte visual puede servir para identificar los periodos de tiempo en que la información tarda más o menos.

### RestAPI

PingPolotter tiene un servicio integrado de RestAPI el cual permite enviar alertas a otras Interfaces de usuarios. La aplicación permite una gran independencia en la forma de compartir información con otras aplicaciones. Nosotros, aunque no utilizamos todos los elementos, nos conviene usar la estructura siguiente, ya que con ella garantizamos el aprovechamiento máximo de la información que PingPlotter ofrece y evita la modificación futura de los métodos que consumen estos datos. 

```
json
{
  "alert": {
    "name": "{{AlertName}}",
    "failed_count": "{{ConditionFailedCount}}"
  },
  "host": {
    "host_id": "{{Host.HostID}}",
    "ip_address": "{{Host.IPAddress}}",
    "dns_name": "{{Host.HostName}}",
    "alias_name": "{{Host.AliasName}}",
    "preferred_name": "{{Host.PreferredName}}",
    "full_display_name": "{{Host.FullDisplayName}}"
  },
  "destination_host": {
    "host_id": "{{DestinationHost.HostID}}",
    "ip_address": "{{DestinationHost.IPAddress}}",
    "dns_name": "{{DestinationHost.HostName}}",
    "alias_name": "{{DestinationHost.AliasName}}",
    "preferred_name": "{{DestinationHost.PreferredName}}",
    "full_display_name": "{{DestinationHost.FullDisplayName}}"
  },
  "configuration": {
    "name": "{{ConfigName}}"
  },
  "agent": {
    "name": "{{AgentName}}"
  },
  "timestamps": {
    "current_time": "{{Now}}",
    "utc_time": "{{UtcNow}}"
  },
  "historical_data": "{{HistoryData}}",
}

```

### Resumen

PingPlotter tiene como finalidad presentar de forma amigable la presencia de latencia en los datos y la perdida de paquetes en la comunicación de las redes. Algunas de los errores más comunes a los que se les hace un seguimiento son:

- La perdida de respuesta con el objetivo
- Alta latencia en la respuesta
- Perdida de paquetes de datos
- Congestión en la red

Como alternativa gratuita existe MTR
