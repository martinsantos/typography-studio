# Lectura, jerarquía y tamaño óptico

## Las funciones preceden a las proporciones

Asigná título, sección, subtítulo, bajada, cuerpo, interfaz, guía y epígrafe.
Evaluá su relación en contenido renderizado, incluida la línea anterior al
título. Un titular de 58 px no justifica subtítulos ilegibles de 11 px.
Un antetítulo puede ser menor y conservar una función editorial clara.

`assets/reading-tokens.es.json` ofrece perfiles iniciales ajustables para
pantallas con escritura latina. Cuerpo de 18–20 px, guía de unos 16 px,
interlineado 1,5–1,65 y unos 65 grafemas por línea completa de escritorio
son opciones para probar, no leyes fisiológicas, mínimos universales ni
exigencias WCAG.

USWDS y Practical Typography ofrecen recomendaciones diferentes.
Elegí según lectores, idioma, fuente, densidad y soporte. No atribuyas
una proporción a todas las fuentes ni prometas reproducir una plataforma
actual sin inspeccionarla.

## Compensar el tamaño aparente

Registrá por separado tamaño CSS, caja de línea, altura de mayúsculas/x y
altura visible de tinta. Igual tamaño nominal puede verse muy distinto.
Usá ejes de tamaño óptico disponibles con intención y probá si la aplicación
los aplica. No simules un eje `opsz` escalando geometría.

Comprobá funciones, posiciones y separaciones verticales en la composición
completa. Los títulos pueden necesitar espaciado o interlineado más cerrado.
El tracking debe tener un fin concreto; no repara dibujo ni métricas base.
Revisá saltos y altura total de título/bajada en móvil.

## Medir las líneas reales

Usá el binario, estilo/ejes, idioma y texto elegidos. Contá grupos de grafemas
incluidos los espacios interiores en las líneas efectivamente compuestas.
Separá últimas líneas de párrafo del promedio de líneas completas.
Informá corpus y rango: `65ch` mide anchos del glifo cero, no 65 grafemas.

Partí de una medida en em y calibrá renderizando. En ventanas estrechas,
conservá cuerpo legible y ancho disponible; no achiques para forzar 65
caracteres. Revisá columnas y palabras largas. No cuentes blancos finales
como tinta visible.

En otros sistemas de escritura, definí una medida y comparación apropiadas
sin importar automáticamente objetivos latinos de cantidad de caracteres.

## Probar adaptaciones y contraste

Revisá escritorio, móvil, texto ampliado al 200%, zoom nativo pertinente
y redistribución a 320 px CSS. Cambiar tamaño raíz comprueba un mecanismo;
no equivale al zoom nativo del navegador.

Cuando aplique WCAG 1.4.12, probá juntos interlineado 1,5, separación entre
párrafos 2 em, letras 0,12 em y palabras 0,16 em, sin pérdida de contenido
ni función. Son ajustes del usuario que se deben tolerar, no estilos
iniciales obligatorios. Respetá excepciones por idioma y escritura.

Comprobá colores reales, transparencia y polaridad: 4,5:1 para texto normal
y 3:1 para texto grande según su definición WCAG. La conformidad completa
requiere más comprobaciones que las tipográficas.

## Impresión y estudios con lectores

Usá otra jerarquía en puntos; empezá por 10–12 pt de cuerpo solo cuando
corresponda a fuente y público. Comprobá márgenes, interlineado, encabezados,
tablas, saltos e incrustación real. Abrí las páginas exportadas y probá
impresión física cuando sea el soporte previsto.

Preferencia, reconocimiento, velocidad y comprensión son resultados distintos.
Una revisión visual o escala modular no demuestra mayor rapidez.
Un estudio requiere tareas definidas, participantes representativos,
comparaciones adecuadas y variabilidad informada. Una fuente puede beneficiar
a personas distintas de manera diferente; no prometas una mejora universal.
