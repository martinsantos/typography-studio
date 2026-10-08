# Material de presentación al catálogo

Versión 0.4.1, plugin compuesto únicamente por una skill.
Este documento prepara la presentación; no acredita envío, aprobación
ni publicación en el catálogo de OpenAI.

- Nombre: **Typography Studio**
- Subtítulo: **Diseñá y revisá fuentes**
- Editor: identidad verificada elegida en el panel.
- Categoría: confirmar las opciones vigentes del panel.
- Soporte: [Issues del repositorio](https://github.com/martinsantos/typography-studio/issues).
- Idiomas: instrucciones, diez referencias y plantillas en español e inglés;
  informes en el idioma del usuario. Corpus latino en ambos idiomas.
- Paquete español: `typography-studio-0.4.1-plugin-es.zip`.

## Descripción

Diseñá y refiná fuentes desde su propósito: glifos de control, correcciones
ópticas, espaciado, kerning, pesos, cursivas, familias variables y exportaciones.
Revisá palabras renderizadas y jerarquías de lectura con referencias
atribuidas y evidencia. Incluye herramientas locales opcionales y corpus
latino en español e inglés. Requiere inspección de imágenes y un editor
adecuado para modificar fuentes. Los controles técnicos no certifican
estética, velocidad de lectura ni plataformas sin probar.

## Pedidos iniciales

1. Ayudame a diseñar una fuente desde su propósito y revisar glifos de control
   dentro de palabras reales.
2. Revisá curvas, espaciado, puntuación y jerarquía de mi fuente con pruebas
   visuales reales.

## Comportamiento y privacidad

Una skill, sin servidores MCP, conexiones de cuenta, hooks, telemetría
ni subidas automáticas. Los auxiliares leen fuentes y corpus elegidos
y crean metadatos, HTML y capturas locales nuevos.
El HTML incrusta la fuente: se aplican su licencia y confidencialidad.
El capturador bloquea solicitudes externas. La investigación solicitada
puede utilizar herramientas del entorno con sus permisos; el paquete
no implementa un servicio externo.

El agente debe abrir imágenes antes de concluir visualmente.
La skill necesita herramientas de edición para modificar fuentes.
Los resultados con lectores requieren participantes, y las plataformas
nativas deben probarse para sostener afirmaciones sobre ellas.

## Licencia y originalidad

MIT para instrucciones, resúmenes, código y recursos originales.
No se redistribuyen fuentes, capítulos PDF ni entregas de clientes.
Las referencias están atribuidas; no se declara respaldo de sus autores
ni de OpenAI.

## Evidencia

La validación comprueba rutas, límites de metadatos, referencias, iconos,
alcance y archivos generados. Las pruebas de auxiliares registran fuente,
hash, versiones e imágenes reales. Los casos de `evals/cases.json`
son propuestas de evaluación, no un estudio independiente ejecutado.
[Registro de validación](VALIDATION.es.md).
