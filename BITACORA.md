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
- Para los riesgos de FORM-AC-01, cada integrante usará el incidente que analizó en su equipo, citando el informe oficial de su caso (el docente lo aceptó).

**Problemas detectados**
- El repositorio CHRSweb tiene secretos en texto plano en `application.properties` y una carpeta `uploads/` con archivos de cédulas. No se copian a este repositorio y se avisará a quien administra CHRSweb.
