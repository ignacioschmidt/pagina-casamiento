# Plan: Rediseño completo de la página de casamiento

**Created:** 2026-02-28
**Status:** pending

## Context

Rediseño estructural de `index.html`. Se eliminan secciones repetidas/innecesarias y se reestructura el hero con foto apaisada, nombres en una línea, venues con links, countdown y botón sutil. El orden final es: Hero → Dress Code → Foto → Regalos (sin footer). El archivo es un único HTML con estilos y JS inline.

## Steps

- [ ] 1. **Reestructurar el hero (`#hero`)** en `index.html`
  - Eliminar la botánica superior (`.hero-top-botanical`) y la franja floral inferior (`.hero-floral-bottom`)
  - Agregar un `<img>` placeholder para la foto de la pareja con aspecto apaisado (aspect-ratio ~16/9 o ~3/1), con un src placeholder que el usuario reemplazará después
  - Cambiar `.hero-names` para que "Toia & Nachi" quede en una sola línea: quitar el `<br>` implícito del `&` y ajustar font-size con clamp para que no salte de línea en mobile
  - Eliminar `.hero-hand-date` (la fecha "9 de mayo · 2026" de arriba)
  - Eliminar `.hero-tagline` ("y lo vamos a celebrar con todo")
  - Mantener `.hero-venues` con Iglesia Santa Rita y Espacio Pilar, agregar links `<a>` de "ver ubicación" debajo de cada venue (reusar los links de Google Maps existentes del `#info`)
  - Mantener el countdown tal cual
  - Cambiar el botón "Confirmar asistencia" del hero: quitar `width:100%;display:block`, hacerlo `display:inline-block` con `width:auto`, usar clase `.btn` (borde + transparente) en lugar de `.btn-primary`

- [ ] 2. **Eliminar sección `#intro`** (líneas ~620-625: "finalmente... dijimos que sí")
  - Borrar todo el `<section id="intro">` y sus estilos CSS asociados (#intro, .intro-eyebrow, .intro-heading, .intro-secondary)

- [ ] 3. **Eliminar el divider SVG** que está entre `#intro` y `#info` (líneas ~628-638)

- [ ] 4. **Eliminar sección `#info`** (líneas ~641-693: "El plan del día" con ceremonia y fiesta)
  - Borrar todo el `<section id="info">` y sus estilos CSS (#info, .info-botanical, .info-grid, .info-card, .info-separator, etc.)

- [ ] 5. **Eliminar el divider SVG** que está entre `#info` y `#couple-photo` (líneas ~696-706)

- [ ] 6. **Reordenar secciones restantes** para que queden en este orden:
  - Hero (ya modificado con venues + countdown + botón confirmar)
  - Dress Code (`#dresscode`)
  - Foto banner (`#couple-photo`)
  - Regalos (`#regalo`)

  Esto implica mover `#dresscode` antes de `#couple-photo` (actualmente está después). Y eliminar el divider mauve que estaba antes de dresscode.

- [ ] 7. **Eliminar sección `#rsvp`** (líneas ~765-782: el segundo "Confirmar asistencia")
  - Borrar `<section id="rsvp">` completo y sus estilos CSS (#rsvp)

- [ ] 8. **Eliminar el footer** completo (líneas ~799-808)
  - Borrar `<footer>` y sus estilos CSS (footer, .footer-floral-border, .footer-content, .footer-names, .footer-year, .footer-closing)

- [ ] 9. **Limpiar CSS huérfano**
  - Remover estilos de: `.hero-top-botanical`, `.hero-floral-bottom`, `.hero-hand-date`, `.hero-tagline`, `.hero-rule`, `.intro-*`, `#info`, `.info-*`, `#rsvp`, `footer`, `.footer-*`
  - Mantener estilos de: `.hero-venues`, `.countdown`, `.cd-*`, `#dresscode`, `#couple-photo`, `#regalo`, modales, botones, y todo el CSS base

- [ ] 10. **Agregar CSS para la foto hero apaisada**
  - Nuevo estilo `.hero-photo` con aspect-ratio apaisado (~2.5/1 o ~3/1), width 100%, object-fit cover
  - Asegurar que todo el hero (foto + nombres + venues + countdown + botón) sea visible sin scroll en viewport estándar mobile (ajustar paddings)

- [ ] 11. **Verificar que no quede JS roto**
  - La función `openRsvpModal()` sigue siendo necesaria (el botón del hero la usa)
  - Las funciones de modales, copy y countdown se mantienen intactas
  - No debería haber referencias rotas ya que las secciones eliminadas no tenían JS propio

## Files likely affected

| File | Reason |
|------|--------|
| `index.html` | Único archivo — todo el HTML, CSS y JS inline. Se eliminarán secciones, se reestructurará el hero, se reordenarán secciones, se limpiará CSS |

## Open questions / risks

- La foto de la pareja para el hero aún no fue pasada — se dejará un `<img>` con `src` placeholder (`img/hero.jpeg`) para que el usuario la reemplace
- Asegurar que el hero completo (foto + nombres + venues + countdown + botón) quepa sin scroll en mobile puede requerir ajustes de tamaños después de ver el resultado real
- Los dividers SVG entre las secciones restantes (dresscode → foto → regalos): ¿se mantienen, se agregan nuevos, o se deja sin dividers? → Por defecto los elimino todos para un look más limpio

## After execution

- [ ] Abrir `index.html` en browser y verificar visualmente
- [ ] Verificar en mobile (o DevTools responsive) que el hero no requiere scroll
- [ ] Verificar que modales (RSVP + regalo) siguen funcionando
- [ ] Update `.claude/memory/repo-context.md` to reflect structural changes
