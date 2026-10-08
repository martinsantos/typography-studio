# Normas técnicas y aceptación con alcance definido

Separá tres tipos de evidencia:

1. **Requisitos aplicables:** especificaciones de formato y accesibilidad.
2. **Perfil del proyecto:** repertorio, estilos, tamaños, plataformas y entrega.
3. **Juicio visual:** muestras renderizadas efectivamente abiertas y revisadas.

Registrá sección, versión/estado, URL y fecha de consulta. OTS y FontBakery
son comprobaciones independientes útiles, no una puntuación de calidad.
Un corpus finito no demuestra perfección ni compatibilidad universal.

## Formatos y composición de glifos

- [OpenType](https://learn.microsoft.com/en-us/typography/opentype/spec/otff):
  tablas, directorio, alineación, sumas de comprobación y reglas por formato.
  Ejecutá OTS sobre los archivos distribuidos y conservá el original, sin
  reemplazarlo silenciosamente por la salida del saneador.
- [name](https://learn.microsoft.com/en-us/typography/opentype/spec/name),
  [OS/2](https://learn.microsoft.com/en-us/typography/opentype/spec/os2),
  [cmap](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap),
  [fvar](https://learn.microsoft.com/en-us/typography/opentype/spec/fvar):
  nombres, vinculación de estilos, métricas, cobertura, ejes e instancias.
  Tener cmap Unicode no implica cubrir todo Unicode.
- [WOFF2](https://www.w3.org/TR/WOFF2/): cabeceras, decodificación y
  fidelidad al SFNT de origen. Los hashes del SFNT reconstruido difieren
  de los bytes almacenados en WOFF2.
- [glyf](https://learn.microsoft.com/en-us/typography/opentype/spec/glyf):
  estructura y banderas. OVERLAP_SIMPLE es opcional; revisá advertencias y
  renderizado sin transformar cualquier recomendación en obligación.
- [Normalización Unicode](https://www.unicode.org/reports/tr15/#Design_Goals):
  equivalencia canónica. Compará el corpus NFC/NFD con composición y marcas;
  la normalización no exige bytes de composición idénticos para todo texto.

`fsType=4` indica incrustación para previsualización e impresión. No concede
incrustación editable, acredita titularidad ni reemplaza una licencia.
Probá por separado la edición con fuentes instaladas. No borres permisos
para superar una prueba documental.

En Word, consultá [WordprocessingML Kern](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.kern):
el umbral se expresa en medios puntos y se hereda por estilos. Si ningún
nivel habilita kerning, no se aplica. Probá la aplicación y los estilos reales.

## Tipografía web

Consultá [WCAG 2.2](https://www.w3.org/TR/WCAG22/) y sus páginas explicativas:

| Criterio | Alcance |
| --- | --- |
| 1.4.3 | Contraste normal 4,5:1 y grande 3:1, con sus excepciones |
| 1.4.4 | Ampliar texto al 200% sin pérdida de contenido ni función |
| 1.4.10 | Redistribución a 320 px CSS para lectura vertical, con excepciones |
| 1.4.12 | Tolerar los ajustes combinados de espaciado del usuario |
| 1.4.8 | Controles opcionales AAA; no una receta de estilos iniciales |

No atribuyas a WCAG cuerpo de 16 px, líneas de 65 caracteres o interlineado
1,65. [CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/) describe selección,
kerning, variaciones y síntesis; registrá su estado al consultar.
Verificá la fuente que dibuja la muestra, además del CSS calculado.

## Cerrar la revisión

Registrá hashes, corpus, tamaños, estilos/ejes, versiones, plataformas,
resultados técnicos y advertencias, imágenes abiertas, defectos y condiciones
no probadas. Seguí los criterios acordados sin inventar firmas obligatorias
ni certificaciones externas.

Usá `TECHNICALLY_ACCEPTABLE_IN_SCOPE` para requisitos y perfil verificados;
`LOCALLY_ACCEPTABLE` para hallazgos visuales del corpus declarado.
Explicá defectos pendientes por separado. La evidencia nueva reabre su parte.
