# Repo Context

**Project:** Página de casamiento — Toia & Nachi
**Stack:** HTML / CSS / JS estático (sin build tools, sin frameworks)
**Last updated:** 2026-02-28

## Overview

Sitio de invitación de casamiento para Toia & Nachi, boda el **9 de mayo de 2026**. Es un único archivo `index.html` con todos los estilos y scripts inline. No tiene backend conectado; el RSVP muestra un estado local de éxito (pendiente integración con Formspree). El sitio incluye modales para RSVP y datos bancarios de regalo.

## Directory structure

| Path | Purpose |
|------|---------|
| `index.html` | Página completa — HTML, CSS y JS en un solo archivo |
| `img/` | Imágenes: fotos de la pareja + decorativas |
| `generar-imagenes.py` | Script Python para generar nuevas imágenes via Replicate API (FLUX Schnell) |
| `.claude/` | Configuración, planes y memoria de Claude Code |

## Key files

| File | Role |
|------|------|
| `index.html` | Todo el sitio — secciones, estilos, modales, JS |
| `img/hero.jpeg` | Foto principal apaisada del hero (pareja bajo puente, object-position: center 85%) |
| `img/01.jpg` | Imagen decorativa entre hero y dresscode |
| `img/02.jpg` | Imagen decorativa entre dresscode y foto banner |
| `img/03.jpg` | Imagen decorativa entre foto banner y regalos |
| `img/foto-banner.jpeg` | Foto de la pareja en sección banner central |
| `img/regalo.png` | Ícono de regalo — sección regalos (320×320, sin fondo) |
| `img/FONDO.png` | Imagen de fondo del hero (cover, opacity 0.45) |
| `img/DIVISOR DRESS CODE.png` | Divisor visual entre hero y dress code |

## Architecture

Sitio 100% estático de una sola página. Estructura de secciones:

1. **#hero** — Foto apaisada (hero.jpeg), nombres ("Toia & Nachi" en una línea), venues side-by-side con links "ver ubicación", countdown en vivo, botón sutil RSVP. Sin decoraciones botánicas.
2. **#dresscode** — Código de vestimenta "Elegante", con divisor decorativo entre hero y dresscode
3. **#couple-photo** — Banner con foto de la pareja (foto-banner.jpeg)
4. **#regalo** — Datos bancarios (abre modal)

**Sin footer.** La página termina en la sección de regalos.

**Modales:** `#modal-rsvp` (formulario de confirmación) y `#modal-gift` (datos bancarios con copy-to-clipboard).

## CSS / Diseño

**Fuentes Google:**
- `Cormorant Garamond` — titulares y cuerpo serif
- `Dancing Script` — acentos handwritten (fecha, dresscode)
- `Jost` — sans-serif general

**Paleta (variables CSS + colores hardcodeados):**
```
--cream: #faf7f2   --warm: #f0ebe1    --stone: #c4b89a
--muted: #9c8e7a   --dark: #2a2218    --gold: #b09060
--sage: #7d9b82    --sage-light: #e8ede9
--mauve: #b8858f   --mauve-light: #f5edef
--terracotta: #b87560  --forest: #2d3d2e
```

**Colores específicos por sección (hardcodeados):**
| Elemento | Color |
|----------|-------|
| Nombres "Nachi & Toia" + fecha | `#898d75` |
| Venues (Iglesia, Espacio Pilar) + horarios | `#536749` |
| Cuenta regresiva (números) | `#7c829a` |
| Botón confirmar asistencia (texto y borde) | `#898d75` |
| Dress code (título) | `#898d75` |
| "Elegante" (subtítulo) | `#5b1d1d` |

## Build & test

```bash
# No build — abrir directamente en browser
open index.html
```

## Conventions

- Todo en `index.html` — no separar CSS/JS en archivos externos
- Fotos reales de la pareja: mantener en `img/` con nombres descriptivos
- Imágenes decorativas entre secciones: `img/01.jpg`, `img/02.jpg`, `img/03.jpg`
- Los datos bancarios en `#modal-gift` siguen siendo placeholders (CBU, alias, banco, titular)
- El form de RSVP no está conectado a backend — comentario en JS sugiere Formspree
- Botón de confirmar asistencia es sutil (borde, transparente, inline) — no full-width

## Change log

| Date | Change |
|------|--------|
| 2026-02-28 | Rediseño completo: hero con foto apaisada + venues side-by-side + countdown. Eliminadas secciones: intro, info/plan del día, segundo RSVP, footer. Orden final: Hero → Dresscode → Foto → Regalos. |
| 2026-02-28 | Nueva paleta cromática por sección. Fondo hero con FONDO.png. Divisor decorativo hero↔dresscode. Imagen regalo.png (320px) reemplaza botánica. Dress code: sans-serif uppercase para "Elegante". |
