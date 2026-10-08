---
name: typography-design-review
description: Diseñar, refinar y evaluar fuentes tipográficas a partir de fuentes editables y pruebas renderizadas reales. Usar para construir glifos, corregir ópticamente, ajustar espaciado y kerning, desarrollar cursivas, familias y fuentes variables, exportar OpenType o revisar jerarquía y facilidad de lectura. Inspeccionar las imágenes, identificar la fuente utilizada y distinguir validez técnica, juicio visual y rendimiento de lectura medido. Trabaja con el propósito, las fuentes y las herramientas del usuario, sin imponer una marca, familia ni estilo.
---

# Diseño tipográfico y revisión visual

Partí del propósito para construir un sistema coherente de formas: dibujá,
renderizá, inspeccioná, corregí y documentá. Usá el idioma del usuario en las
explicaciones y los informes. La compilación y las curvas suaves no bastan
para aprobar un dibujo.

## Elegir las referencias

- Diseño nuevo o tono inconsistente: [Del propósito a la forma](references/brief-to-form.es.md).
- Construcción de glifos de control: [Taller de construcción](references/construction-workbench.es.md).
- Formas, espaciado, kerning o confusiones: [Revisión óptica](references/optical-review.es.md).
- Pesos, cursivas, fuentes variables y exportación: [Familias y exportaciones](references/families-and-exports.es.md).
- Tamaños, títulos, interlineado y composición adaptable: [Lectura y jerarquía](references/reading-and-hierarchy.es.md).
- Especificaciones y decisiones de entrega: [Normas y aceptación](references/standards-and-acceptance.es.md).
- Ejercicios y devolución: [Práctica y evaluación](references/practice-and-calibration.es.md).
- Influencias educativas y atribución: [Formación](references/formation-and-design.es.md) y [Fuentes consultadas](references/sources.es.md).
- Herramientas deterministas: [Herramientas locales](references/tooling.es.md).

## 1. Establecer el uso previsto

Recuperá la función, el público, el tono, los idiomas y sistemas de escritura,
los tamaños, las plataformas, los formatos y la titularidad de las fuentes.
Inferí lo que ya aportó el usuario y preguntá por faltantes que afecten el
resultado, mientras avanzás en tareas independientes.

Registrá el propósito con [la plantilla](assets/brief-template.es.md).
Definí restricciones observables: proporciones, contraste de trazos, curvas,
terminales, aperturas, peso, ritmo y reconocimiento. Las categorías «sans» o
«serif» no determinan una voz. Elegí referencias con licencia para comparar,
sin copiarlas por calco.

Para un diseño latino nuevo, empezá por H/O/n/o y después revisá las estructuras
críticas e/s/r/a dentro de palabras. Elegí controles adecuados para otro
sistema de escritura. No extrapoles un alfabeto completo desde controles sin
revisar. En fuentes existentes, inspeccioná primero las palabras del usuario.

## 2. Identificar y preservar los archivos

Identificá fuentes editables, binarios exportados, versión y SHA-256.
Conservá la iteración anterior. Evitá inicializadores que reemplacen dibujos
existentes. Generá cada candidato en una carpeta nueva y registrá el compilador
y sus opciones.

Usá el editor y compilador admitidos por el proyecto. UFO/designspace, Glyphs
y SFD son formatos de trabajo, no binarios terminados intercambiables.
Cambiar los metadatos de una fuente no crea un dibujo original nuevo.

`scripts/inspect_font.py` informa metadatos y cobertura del corpus sin modificar
la fuente. No evalúa curvas, composición de glifos ni estética. Los glifos
ausentes, las sustituciones silenciosas, los estilos sintéticos y las
transformaciones horizontales invalidan la evidencia sobre un dibujo.
Marcá el material sin cobertura como no evaluado.

## 3. Producir pruebas e inspeccionarlas

Usá el binario real en un motor disponible. Esperá la carga y verificá qué
fuente utiliza el renderizador. Mantené comparables el tamaño, peso, ejes,
línea de base, texto, ventana, espaciado y polaridad entre iteraciones.

Prepará palabras y frases completas al tamaño de uso; después, siluetas
ampliadas y contornos con nodos y manejadores para localizar las causas.
Agregá párrafos, puntuación, cifras y signos propios del idioma. Probá tamaños
mínimos, habituales y exigentes, ambas polaridades y el repertorio real.

`scripts/build_proof.py` genera un HTML autónomo a partir de la fuente y el
corpus. Usá `--language es` para los rótulos y mensajes en español; sin un
corpus personalizado, selecciona `assets/corpus.es.json`. Las muestras sin
cobertura se retienen. `scripts/capture_proof.mjs` captura con Playwright y
registra qué fuente se utilizó. Adaptá corpus, tamaños y herramientas.

**Abrí e inspeccioná las imágenes.** Generar capturas no constituye una revisión
visual. Asegurá que se vean palabras completas, contornos y contexto de títulos.
Reencuadrá pruebas recortadas y abrí secciones legibles de páginas extensas.
Si no podés inspeccionar imágenes, declaralo pendiente sin inventar observaciones.

## 4. Evaluar el sistema antes de reparar un detalle

Describí constantes y variaciones deliberadas. Evaluá cada criterio como
`LOCALLY_ACCEPTABLE` (aceptable dentro del alcance), `DEFECT` (defecto) o
`NOT_EVALUATED` (no evaluado), con imagen, texto, variante, tamaño y motivo:

| Criterio | Qué observar |
| --- | --- |
| Forma, curvas y terminales | Quiebres, bultos, planos, estrechamientos y cortes inconsistentes |
| Peso óptico y contraformas | Uniones oscuras, aperturas cerradas y cambios de color no buscados |
| Espaciado y ritmo | Pausas falsas, colisiones, blanco entre palabras y relación con los signos |
| Reconocimiento al tamaño real | Confusiones I/l/1, O/0 y rn/m dentro de palabras cubiertas |
| Voz y función | Relación entre el detalle, el propósito y la palabra completa |

Ante una discrepancia grave, recomendá `REDRAW_REQUIRED` (requiere redibujo).
Las comprobaciones técnicas no la compensan. Si faltan letras o contexto,
usá `FUNCTIONAL_CHECK_INCOMPLETE` (comprobación funcional incompleta) y
producí primero esa evidencia.

Resolvé los espacios laterales y entre palabras antes de acumular pares de
kerning. Revisá puntuación en abreviaturas y finales. Separá tracking y kerning.
Una fuente más cerrada no es necesariamente más legible; una curva redonda
no implica un tono lúdico.

## 5. Corregir con una hipótesis y comprobar el resultado

Explicá la hipótesis y el efecto visible esperado antes de editar.
Separá cambios de dibujo y métricas cuando sea útil. Conservá el original
y compará variantes en condiciones equivalentes; usá rótulos neutrales antes
de revelar la elección constructiva cuando eso ayude.

Editá estructura, trazos, contraformas y terminales en conjunto, con nodos
útiles. Volvé a las palabras después de modificar una letra aislada.
Comprobá letras vecinas, acentos, signos y pesos extremos para detectar
regresiones. Cambiá la hipótesis si la evidencia la contradice.

En familias, revisá cada peso y estilo distribuido, extremos e intermedios
de los ejes. Las extrapolaciones son candidatas. La cursiva requiere una
estructura deliberada. Verificá sustituciones OpenType y posición de marcas
con herramientas de composición de glifos.

## 6. Revisar la composición por separado

Elegí funciones antes que tamaños: título, subtítulo, bajada, cuerpo, interfaz
y guía. Usá [los valores iniciales](assets/reading-tokens.es.json) como perfil
ajustable. Compensá tamaño aparente, altura de x, mayúsculas, peso, idioma
y pantalla. Cuerpo, subtítulo y guía deben conservar una relación coherente.

Para el perfil editorial latino de pantalla, empezá alrededor de 18–20 px
de cuerpo, interlineado 1,5–1,65 y unos 65 grafemas por línea completa de
escritorio. Son decisiones que requieren pruebas renderizadas. En móvil,
usá el ancho disponible. En impresión, trabajá en puntos y con otra escala.

Medí por separado tamaño calculado, altura visible de tinta y caja de línea.
Contá grafemas en las líneas reales: `65ch` no equivale a 65 caracteres.
Revisá saltos y proporciones de título y bajada, incluida la línea anterior
al titular. No apruebes una escala por aritmética ni supongas estilos actuales
de una plataforma sin inspeccionarlos.

Comprobá contraste, ampliación, redistribución y ajustes de espaciado del
usuario sobre contenido real. Aplicá los criterios WCAG pertinentes de la
referencia de normas. Las métricas CSS y la preferencia visual no demuestran
lectura más rápida o mejor comprensión; eso exige pruebas con lectores.

## 7. Cerrar la revisión y conservar lo aprendido

Separá requisitos técnicos, decisiones del proyecto y juicio visual.
Registrá archivos y hashes, corpus, versiones, motores, plataformas,
imágenes abiertas, defectos corregidos, límites y advertencias.
Usá [la ficha de revisión](assets/review-template.es.md).

Indicá el resultado: redibujar, reunir evidencia o aceptar dentro del alcance
declarado. Seguí los criterios del usuario, sin inventar firmas externas,
certificaciones ni otra barrera de publicación. Respetá el rechazo existente
del candidato exacto. Una preferencia A/B no aprueba una familia completa.

Terminá una iteración cuando pasen sus comprobaciones y la inspección no
identifique otro defecto concreto dentro del alcance. Evitá editar contornos
sin hipótesis. La nueva evidencia puede reabrir la revisión. Un conjunto
finito de pruebas no certifica perfección ni compatibilidad universal.

Conservá el juicio inicial cuando una devolución lo corrija. Los casos
repetidos son práctica, no una prueba independiente de eficacia ni
entrenamiento del modelo. Ningún script asigna una puntuación de calidad.
