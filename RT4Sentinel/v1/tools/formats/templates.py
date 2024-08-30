# Formatos de mensajes de texto por nivel de importancia y longitud
formatos_mensajes = {
    'bajo': {
        'corto': "[Bajo] Recordatorio: El servidor de pruebas está en mantenimiento programado desde las 10 AM. No se requiere ninguna acción.",
        'medio': "[Bajo] Notificación: El servidor de pruebas inició su mantenimiento programado a las 10 AM. Estará fuera de servicio hasta las 12 PM. No es necesario tomar medidas.",
        'largo': "[Bajo] Atención: El servidor de pruebas comenzó su mantenimiento programado hoy a las 10 AM y se espera que esté fuera de servicio hasta las 12 PM. Este mantenimiento es parte de nuestras actualizaciones mensuales rutinarias y no se espera que afecte otros sistemas. No se requiere ninguna acción en este momento, pero puedes contactar al equipo de soporte si tienes alguna pregunta."
    },
    'medio': {
        'corto': "[Medio] Alerta: Error en la sincronización de datos. Revisar logs.",
        'medio': "[Medio] Alerta: Se detectó un error en la sincronización de datos a las 11:15 AM. Por favor, revisa los registros del sistema para más detalles y confirma que todo está en orden.",
        'largo': "[Medio] Alerta Importante: Un error de sincronización de datos se detectó a las 11:15 AM. Parece que hay un problema con la integración del sistema de bases de datos que puede afectar a la transferencia de información entre los servidores. Se requiere que revises los registros del sistema para identificar el problema y asegurarte de que todas las conexiones estén funcionando correctamente. Contacta al equipo de soporte si necesitas asistencia adicional."
    },
    'alto': {
        'corto': "[Alto] Urgente: Falla total del sistema. Necesita atención inmediata.",
        'medio': "[Alto] Urgente: Falla total del sistema a las 2:30 PM. Se requiere intervención inmediata para restablecer los servicios afectados.",
        'largo': "[Alto] Urgente: Falla crítica del sistema detectada a las 2:30 PM. Todo el sistema se encuentra fuera de servicio, afectando múltiples servicios críticos para la operación. Es imperativo que se realicen acciones inmediatas para diagnosticar y resolver el problema. Los equipos de infraestructura y soporte están alertados, y se espera una actualización sobre el progreso cada 15 minutos. Todos los técnicos disponibles deben priorizar esta incidencia hasta que se resuelva completamente."
    }
}

