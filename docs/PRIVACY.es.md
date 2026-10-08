# Aviso de privacidad de Typography Studio

Editor: Martín Santos. Actualizado el 2026-10-08.
[English](PRIVACY.md).

## Alcance

Typography Studio distribuye una skill para agentes y auxiliares locales
opcionales para pruebas tipográficas. El paquete no incluye un servidor
del editor, conexión de cuenta, analítica, telemetría ni servicio de subidas
automáticas.

Los auxiliares leen la fuente y el corpus elegidos por el usuario y crean
metadatos, HTML y capturas locales. El HTML incrusta la fuente seleccionada.
El capturador bloquea solicitudes de red externas. Estos auxiliares no
envían las fuentes ni las pruebas seleccionadas al editor.

Los archivos elegidos pueden contener metadatos de autoría o copyright en
la fuente, o información personal en el texto de prueba. Los auxiliares
usan ese contenido para inspeccionar la fuente y producir las pruebas
solicitadas; los resultados pueden incluir sus metadatos y el texto elegido.

## Herramientas del entorno e instalación

ChatGPT, Codex u otro entorno de agentes puede procesar la información
aportada en conversaciones o mediante sus herramientas según los ajustes
y políticas de ese servicio. La investigación solicitada puede utilizar
su navegador o herramientas conectadas. Revisá el destino y los permisos
antes de compartir fuentes confidenciales, trabajos de clientes o datos
personales mediante esas herramientas.

GitHub gestiona descargas e interacciones del repositorio. Si instalás con
el CLI Skills, que es una herramienta separada, se aplica su propia política
de telemetría; consultá la [documentación del CLI](https://www.skills.sh/docs/cli).

## Archivos locales y soporte

El usuario controla los archivos generados localmente y puede borrarlos
con sus herramientas habituales. Las fuentes incrustadas y las capturas
conservan los requisitos de licencia y confidencialidad del material original.
Los resultados permanecen en la carpeta local elegida hasta que el usuario
los elimina; los auxiliares no programan su retención ni borrado automático.

El soporte utiliza [Issues públicos de GitHub](https://github.com/martinsantos/typography-studio/issues).
No incluyas fuentes privadas, credenciales, datos personales ni archivos
confidenciales de clientes en un issue público. El editor puede ver la
información que decidas publicar allí.
Esa información pública permanece disponible mientras esté disponible la
publicación. GitHub gestiona los controles de cuenta, historial de ediciones
y retención; utilizá los permisos de tu cuenta para gestionar lo que publicaste.
