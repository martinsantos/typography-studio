# Fuentes consultadas y límites

Resúmenes originales y referencias enlazadas, sin redistribuir libros o PDF
ni atribuir respaldo de sus autores. Las especificaciones, recomendaciones
de diseño y estudios con lectores aportan evidencias distintas.
Registro de consulta original: 2026-10-08. Esta traducción conserva ese
registro; verificá el material primario vigente al aplicarlo a una entrega.

## Construcción, espaciado e influencias educativas

- *Design With FontForge*, documentación comunitaria:
  [Trusting Your Eyes](https://designwithfontforge.com/en-US/Trusting_Your_Eyes.html),
  [Creating o and n](https://designwithfontforge.com/en-US/Creating_o_and_n.html),
  [Spacing, Metrics and Kerning](https://designwithfontforge.com/en-US/Spacing_Metrics_and_Kerning.html),
  [Word Space](https://designwithfontforge.com/en-US/Word_Space.html).
  Juicio óptico contextual, controles y espaciado antes del kerning.
- OERT, [Percepción visual y ritmo](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/percepcion-visual-y-ritmo.md),
  Marcela Romero, colaboración de Inés Puparelli: reconocimiento, intervalos y ritmo.
- OERT, [La letra y su conjunto](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/la-letra-y-su-conjunto.md),
  Marcela Romero: signo/palabra, blancos compartidos, interlineado y color.
- OERT, [Conceptos fundamentales](https://github.com/oert/live.oert.org/blob/0cb82c5a495cd11753d869578bf4a41d3f0b5a25/es/conceptos-fundamentales.md),
  Pablo Cosgaya, colaboración de Marcela Romero y revisión de Natalia Pano:
  familia, variables, espaciado y color. Estos apartados y los artículos
  anteriores nutrieron los resúmenes originales.
- Pablo Cosgaya, *Programa Tipografía 1*, 2016, programa histórico FADU/UBA
  aportado para estudio. Consultado para estructura, trazo, contraformas,
  constantes de familia y crítica razonada. No prueba el programa vigente.
  El PDF no se incluye.
- Eduardo Gabriel Pepe, *Diseño tipográfico e identidad*, **Bold 2**, 2015,
  pp. 56–66. Artículo aportado y consultado para forma, función, identidad
  y proceso; no se incluye. **Rubén Fontana (2007) aparece como cita
  secundaria en Pepe, p. 65**; no se leyó directamente ese texto de Fontana
  ni se atribuye respaldo al método.
- Glyphs, [Multiple Masters, Part 1: Setting Up Masters](https://glyphsapp.com/learn/multiple-masters-part-1-setting-up-masters),
  Rainer Erich Scheichelbauer: configuración de másteres e interpolación.

## Google Fonts

- [Google Fonts Guide](https://googlefonts.github.io/gf-guide/): se consultó
  la portada, que separa estructura de fuentes, requisitos generales,
  estáticos/variables, contornos, control de calidad y pruebas locales.
  Leé el capítulo completo pertinente antes de afirmar cumplimiento.
- [gf-docs README](https://github.com/googlefonts/gf-docs/blob/main/README.md)
  declara obsoleto ese repositorio y enlaza la guía anterior.
  [Reviewing Families](https://github.com/googlefonts/gf-docs/tree/main/ReviewingFamilies)
  y [Quick Start](https://github.com/googlefonts/gf-docs/tree/main/QuickStartGlyphs)
  históricos orientaron la separación entre fuentes, compilación, controles
  y renders; no son política vigente de presentación.
- [Google Fonts Knowledge](https://fonts.google.com/knowledge) devolvió una
  estructura JavaScript en el entorno de consulta original. No se declara
  leído ningún artículo no visible ni se midió CSS actual de Medium.

## Composición, accesibilidad y resultados de lectura

- USWDS [Typography](https://designsystem.digital.gov/components/typography/),
  [font size](https://designsystem.digital.gov/design-tokens/typesetting/font-size/)
  y [line height](https://designsystem.digital.gov/design-tokens/typesetting/line-height/):
  funciones, tamaño efectivo, medida e interlineado. Recomienda, entre otras
  opciones, 66 caracteres e interlineados alrededor de 1,5/1,62.
  Los 65 grafemas y 1,65 del paquete son elecciones ajustables.
- Matthew Butterick, *Practical Typography*:
  [Point size](https://practicaltypography.com/point-size.html),
  [Line length](https://practicaltypography.com/line-length.html),
  [Line spacing](https://practicaltypography.com/line-spacing.html),
  [Headings](https://practicaltypography.com/headings.html),
  [Letterspacing](https://practicaltypography.com/letterspacing.html),
  [Kerning](https://practicaltypography.com/kerning.html).
  Sus recomendaciones de 15–25 px, líneas de 45–90 caracteres e interlineado
  120–145% difieren del perfil amplio 1,65. No hay acuerdo unánime sobre
  una proporción única.
- W3C [WCAG 2.2](https://www.w3.org/TR/WCAG22/) y páginas explicativas:
  [contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html),
  [ampliación](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html),
  [redistribución](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html),
  [espaciado](https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html),
  [presentación visual](https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html).
  Aplicá nivel, excepciones y mecanismo de cada criterio. Las tolerancias
  de espaciado no son estilos iniciales obligatorios. Una fuente sola
  no certifica conformidad WCAG de un sitio.
- Wallace y colaboradores (2022), *Towards Individuated Reading Experiences:
  Different Fonts Increase Reading Speed for Different Individuals*,
  [resumen de Adobe Research](https://research.adobe.com/publication/towards-individuated-reading-experiences-different-fonts-increase-reading-speed-for-different-individuals/).
  Solo se leyó la página y el resumen. Advierte contra una fuente óptima
  universal; no establece una mejora numérica de este paquete.
- La proporción áurea es un modelo de composición, no prueba de lectura
  perfecta. El paquete no la utiliza para aprobar un resultado.

## Formatos e integración nativa

- Microsoft [OpenType](https://learn.microsoft.com/en-us/typography/opentype/spec/),
  especialmente [name](https://learn.microsoft.com/en-us/typography/opentype/spec/name),
  [OS/2](https://learn.microsoft.com/en-us/typography/opentype/spec/os2),
  [cmap](https://learn.microsoft.com/en-us/typography/opentype/spec/cmap) y
  [fvar](https://learn.microsoft.com/en-us/typography/opentype/spec/fvar).
  Sintaxis, nombres, permisos y ejes no definen calidad estética.
- W3C [WOFF2](https://www.w3.org/TR/WOFF2/) y
  [CSS Fonts 4](https://www.w3.org/TR/css-fonts-4/): distribución,
  renderizado, fuente utilizada, estilos y síntesis.
- Unicode [normalización](https://www.unicode.org/reports/tr15/):
  NFC/NFD requiere comprobar composición, además del mapa de caracteres.
- Microsoft [OOXML `w:kern`](https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.kern):
  umbrales de kerning y herencia necesitan pruebas en la aplicación real.
  Un navegador Linux o LibreOffice no valida Office nativo ni iOS.

## Empaquetado de skills y plugins

- OpenAI [Build skills](https://learn.chatgpt.com/docs/build-skills),
  [Package your plugin](https://developers.openai.com/plugins/build/plugins),
  [Submit and publish](https://developers.openai.com/plugins/deploy/submission)
  y [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines):
  consulta original del 2026-10-08 sobre recursos progresivos, manifiesto,
  iconos y diferencia entre distribución y revisión del catálogo.
- OpenAI [skill-creator](https://github.com/openai/skills/tree/main/skills/.system/skill-creator):
  entrada enfocada, auxiliares opcionales y referencias según necesidad.
  Es una referencia de empaquetado, no un respaldo del paquete.
