BASE_CONOCIMIENTO = {
    "1": {
        "nombre": "Redes e Internet",
        "causas": {
            "Problema con DNS": {
                "sintomas": {
                    "hay_wifi": 2,
                    "hay_ip": 1,
                    "no_abren_dominios": 3,
                    "servidor_no_responde": 0
                },
                "solucion": "Comprobar la resolución DNS y la configuración del servidor DNS."
            },
            "Falla de conectividad": {
                "sintomas": {
                    "hay_wifi": 0,
                    "hay_ip": -2,
                    "no_abren_dominios": 1,
                    "servidor_no_responde": 2
                },
                "solucion": "Comprobar la conexión, la puerta de enlace y la disponibilidad de la red."
            },
            "Servidor inaccesible": {
                "sintomas": {
                    "hay_wifi": 2,
                    "hay_ip": 2,
                    "no_abren_dominios": 1,
                    "servidor_no_responde": 3
                },
                "solucion": "Verificar que el servidor esté disponible y que el servicio esté funcionando."
            }
        },
        "preguntas": [
            ("hay_wifi", "¿El equipo está conectado al Wi-Fi o a la red?"),
            ("hay_ip", "¿El equipo tiene una dirección IP válida?"),
            ("no_abren_dominios", "¿Fallan los sitios por nombre, aunque la red parezca conectada?"),
            ("servidor_no_responde", "¿El servidor de destino no responde?")
        ]
    },
    "2": {
        "nombre": "Computadoras",
        "causas": {
            "Memoria o CPU saturada": {
                "sintomas": {
                    "equipo_lento": 3,
                    "muchos_programas": 2,
                    "poco_espacio": 0,
                    "sobrecalentamiento": 1
                },
                "solucion": "Revisar el uso de memoria y CPU y cerrar programas innecesarios."
            },
            "Poco espacio en disco": {
                "sintomas": {
                    "equipo_lento": 1,
                    "muchos_programas": 0,
                    "poco_espacio": 3,
                    "sobrecalentamiento": 0
                },
                "solucion": "Comprobar el espacio disponible y liberar archivos innecesarios de forma segura."
            },
            "Posible sobrecalentamiento": {
                "sintomas": {
                    "equipo_lento": 1,
                    "muchos_programas": 0,
                    "poco_espacio": 0,
                    "sobrecalentamiento": 3
                },
                "solucion": "Revisar temperaturas y ventilación; solicitar mantenimiento si persiste."
            }
        },
        "preguntas": [
            ("equipo_lento", "¿El equipo funciona lentamente?"),
            ("muchos_programas", "¿Hay muchos programas abiertos al mismo tiempo?"),
            ("poco_espacio", "¿El disco tiene poco espacio libre?"),
            ("sobrecalentamiento", "¿El equipo se calienta más de lo habitual?")
        ]
    },
    "3": {
        "nombre": "Aplicaciones",
        "causas": {
            "Error de configuración": {
                "sintomas": {
                    "no_inicia": 2,
                    "mensaje_error": 2,
                    "cambio_reciente": 3,
                    "solo_una_app": 2
                },
                "solucion": "Revisar la configuración y los cambios recientes de la aplicación."
            },
            "Dependencia faltante o incompatible": {
                "sintomas": {
                    "no_inicia": 3,
                    "mensaje_error": 3,
                    "cambio_reciente": 2,
                    "solo_una_app": 1
                },
                "solucion": "Consultar el mensaje de error y verificar las dependencias requeridas."
            },
            "Falla general del sistema": {
                "sintomas": {
                    "no_inicia": 1,
                    "mensaje_error": 1,
                    "cambio_reciente": 0,
                    "solo_una_app": -2
                },
                "solucion": "Comprobar los servicios del sistema y si otras aplicaciones presentan fallas."
            }
        },
        "preguntas": [
            ("no_inicia", "¿La aplicación no inicia o se cierra?"),
            ("mensaje_error", "¿Aparece un mensaje de error?"),
            ("cambio_reciente", "¿El problema comenzó después de una actualización o cambio?"),
            ("solo_una_app", "¿El problema ocurre solamente en una aplicación?")
        ]
    },
    "4": {
        "nombre": "Bases de datos",
        "causas": {
            "Servidor o puerto inaccesible": {
                "sintomas": {
                    "conexion_rechazada": 3,
                    "credenciales_error": 0,
                    "servidor_activo": -2,
                    "error_timeout": 3
                },
                "solucion": "Verificar el estado del servidor, el puerto y las reglas de red."
            },
            "Credenciales incorrectas": {
                "sintomas": {
                    "conexion_rechazada": 0,
                    "credenciales_error": 3,
                    "servidor_activo": 2,
                    "error_timeout": -1
                },
                "solucion": "Verificar el usuario, la contraseña y los permisos de acceso."
            },
            "Servicio de base de datos detenido": {
                "sintomas": {
                    "conexion_rechazada": 3,
                    "credenciales_error": 0,
                    "servidor_activo": -3,
                    "error_timeout": 1
                },
                "solucion": "Comprobar si el servicio de base de datos está iniciado."
            }
        },
        "preguntas": [
            ("conexion_rechazada", "¿La conexión es rechazada?"),
            ("credenciales_error", "¿El mensaje menciona usuario, contraseña o permisos?"),
            ("servidor_activo", "¿Has comprobado que el servidor esté activo?"),
            ("error_timeout", "¿La conexión termina por tiempo de espera?")
        ]
    }
}
