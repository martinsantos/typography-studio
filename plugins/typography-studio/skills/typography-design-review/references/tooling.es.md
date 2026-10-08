# Herramientas locales opcionales

Usá las herramientas del proyecto cuando resuelvan mejor edición, composición
de glifos o pruebas. Estos auxiliares inspeccionan binarios aportados:
no dibujan contornos, construyen familias, certifican normas ni puntúan calidad.

## Entorno

Python 3.10+ con `fonttools[woff]` admite metadatos y formatos comprimidos.
Instalá en un entorno virtual manteniendo las comprobaciones TLS y de firmas:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install 'fonttools[woff]'
```

Para capturar, usá Node 20+ y Playwright con Chromium compatible.
Conservá la dependencia local y su archivo de versiones.
Los auxiliares no instalan dependencias ni descargan fuentes por su cuenta.
La validación y el empaquetado usan solo la biblioteca estándar de Python.

## Metadatos y cobertura

```sh
python scripts/inspect_font.py /ruta/a/fuente.ttf --output /ruta/a/metadatos-nuevos.json
```

Ejecutá desde esta carpeta con el Python preparado. Informa SHA-256, nombres,
métricas, peso/estilo, ejes, funciones y caracteres ausentes en texto real,
NFC y NFD. cmap no prueba dibujo, sustitución ni posición de marcas.
Una función declarada no prueba su funcionamiento. Los permisos de
incrustación no reemplazan la licencia.

`--corpus /ruta/a/corpus.json` selecciona texto propio. El esquema de
`assets/corpus.es.json` usa `id` único en minúsculas, `label`/`text`
de texto y `kind` con `words`, `diagnostic` o `paragraph`.
Los párrafos pueden incluir `heading` y `lead` completos: también se
verifica su cobertura. `language` indica el idioma de una muestra.
Los identificadores técnicos se conservan entre idiomas.

## Prueba visual autónoma en español

```sh
python scripts/build_proof.py /ruta/a/fuente.ttf --language es --output /ruta/a/prueba-nueva.html
```

`--language es` traduce encabezados, rótulos, mensajes de carga y avisos;
usa el corpus en español si no se indicó uno propio. `--language en`
conserva la interfaz inglesa. Ambos corpus mantienen palabras de prueba
en español e inglés para comparar el mismo repertorio.

El HTML incrusta una variante real, desactiva estilos sintéticos, utiliza
los ejes variables predeterminados e informa el hash.
Si faltan caracteres, retiene la muestra entera para evitar evidencia falsa
por sustitución. Incluye tamaños de uso y exigencia y ambas polaridades.
Los párrafos parten de 20 px / 1,65 y ajustan ancho hacia 65 grafemas por
línea completa de escritorio. `--measure 60` cambia el objetivo.
Las pantallas estrechas mantienen su ancho. Inspeccioná imágenes y medidas;
las cajas DOM no son límites de tinta.

Para comparar candidatos, conservá el mismo ancho real en lugar de calibrar
cada uno independientemente. Este auxiliar no compara toda una familia,
todos los ejes/funciones ni manejadores. Necesitás pruebas emparejadas y
vistas del editor para eso. Los 12 px son diagnóstico; la ampliación de
96 px aparece en la prueba ancha. Los términos demasiado largos se desplazan
horizontalmente; `overflowSamples` indica cuáles requieren una vista mayor.

## Capturar y verificar la fuente utilizada

```sh
node scripts/capture_proof.mjs /ruta/a/prueba-nueva.html /ruta/a/capturas-nuevas
```

La captura carga HTML local, bloquea solicitudes externas, espera la fuente,
captura anchos 1440/390/320 y obtiene evidencia de Chromium para cada muestra.
Falla ante sustituciones o evidencia ausente en muestras visibles.
`hiddenSamples` registra ampliaciones ocultas en móvil; no están aprobadas
en esa ventana. Los rótulos usan fuente del sistema y quedan fuera de la
auditoría del dibujo. Las muestras sin cobertura se retienen visiblemente.

Si Playwright está en otra ubicación, `TYPE_REVIEW_PLAYWRIGHT` indica su
módulo; `TYPE_REVIEW_BROWSER`, un Chromium existente. Son rutas locales.
`--browser-arg=VALOR` admite una opción explícita necesaria.
Conservá el aislamiento cuando esté disponible; un contenedor Linux
administrado con root puede requerir `--browser-arg=--no-sandbox`
solo para ese entorno.

La salida son capturas y `capture-report.json`, no aprobación visual.
Abrí palabras completas y recortes legibles. Registrá sistema y dispositivo;
este auxiliar no valida Office, Windows ni iOS nativo.

## Preservación y publicación

Las fuentes aportadas no se editan y las salidas rechazan destinos existentes.
El HTML contiene la fuente: tratá licencia y confidencialidad de ese archivo
según el proyecto. Capturar no sube archivos. No agregues fuentes privadas
ni pruebas con fuentes incrustadas a contribuciones públicas sin autorización
y licencia apropiadas.
