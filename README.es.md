# Typography Studio — español

Skill abierta y plugin de Codex para **diseñar fuentes tipográficas y revisar
su calidad visual**. Versión **0.4.1**, con instrucciones, diez referencias,
plantillas y herramientas de prueba en español. También conserva el inglés.
Es independiente de marcas, familias concretas y estilos obligatorios.

[English](https://github.com/martinsantos/typography-studio/blob/v0.4.1/README.md) · [Instrucciones de la skill](plugins/typography-studio/skills/typography-design-review/SKILL.es.md) ·
[Fuentes consultadas](plugins/typography-studio/skills/typography-design-review/references/sources.es.md)

## Descargar e instalar

[La release 0.4.1](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.1)
contiene tres paquetes en español:

- **Skill:** `typography-studio-0.4.1-skill-es.zip`. Extraelo en tu proyecto;
  la entrada queda en `.agents/skills/typography-design-review/SKILL.md`.
- **Plugin:** `typography-studio-0.4.1-plugin-es.zip`. Tiene manifiesto,
  instrucciones e interfaz en español, preparado para importación compatible
  y presentación al catálogo.
- **Marketplace:** `typography-studio-0.4.1-marketplace-es.zip`. Extraelo en
  una carpeta nueva e instalalo con los comandos siguientes.

```sh
codex plugin marketplace add /ruta/absoluta/typography-studio
codex plugin add typography-studio@typography-studio-marketplace
```

La ruta corresponde a la carpeta extraída con `.agents/plugins/marketplace.json`.
Elegí la edición inglesa o española: ambas utilizan la misma identidad
`typography-studio` y la misma skill `$typography-design-review`.
[Guía completa de instalación y publicación](docs/PUBLISHING.es.md).

## Pedir un trabajo

> Usá $typography-design-review para construir una sans de títulos clara y
> fuerte. Empezá por H/O/n/o y revisá palabras reales antes de ampliar el repertorio.

> Usá $typography-design-review para revisar esta fuente: curvas, espaciado,
> puntuación, jerarquía, ancho de lectura e interlineado. Mostrá las pruebas
> visuales y registrá los límites de la revisión.

El agente debe responder en tu idioma y abrir las imágenes para sostener
sus juicios visuales. La skill trabaja con las fuentes y el editor de tu proyecto.

## Pruebas visuales en español

```sh
python scripts/build_proof.py /ruta/a/fuente.ttf --language es --output /ruta/a/prueba-nueva.html
node scripts/capture_proof.mjs /ruta/a/prueba-nueva.html /ruta/a/capturas-nuevas
```

Ejecutá desde la carpeta de la skill. El ZIP español selecciona español
por defecto; `--language en` permite cambiarlo. El HTML traduce rótulos,
mensajes de carga y avisos de caracteres ausentes. Los párrafos de prueba
conservan su idioma, y el corpus sigue cubriendo español e inglés.
Los auxiliares opcionales requieren FontTools y, para capturar, Node/Playwright.
[Preparación de herramientas](plugins/typography-studio/skills/typography-design-review/references/tooling.es.md).

## Alcance de la revisión

- Construcción y tono se juzgan según el propósito del usuario.
- Dibujo, espaciado, exportación y composición se comprueban por separado.
- Tamaños, altura aparente, interlineado y líneas se revisan sobre pruebas reales.
- Los perfiles iniciales son ajustables.
- Cada conclusión identifica archivo, imagen, tamaño y contexto observado.

[Plantilla de propósito](plugins/typography-studio/skills/typography-design-review/assets/brief-template.es.md) ·
[Ficha de revisión](plugins/typography-studio/skills/typography-design-review/assets/review-template.es.md) ·
[Registro de práctica](plugins/typography-studio/skills/typography-design-review/assets/practice-template.es.md).

MIT permite usar, modificar y redistribuir el paquete. Las fuentes aportadas
conservan su licencia. No se distribuyen fuentes ni PDF de terceros.
[Contribuir](CONTRIBUTING.es.md) · [Validación](docs/VALIDATION.es.md).
La publicación en GitHub está separada de la presentación y revisión
para el catálogo de OpenAI.
