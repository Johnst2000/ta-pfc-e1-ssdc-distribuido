"""Servicio de convocatorias (esqueleto). Al publicar una convocatoria avisa al servicio de
notificaciones por HTTP. Si notificaciones no responde, convocatorias sigue funcionando."""
import json
import os
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

PUERTO = int(os.environ.get("PORT", "8081"))
URL_NOTIFICACIONES = os.environ.get("NOTIFICACIONES_URL", "http://localhost:8082")

CONVOCATORIAS = {
    1: {"id": 1, "titulo": "Convocatoria de ejemplo - Software", "estado": "borrador"},
    2: {"id": 2, "titulo": "Convocatoria de ejemplo - Redes", "estado": "borrador"},
}


def avisar(convocatoria):
    """Envía el evento al servicio de notificaciones. Devuelve 'enviada' o 'pendiente'."""
    cuerpo = json.dumps({
        "tipo": "ConvocatoriaPublicada",
        "convocatoriaId": convocatoria["id"],
        "titulo": convocatoria["titulo"],
    }).encode("utf-8")
    peticion = urllib.request.Request(
        URL_NOTIFICACIONES + "/notificaciones", data=cuerpo,
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(peticion, timeout=2):
            return "enviada"
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        print(f"[convocatorias] notificaciones no disponible: {error}", flush=True)
        return "pendiente"


class Manejador(BaseHTTPRequestHandler):
    def _responder(self, codigo, cuerpo):
        datos = json.dumps(cuerpo, ensure_ascii=False).encode("utf-8")
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(datos)))
        self.end_headers()
        self.wfile.write(datos)

    def do_GET(self):
        if self.path == "/health":
            self._responder(200, {"servicio": "convocatorias", "estado": "ok"})
        elif self.path == "/convocatorias":
            self._responder(200, list(CONVOCATORIAS.values()))
        else:
            self._responder(404, {"error": "ruta no encontrada"})

    def do_POST(self):
        partes = self.path.strip("/").split("/")
        if len(partes) == 3 and partes[0] == "convocatorias" and partes[2] == "publicar" \
                and partes[1].isdigit() and int(partes[1]) in CONVOCATORIAS:
            convocatoria = CONVOCATORIAS[int(partes[1])]
            convocatoria["estado"] = "publicada"
            aviso = avisar(convocatoria)
            self._responder(200, {"convocatoria": convocatoria, "notificacion": aviso})
        else:
            self._responder(404, {"error": "ruta no encontrada"})


if __name__ == "__main__":
    print(f"[convocatorias] escuchando en el puerto {PUERTO}", flush=True)
    HTTPServer(("0.0.0.0", PUERTO), Manejador).serve_forever()
