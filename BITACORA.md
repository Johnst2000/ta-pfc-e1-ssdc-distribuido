# Bitácora del equipo CHRS

Registro de las sesiones de trabajo del equipo (fecha, integrantes presentes, decisiones tomadas y problemas resueltos).

---

## 18 de noviembre de 2026 — Planificación inicial de TA-PFC-E1

**Registrado por:** John Silva Triviño
**Presentes:** John Silva Triviño

**Decisiones**

- Se parte del SSDC (proyecto de Aplicaciones Web) como línea base y se evoluciona a una arquitectura distribuida.
- Se crea este repositorio público nuevo; no se usa CHRSweb como repositorio de entrega.
- Roles propuestos: Líder de Desarrollo (John), Responsable de Documentación (Aldair), Arquitecto (Eduardo) y Responsable de Calidad (Joseph). Quedan pendientes de confirmación del grupo.
- FORM-TL-02 y FORM-IC-01 no se consideran requisito, según la respuesta del docente en el grupo de WhatsApp.
- Para los riesgos de FORM-AC-01, cada integrante usará el incidente que analizó en su equipo, citando el informe oficial de su caso.

## 18 de noviembre de 2026 — Plantilla de ADR

**Registrado por:** Eduardo Reinoso Vélez
**Presentes:** Eduardo Reinoso Vélez

**Trabajo realizado**

- Se agrega `docs/adr/PLANTILLA-ADR.md` con los cuatro apartados que pide la tarea (contexto, opciones, decisión y consecuencias), para usarla en el ADR-001 y el ADR-002.

## 19 de noviembre de 2026 — Fila de riesgo R4

**Registrado por:** Eduardo Reinoso Vélez
**Presentes:** Eduardo Reinoso Vélez

**Trabajo realizado**

- Se agrega `docs/secciones/12_riesgo_R4.tex` con la fila R4 del análisis de riesgos, basada en el incidente de Amazon S3 (28 de febrero de 2017).
- Se comprobó en el repositorio CHRSweb que `spring.jpa.hibernate.ddl-auto=update` está activo (línea 56 de `application.properties`).
- Uso de IA: Claude (Sonnet 5.5) para verificar el dato en el código y el informe de AWS.

## 19 de noviembre de 2026 — Criterios de calidad

**Registrado por:** Joseph Calderón Saltos
**Presentes:** Joseph Calderón Saltos

**Trabajo realizado**

- Agregué `docs/secciones/06_requisitos_rnf.tex` con cuatro requisitos de calidad propuestos y sus criterios de aceptación y verificación.
- Dejé indicados los puntos que deben confirmarse después de la entrevista y cuando se defina la arquitectura.

**Commit:** `e93b938` — Define criterios de calidad del SSDC

## 19 de noviembre de 2026 — Entrevistas para el levantamiento de requisitos

**Registrado por:** Aldair Herrera Barco
**Presentes:** (quiénes estuvieron)

**Trabajo realizado**

- Entrevista al Decano de la carrera. Medio: presencial.
- Entrevista a la Coordinadora de la carrera, grabada en dos partes.
- Los audios están en `/evidencias/`.

**Pendiente**

- Resumen de cifras y tabla de trazabilidad requisito → entrevista.

## 20 de noviembre de 2026 — Estado preliminar de requisitos de calidad

**Registrado por:** Joseph Calderón Saltos  
**Presentes:** Joseph Calderón Saltos

**Trabajo realizado**

- Se amplió `docs/secciones/06_requisitos_rnf.tex` con el estado preliminar de RNF-01 a RNF-04, tomando como referencia el comportamiento y las limitaciones descritos en `docs/secciones/09_comunicacion.tex`.
- Se indicaron las comprobaciones pendientes. No se realizaron pruebas nuevas.

**Commit:** `b2ec0a2` — Añadido estado preliminar de requisitos de calidad

## 20 de noviembre de 2026 — Bosquejo, diagramas C4, ADR y justificación

**Registrado por:** Eduardo Reinoso Vélez
**Presentes:** Eduardo Reinoso Vélez

**Trabajo realizado**

- Se agrega `evidencias/bosquejo-arquitectura-1-2026-11-20.jpg`, el primer bosquejo a mano de la arquitectura (commit `6762d58`). Lo dibujó Eduardo a partir de una propuesta inicial de estructura redactada con ayuda de Claude. Es una propuesta individual, para discutir con el equipo.
- Se agregan los diagramas C4 de contenedores (`6ce954d`) y de contexto (`1500c83`), en `.drawio` y PNG. El de contenedores es la versión limpia del bosquejo: los servicios que guardan datos tienen su propia base PostgreSQL, la comunicación entre `convocatorias` y `notificaciones` es HTTP como en el esqueleto, y la cola de mensajes queda como componente planeado, pendiente del ADR-002.
- Se agregan el ADR-001 y la sección 07 (`a0a01d4`), y el ADR-002 con las secciones 08 y 11 (`74ecef5`). No incluyen mediciones ni cifras de la entrevista, que no estaban en el repositorio.
- Uso de IA: Claude (Sonnet 5.5) propuso la estructura inicial, redactó los borradores de los ADR y de las secciones 07, 08 y 11, y generó los archivos `.drawio` de los diagramas. Eduardo dibujó el bosquejo a mano, y revisó y ajustó los borradores.

## 21 de noviembre de 2026 — Actualización de calidad y riesgos

**Registrado por:** Joseph Calderón Saltos
**Presentes:** Joseph Calderón Saltos

**Trabajo realizado**

- Se actualizaron los RNF-01 a RNF-06 y su trazabilidad con las entrevistas y con ISO/IEC 25010.
- Se amplió la sección de trabajos relacionados con un cuarto estudio sobre selección docente y su referencia.
- Se documentó el análisis CAP/PACELC para datos críticos del SSDC.
- Se incorporó el riesgo R1 en un archivo propio y se conservó el archivo de R4.

**Commits:** `418437c`, `33b7008`, `ef81eca`, `895ef42`, `720a04f`, `239842a`, `7333b29`, `7d9299f`, `1d1ba4c`, `2a9fbd6`, `c516cc6`, `11daa69`, `a222aa6`, `d47cf90`.

## 21 de noviembre de 2026 — Revisión de los ADR y video

**Registrado por:** Eduardo Reinoso Vélez
**Presentes:** Eduardo Reinoso Vélez

**Trabajo realizado**

- El ADR-001 fue revisado por el equipo CHRS y el ADR-002 por John Silva Triviño. Ambos pasan de estado «propuesto» a «aceptado» y se actualiza el campo «Revisado por».
- Eduardo grabó su parte del video (diagramas C4 y ADR), a la espera de unirla con las partes de los demás integrantes en un único video.
- Sesión de diseño del equipo por llamada: estuvimos los cuatro integrantes (Joseph Calderón Saltos, Aldair Herrera Barco, Eduardo Reinoso Vélez y John Silva Triviño). Revisamos juntos el bosquejo de la arquitectura y el diagrama C4 de contenedores. Capturas: `evidencias/sesion-diseno-1-bosquejo-2026-11-21.jpeg` y `evidencias/sesion-diseno-2-c4-nivel2-2026-11-21.jpeg`.

## 21 de noviembre de 2026 — Cierre de aportes de calidad

**Registrado por:** Joseph Calderón Saltos  
**Presentes:** Joseph Calderón Saltos

**Trabajo realizado**

- Se ampliaron los trabajos relacionados y las referencias bibliográficas.
- Se completó mi análisis CAP/PACELC y se agregaron los riesgos R2 (Meta) y R3 (Fastly) en archivos separados.
- Se registraron mis entregables con sus issues y commits en `docs/secciones/14_aportes_ia.tex`.
- Grabé mi parte del video sobre los requisitos de calidad y el análisis CAP/PACELC.

**Commits:** `5a0e6d75`, `9bda3b80`, `a67e73fd`, `62f0f4bc`.

## 21 de noviembre de 2026 — Integración del documento

**Registrado por:** Aldair Herrera Barco
**Presentes:** Aldair Herrera Barco

**Trabajo realizado**

- Redacté la sección 02 (contexto) a partir de las entrevistas y compilé el primer PDF.
- Agregué las secciones 01 (resumen), 03 (objetivos) y 05 (requisitos funcionales con trazabilidad a las entrevistas).
- Integré en `main.tex` las secciones 01 a 05, 10, 14 y los riesgos R1 a R5.
- Agregué mi subsección de aportes y uso de IA en la sección 14.
- Grabé mi parte del video.

**Problemas resueltos**

- Conflictos al hacer `pull` por cambios simultáneos en `main.tex` y en la sección 14; se resolvieron con `git stash` y `pull --rebase`.
