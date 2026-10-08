# Familias, cursivas, variaciones y distribución

## Ampliar un sistema revisado

Conservá la variante inicial aprobada. Dibujá másteres adicionales con
decisiones deliberadas de astas, horizontales, contraformas, uniones y
espaciado. Contornos correspondientes, direcciones, puntos iniciales y tipos
de nodo deben admitir interpolación sin alterar extremos previstos.
Convertí másteres cúbicos a cuadráticos juntos para variaciones TrueType.

Revisá extremos e intermedios de los ejes, también entre instancias con
nombre. Las extrapolaciones son provisionales. Los pesos finos exponen
uniones débiles; los gruesos pueden cerrar blancos, fusionar trazos y
dañar signos. Pasos numéricos iguales de `wght` no garantizan coherencia óptica.

## Cursivas y comportamiento OpenType

Definí qué formas cambian de estructura y cuáles siguen la redonda.
Un ángulo de inclinación no aprueba una cursiva. Revisá entradas, salidas,
ancho, hombros, uniones, espaciado y acentos. No impongas un ángulo
universal ni una construcción obligatoria de a/f.

Verificá cifras proporcionales y tabulares mediante sustituciones y avances
reales. El tracking no reemplaza diseños distintos de cifras.
Probá alternancias sin codificar activando su función: cmap no las muestra.
Comprobá diacríticos, anclas y composición por idioma con texto real.

## Exportar con fidelidad

- Usá fuente editable y compilador del proyecto. Registrá versiones, opciones
  y revisión; conservá el candidato anterior.
- Compará contornos y avances entre fuentes y formatos, con tolerancia adecuada
  de conversión. Esto verifica fidelidad, no legibilidad.
- Coordiná nombres de familia/subfamilia, estilos vinculados, pesos, métricas,
  STAT/fvar, instancias y nombres PostScript. Probá convivencia y actualización.
- Validá cada binario estático y variable distribuido, incluidas advertencias.
  Agrupá familias correctamente en FontBakery; explicá advertencias sin borrar
  contornos válidos para mejorar una puntuación.
- Conservá permisos de incrustación. Incluí licencia, versión, archivos y hashes.
  La licencia de estas herramientas no licencia las fuentes del usuario.
- Conservá inmutables las URL de archivos versionados: corregí con una release
  nueva. Documentá fuentes alternativas, licencias y cobertura por separado.

## Evidencia por plataforma

Ajustá la matriz al uso: navegadores, renderizado de Windows, Word/Excel/
PowerPoint si corresponde, aplicaciones de Apple, PDF e impresión.
Registrá versiones reales de sistema y aplicación. WebKit en Linux no es
una prueba física de iOS; LibreOffice no es Microsoft Office y PDF no es papel.

En Office, probá estilos estáticos instalados, selección real de negrita y
cursiva, vinculaciones, kerning explícito, saltos, acentos y exportación.
Una lista de alternativas CSS no se traslada automáticamente a Word.
Editar con una fuente instalada difiere del permiso de incrustación editable.

En iOS, distinguí fuentes web en Safari, visualización PDF y fuentes instaladas
utilizadas por cada aplicación. Instalar no garantiza reconocimiento universal.

Consultá [Normas y aceptación](standards-and-acceptance.es.md).
