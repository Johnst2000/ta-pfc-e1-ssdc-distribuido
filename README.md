# SSDC distribuido — Proyecto Fin de Curso (Aplicaciones Distribuidas)

Evolución del **Sistema de Selección Docente y Convocatorias (SSDC)** de la Universidad Técnica Estatal de Quevedo (UTEQ) hacia una arquitectura distribuida. El SSDC nació como proyecto de la asignatura Aplicaciones Web (monolito en capas con Angular, Spring Boot y PostgreSQL); en este periodo se rediseña como sistema distribuido.

- **Asignatura:** Aplicaciones Distribuidas (ISR-701), Carrera de Software, 7.º semestre, paralelo A
- **Docente:** Gleiston C. Guerrero-Ulloa, PhD
- **Periodo:** SPA 2026–2027
- **Entrega actual:** TA-PFC-E1 — Propuesta y análisis del sistema distribuido (Semana 5)

## Integrantes y roles (equipo CHRS)

| Integrante | Usuario de GitHub | Rol |
|---|---|---|
| Silva Triviño John Jairo | Johnst2000 | Líder de Desarrollo |
| Herrera Barco Humberto Aldair | aldhair00 | Responsable de Documentación |
| Reinoso Vélez Eduardo David | ereinosov | Arquitecto |
| Calderón Saltos Joseph Alexander | JosephACS | Responsable de Calidad |

## Estructura del repositorio

```
/src/                servicios del esqueleto
/docs/               documento LaTeX (.tex, .bib), figuras y PDF compilado
/docs/adr/           registros de decisiones de arquitectura (ADR)
/docs/diagramas/     diagramas editables (.drawio)
/evidencias/         acta o encuesta, fotografías y capturas
BITACORA.md          registro de las sesiones de trabajo
README.md            este archivo
```

## Cómo compilar el documento

- **Compilador:** pdfLaTeX con biblatex y biber (TeX Live o MiKTeX; paquetes: biblatex, csquotes, babel, tabularx, booktabs, graphicx).
- **Archivo principal:** `docs/main.tex`
- **Orden de comandos**, desde la carpeta `docs/`:

```
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Cómo ejecutar el esqueleto

Requisito: Docker Desktop abierto. Desde la carpeta `src/`:

```
docker compose up --build
```

Se levantan dos servicios que se comunican por HTTP: `convocatorias` (puerto 8081) y `notificaciones` (puerto 8082). Las pruebas paso a paso están en [`src/README.md`](src/README.md).

## Video

Video de la entrega TA-PFC-E1 (5 a 7 minutos, los cuatro integrantes): **ENLACE PENDIENTE**

## Evidencias

- Entrevistas (audio): `evidencias/Decano.m4a`, `evidencias/Coordinadora p1.m4a`, `evidencias/Coordinadora p2.m4a`
- Sesiones de diseño y bosquejo: `evidencias/`
- Capturas del esqueleto en ejecución: `evidencias/01-servicios-en-marcha.png`, `02-comunicacion-entre-servicios.png`, `03-tolerancia-a-fallos.png`

## Seguridad

Este repositorio no contiene contraseñas, tokens, claves ni datos personales. La configuración sensible se entrega por variables de entorno.
