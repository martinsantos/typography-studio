# Typography Studio

Skill abierta y plugin de Codex para **diseñar fuentes tipográficas y revisar
su calidad visual**. Parte del propósito de la fuente, desarrolla un sistema
de formas y revisa palabras reales antes de ampliar el alfabeto y la familia.
Es independiente de marcas, familias concretas y estilos obligatorios.

![Prueba real de título, bajada y cuerpo sobre fondo claro y oscuro](docs/images/proof-example.png)

Ejemplo de la herramienta con **Asap Regular**, una fuente abierta existente,
que no fue dibujada por esta skill ni se redistribuye en el paquete.

Versión **0.4.0**. Incluye instrucciones, referencias, plantillas, ejercicios
y herramientas opcionales para inspeccionar fuentes y capturar pruebas.
La revisión exige abrir las imágenes: un archivo válido no demuestra que
los glifos estén bien dibujados. No promete legibilidad perfecta ni reemplaza
un editor de fuentes. El corpus inicial cubre casos latinos en español e inglés.

## Usarla

Copiá la carpeta
`plugins/typography-studio/skills/typography-design-review/` dentro de
`.agents/skills/` de tu proyecto. Después pedí, por ejemplo:

> Usa $typography-design-review para construir una sans de títulos clara y
> fuerte. Empezá por H/O/n/o y revisá palabras reales antes de ampliar el repertorio.

> Usa $typography-design-review para revisar esta fuente: curvas, espaciado,
> puntuación, jerarquía, ancho de lectura e interlineado. Mostrá las pruebas
> visuales y registrá los límites de la revisión.

Para instalar el plugin desde un checkout local:

```sh
codex plugin marketplace add /ruta/absoluta/typography-studio
codex plugin add typography-studio@typography-studio-marketplace
```

Las herramientas opcionales requieren Python con FontTools y, para capturar,
Node con Playwright. La skill puede utilizar las herramientas del proyecto
sin estos auxiliares. La instalación requiere un cliente compatible.

## Qué distingue la evaluación

- Construcción y tono se juzgan contra el brief del usuario.
- Dibujo, espaciado, exportación y composición se comprueban por separado.
- Tamaños, altura aparente, interlineado y longitud de línea se revisan en pantalla.
- Los valores iniciales de composición son ajustables; no son leyes universales.
- No se aprueba una familia completa con una palabra o una sola captura.
- Cada conclusión identifica el archivo, la imagen, el tamaño y el contexto observado.

La licencia MIT permite usar, modificar y redistribuir el paquete. Las fuentes
de cada proyecto conservan su licencia. Las referencias educativas están
atribuidas; no se redistribuyen los PDF ni se atribuye respaldo de sus autores.

La publicación en GitHub y su marketplace no equivale a figurar en el catálogo
público de OpenAI. [El procedimiento de publicación](docs/PUBLISHING.md)
incluye el ZIP preparado y el paso de presentación con identidad de desarrollador
verificada. [README en inglés](README.md) contiene el detalle técnico.
