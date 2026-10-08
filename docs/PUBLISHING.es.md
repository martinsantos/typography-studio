# Distribución y publicación

[English](https://github.com/martinsantos/typography-studio/blob/v0.4.1/docs/PUBLISHING.md). El repositorio público y las releases están en
[GitHub](https://github.com/martinsantos/typography-studio).

## Fuente pública y marketplace

La versión 0.4.1 incluye ediciones inglesa y española con la misma identidad
de plugin y skill. Para la española, descargá
`typography-studio-0.4.1-marketplace-es.zip` desde la
[release](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.1)
y extraelo en una carpeta nueva. En un cliente Codex compatible:

```sh
codex plugin marketplace add /ruta/absoluta/typography-studio
codex plugin add typography-studio@typography-studio-marketplace
```

La ruta debe ser la carpeta extraída que contiene
`.agents/plugins/marketplace.json`. La edición española ya incorpora
instrucciones, referencias, plantillas, metadatos y pruebas en español.
Conserva los comandos y los identificadores técnicos.

Para instalar desde el repositorio público:

```sh
codex plugin marketplace add martinsantos/typography-studio --ref v0.4.1
codex plugin add typography-studio@typography-studio-marketplace
```

Ese marketplace contiene ambos idiomas y sigue el idioma del usuario;
los ZIP españoles seleccionan también los metadatos de interfaz y los
valores predeterminados en español.

La skill independiente se instala extrayendo
`typography-studio-0.4.1-skill-es.zip` en el proyecto: su entrada queda en
`.agents/skills/typography-design-review/SKILL.md`.
Al actualizar una instalación propia, revisá sus cambios antes de sustituirla.

## Generar los archivos

Para mantener o generar releases, cloná el repositorio público. Los ZIP
españoles son paquetes de instalación; los scripts de mantenimiento están
en el código fuente canónico. Desde ese checkout, Python 3.10+ y la biblioteca
estándar alcanzan para empaquetar:

```sh
python3 scripts/validate.py
python3 scripts/check_localization.py
python3 scripts/check_publisher.py
python3 scripts/package.py --output dist
```

La salida contiene seis ZIP: skill, plugin y marketplace en inglés y en español,
además de `SHA256SUMS` y `package-manifest.json`.
Cada idioma utiliza los mismos auxiliares y licencia MIT.

`scripts/publish.py --execute` sirve para una publicación inicial en un
repositorio vacío. Protege cambios, historial y salidas existentes.
Para una versión posterior, trabajá en una rama, validá y revisá el cambio,
integralo por pull request y publicá una etiqueta nueva con los archivos
y sus hashes. Conservá las etiquetas y descargas anteriores.

## Catálogo público de OpenAI

La distribución en GitHub no equivale a aprobación del catálogo.
El ZIP `typography-studio-0.4.1-plugin-es.zip` contiene
`.codex-plugin/plugin.json`, `skills/`, iconos y licencia en su raíz,
con interfaz e instrucciones españolas.

1. Iniciá sesión en el panel de desarrollador y elegí organización y proyecto.
   Se requiere la identidad individual o empresarial verificada y los permisos
   de publicación indicados por el panel.
2. Abrí Plugins, subí el ZIP y seleccioná la identidad verificable del editor.
3. Resolvé las comprobaciones y confirmá la categoría ofrecida.
   [El material de presentación](SUBMISSION.es.md) aporta textos y alcance.
4. Presentá a revisión y completá las declaraciones y condiciones de la plataforma.
5. Tras la aprobación, publicá y registrá URL pública, versión y comprobante.

El paquete contiene solo skills. No necesita un servidor MCP ni una cuenta
propia. Subir, presentar, aprobar y publicar son estados distintos.
Las condiciones vigentes deben verificarse al realizar la presentación:

[Empaquetado](https://developers.openai.com/plugins/build/plugins) ·
[Presentación](https://developers.openai.com/plugins/deploy/submission) ·
[Directrices](https://developers.openai.com/plugins/plugin-guidelines).

## Comprobar una entrega

Validá estructura y enlaces; compará los hashes de los ZIP descargados con
el manifiesto. Para cambios en herramientas, probá una fuente con licencia
fuera del paquete, caracteres ausentes y rechazo de salidas existentes.
Abrí las capturas antes de registrar hallazgos visuales.
Los ejercicios de comportamiento propuestos no son pruebas ejecutadas.
