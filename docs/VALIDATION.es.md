# Registro de validación

[English](https://github.com/martinsantos/typography-studio/blob/v0.4.1/docs/VALIDATION.md). Registro original del 2026-10-08, versión 0.4.0.
Las comprobaciones del paquete y sus auxiliares se distinguen de la aprobación
de una familia, una evaluación independiente de agentes y la aceptación
del catálogo de OpenAI.

## Fuente externa con licencia

**Asap Regular 3.002**, Asap Project Authors / Omnibus-Type,
SIL Open Font License 1.1. Archivo externo del commit Google Fonts
`5e8a3ba899557829a76cfdac30fa512bda91d7ca`:
`ofl/asap/Asap[wdth,wght].ttf`.

SHA-256: `7bf29bcab72f7d00de600e964a3fc206620050d8448ddd976822378d0fe18028`.

Se usó como fuente existente con licencia, no como diseño de esta skill.
No se distribuyen fuentes ni PDF de terceros. La imagen del README es
una salida renderizada. [Proyecto](https://github.com/Omnibus-Type/Asap) ·
[Licencia](https://github.com/google/fonts/blob/5e8a3ba899557829a76cfdac30fa512bda91d7ca/ofl/asap/OFL.txt).

## Comprobaciones originales ejecutadas

- Se validaron rutas, límites del manifiesto, textos de presentación,
  iconos, metadatos, enlaces, licencia, exclusiones y sintaxis Python.
- Los ZIP se generaron dos veces en Linux con hashes coincidentes,
  rutas portables y metadatos fijos. No se ejecutó empaquetado en Windows.
- FontTools 4.59.1 leyó la fuente variable sin modificar su hash.
  Ejes predeterminados: peso 400, ancho 100. La cobertura del corpus pasó.
- Chromium 151.0.7922.173 / Playwright 1.58.2 en Linux capturaron 1440,
  390 y 320 px CSS. La auditoría identificó fuente propia en 72 muestras
  de escritorio y 60 en cada ancho móvil, sin sustituciones.
  Las ampliaciones de 96 px ocultas en móvil se registraron como tales.
- Las líneas completas de escritorio quedaron entre 59 y 68 grafemas
  después del ajuste hacia 65. Las últimas líneas parciales se separaron.
- Texto y títulos sin cobertura retuvieron su muestra. Se rechazaron salidas
  existentes, se escapó HTML literal y se informó una fuente inválida.
- Una sustitución CSS deliberada con fuente del sistema produjo el rechazo
  esperado, código de salida 1 y evidencia del renderizador.
- La prueba del publicador usó Git real local: commit, remoto vacío,
  etiqueta anotada y SHA coincidente. GitHub y la transferencia de release
  fueron simulados; se comprobaron guardas de preservación.

## Inspección visual original

Se abrieron controles y lectura en escritorio y móvil, en ambas polaridades,
con títulos, bajadas y cuerpo completos. Se reemplazaron fragmentos
incompletos de títulos y se evitaron saltos dentro de palabras diagnósticas.
Una muestra a 48 px y ancho 320 desbordó horizontalmente: requiere la vista
más ancha para juzgarse.

`proof-example.png`: 1212 × 818, SHA-256
`87a3f70f4ff310cc13ee8b95631bb7639b30264dd2f45f084c0733ad96508644`.

Estas pruebas verifican generación utilizable de evidencia, no superioridad
del diseño producido por el agente ni lectura más rápida.

## Publicación 0.4.0

La conexión cloud recibió inicialmente `403 — Resource not accessible by
integration`. La Mac autorizada recuperó los 18 bloques, verificó su SHA-256
y publicó el repositorio y la release 0.4.0. Se verificaron el commit remoto,
la etiqueta y los tres ZIP descargados.

[Repositorio](https://github.com/martinsantos/typography-studio) ·
[Release 0.4.0](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.0).

## Límites

Los diez casos de `evals/cases.json` son propuestas de comportamiento,
no una evaluación independiente ejecutada. La revisión original de una
variante no probó Office, Windows o iOS nativo, ni todas las funciones y
posiciones de una familia. La presentación y revisión de OpenAI siguen
siendo independientes.

## Comprobaciones de localización 0.4.1

2026-10-08. Se agregaron instrucciones, diez referencias, plantillas,
metadatos y pruebas en español, conservando el inglés. Pasaron el validador,
la comprobación de metadatos de skill, la prueba de paquetes localizados
y la simulación del publicador. Se generan seis ZIP: skill, plugin y
marketplace de instalación en ambos idiomas. Se conservan identidad,
auxiliares ejecutables y métricas de lectura. Los scripts de mantenimiento
están en el código fuente canónico.

Python 3.13 / FontTools 4.58.0 renderizaron ambos idiomas con Asap y el
mismo hash anterior, fuera del paquete. Pasaron cobertura de acentos,
idiomas de párrafo, retención de glifos ausentes en español, escape HTML,
rechazo de idioma inválido, conservación de salidas y hash de fuente.
Chrome 154.0.8037.98 / Playwright en macOS verificaron fuente propia en
72 muestras de escritorio y 60 por ancho móvil a 1440/390/320 px CSS,
sin sustituciones ni evidencia ausente.

Se abrieron encabezado español, lectura completa en español en ambas
polaridades, controles de escritorio y capturas de lectura móvil.
Títulos, bajadas y cuerpo se vieron con su contexto. Las medidas de párrafo
en inglés y español a 1440 px fueron idénticas. Son pruebas de localización
y herramientas; no aprueban una fuente ni certifican Office o iOS nativo.

Se extrajeron los tres paquetes españoles y se ejecutó su generador sin
indicar idioma: todos eligieron español por defecto. La skill extraída
también pasó el validador de metadatos de skill-creator.
