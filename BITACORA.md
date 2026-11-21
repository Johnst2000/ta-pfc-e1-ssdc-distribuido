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
