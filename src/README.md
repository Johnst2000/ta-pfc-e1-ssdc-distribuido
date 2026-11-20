# src

Esqueleto funcional del SSDC distribuido: dos servicios mínimos que se comunican por HTTP. No tiene lógica de negocio; solo demuestra que la base técnica funciona.

| Servicio | Puerto | Qué hace |
|---|---|---|
| `convocatorias` | 8081 | Lista convocatorias de ejemplo y, al publicar una, avisa a notificaciones |
| `notificaciones` | 8082 | Recibe avisos y los lista |

Los nombres y puertos son provisionales hasta cerrar el ADR-002 (mecanismo de comunicación).

## Cómo ejecutarlo

Requisito: Docker Desktop abierto. Desde la carpeta `src/`:

```
docker compose up --build
```

## Probarlo (en otra terminal)

Estado de los servicios (en Windows PowerShell usa `curl.exe` en vez de `curl`):

```
curl http://localhost:8081/health
curl http://localhost:8082/health
```

Ver las convocatorias y publicar la 1:

```
curl http://localhost:8081/convocatorias
curl -X POST http://localhost:8081/convocatorias/1/publicar
```

La respuesta debe decir `"notificacion": "enviada"`. Comprobar que el otro servicio recibió el aviso:

```
curl http://localhost:8082/notificaciones
```

## Prueba de tolerancia a fallos

1. Detener notificaciones: `docker stop ssdc-notificaciones`
2. Publicar la convocatoria 2: `curl -X POST http://localhost:8081/convocatorias/2/publicar`
3. Convocatorias sigue funcionando y responde `"notificacion": "pendiente"`.
4. Volver a levantarlo: `docker start ssdc-notificaciones`

## Detener todo

```
docker compose down
```

## Limitaciones conocidas

- Los datos están en memoria; al reiniciar se pierden.
- Si notificaciones está caído, el aviso queda en estado `pendiente` y no se reintenta: ese es justo el problema que resolverá el mecanismo del ADR-002.
