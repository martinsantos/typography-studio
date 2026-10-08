# Revisión óptica: contornos, color, espacio y reconocimiento

## Formas y curvas

Empezá por siluetas y palabras; usá nodos y manejadores para localizar causas.
Buscá bultos, planos, estrechamientos y quiebres no buscados. Distinguí
tangencia, continuidad de curvatura y forma óptica adecuada. Los manejadores
cúbicos colineales no necesitan igual largo. Evaluá las esquinas deliberadas
dentro del sistema, sin eliminarlas por una prueba de suavidad.

Usá extremos y segmentos útiles. No agregues un nodo por píxel ni impongas
una cuota arbitraria. Inspeccioná contraformas y exteriores con igual atención.
Compará formas redondas y rectas en altura y peso aparente. El rebasamiento
óptico es una corrección, no un porcentaje universal.

## Color y proporciones

Compará astas, horizontales, diagonales y curvas al mismo tamaño.
Revisá uniones, hombros, cinturas, contraformas, aperturas y terminales:
manchas oscuras y excepciones que atraigan atención sin intención.
Relacioná alturas y anchos con la función, sin igualar siluetas de otras familias.

Una diferencia de píxeles puede deberse al renderizador. Probá otro tamaño
y motor antes de atribuirla al dibujo.

## Espaciado base, kerning y puntuación

Para latín, usá `nnnn`, `oooo`, `nonono`, `HHHH` y `HOHO`;
colocá letras bajo revisión entre controles adecuados. Adaptá el método
al sistema de escritura. Compará blancos interiores y compartidos
ópticamente, sin equiparar sus áreas.

Los huecos generalizados requieren revisar métricas base antes de sumar
pares. Conservá contornos fijos al comparar métricas cuando sea posible.
Revisá componentes acentuados y anclas al mover un dibujo; después,
comprobá nuevamente kerning y espacio entre palabras.

Un par cerrado no corrige el ritmo abierto de un párrafo. Reducir todos los
espacios laterales puede generar colisiones. Compará alternativas moderadas
y conservá el original y los avances reales.

Probá abreviaturas y finales: `IT.`, `OT,`, `A.V.`, `To.`,
`palabra,`, `palabra.` y comillas/signos del idioma cubierto.
Punto y coma tienen blancos distintos junto a un voladizo alto o una curva.
Inspeccionalos por separado y con el espacio que sigue al signo.

## Reconocimiento

Revisá I/l/1, O/0 y rn/m cuando corresponda, aislados y dentro de palabras
y datos. Una diferencia de altura puede desaparecer a tamaños pequeños.
Compará estructuras considerando espacios laterales y voz del diseño.
Ni una I con barras ni una l curva son soluciones universales.

Cubrí acentos, diacríticos, monedas, cifras, puntuación y marcas reales.
Cuando corresponda, comprobá NFC/NFD con un motor de composición.
La presencia en cmap no garantiza composición equivalente ni marcas correctas.

## Registrar lo observado

Identificá glifo o texto, hash del binario, tamaño, peso/ejes, motor,
polaridad, imagen y razón. Separá observación, causa probable y preferencia.
Marcá como `NOT_EVALUATED` las partes no renderizadas o sustituidas.

Geometría, OCR, similitud de imágenes, OTS y FontBakery no puntúan calidad
visual. El contorno ampliado prueba construcción; el párrafo, composición;
el rendimiento de lectura necesita un estudio con personas.
