# Circulación en directorios

## Estado actual

- Fuente y release públicas: [Typography Studio 0.4.1](https://github.com/martinsantos/typography-studio/releases/tag/v0.4.1).
- CLI Skills 1.7.1: el 2026-10-08 se comprobó que detecta una skill,
  `typography-design-review`. La prueba usó `--list` con telemetría desactivada;
  no fue una instalación comunitaria ni un alta en el directorio.
- OpenAI: ZIP 0.4.1 cargado como borrador el 2026-10-08. Los controles
  automáticos de metadatos y skill siguen pendientes; todavía no se presentó
  a revisión ni se publicó en el directorio.
- Agent Skill Index: [PR #559](https://github.com/heilcheng/awesome-agent-skills/pull/559)
  enviado con entradas españolas e inglesas; revisión del mantenedor pendiente.

[English](DISTRIBUTION.md).

## Directorio de Plugins de OpenAI

Abrí [Plugins](https://platform.openai.com/plugins), seleccioná la organización
y proyecto, y completá la identidad de publicación verificada. Subí
`typography-studio-0.4.1-plugin.zip`: contiene recursos españoles y
traducciones de la ficha. Resolvé los controles de metadatos y skills,
presentá a revisión y publicá la versión aprobada.

Es un plugin compuesto por una skill. Seguí las
[instrucciones oficiales](https://developers.openai.com/plugins/deploy/submission)
y revisá las declaraciones del panel antes de presentar.
La release en GitHub y la detección del CLI son pasos separados de la aprobación
del directorio de OpenAI.

## skills.sh

El comando para compartir es:

```sh
npx skills add martinsantos/typography-studio --skill typography-design-review
```

La [FAQ oficial](https://www.skills.sh/docs/faq) indica que el directorio
incorpora skills mediante instalaciones reales registradas por la telemetría
anónima del CLI. Detectar con `--list` verifica el repositorio, pero no
demuestra que ya esté indexado. Mostrá una prueba real e invitá a primeros
usuarios a probarlo y dejar comentarios.

## Presentación a un índice comunitario

[Agent Skill Index](https://github.com/heilcheng/awesome-agent-skills/blob/main/CONTRIBUTING.md)
acepta incorporaciones de metadatos mediante pull request. El [PR #559](https://github.com/heilcheng/awesome-agent-skills/pull/559)
añade entradas españolas e inglesas que enlazan a nuestra fuente. Su aceptación
sigue pendiente. El [material de presentación](COMMUNITY_PROPOSAL.md) incluye
las entradas exactas, la descripción y dos ejemplos de uso.

- Nombre: Typography Studio
- Skill: `typography-design-review`
- Plataforma comprobada: Codex
- Descripción: Diseño y revisión tipográfica con pruebas renderizadas reales.
- Fuente: [repositorio](https://github.com/martinsantos/typography-studio)
- Implementación: [entrada de la skill](https://github.com/martinsantos/typography-studio/blob/v0.4.1/plugins/typography-studio/skills/typography-design-review/SKILL.md)
- Idiomas: español e inglés
- Licencia: MIT

[VoltAgent](https://github.com/VoltAgent/awesome-agent-skills/blob/main/CONTRIBUTING.md)
pide uso comunitario real y no acepta skills recién creadas.
Lo consideramos después de conseguir primeras instalaciones y comentarios.
La aceptación depende de cada mantenedor.

## Texto breve de difusión

Typography Studio ayuda a agentes a diseñar y revisar fuentes con archivos
editables y pruebas renderizadas reales: glifos, espaciado, kerning, familias
y jerarquía de lectura. Recursos en español e inglés, herramientas locales
opcionales y licencia MIT.
