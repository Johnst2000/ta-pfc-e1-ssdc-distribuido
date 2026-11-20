"""Servicio de notificaciones (esqueleto). Sin lógica de negocio: recibe y lista avisos."""
import json
import os
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer

PUERTO = int(os.environ.get("PORT", "8082"))
AVISOS = []  # en memoria: solo para demostrar la comunicación entre servicios


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
            self._responder(200, {"servicio": "notificaciones", "estado": "ok"})
        elif self.path == "/notificaciones":
            self._responder(200, {"total": len(AVISOS), "avisos": AVISOS})
        else:
            self._responder(404, {"error": "ruta no encontrada"})

    def do_POST(self):
        if self.path != "/notificaciones":
            self._responder(404, {"error": "ruta no encontrada"})
            return
        largo = int(self.headers.get("Content-Length", 0))
        try:
            aviso = json.loads(self.rfile.read(largo) or b"{}")
        except json.JSONDecodeError:
            self._responder(400, {"error": "JSON inválido"})
            return
        aviso["recibido_en"] = datetime.now(timezone.utc).isoformat()
        AVISOS.append(aviso)
        print(f"[notificaciones] aviso recibido: {aviso}", flush=True)
        self._responder(201, {"estado": "registrado", "aviso": aviso})


if __name__ == "__main__":
    print(f"[notificaciones] escuchando en el puerto {PUERTO}", flush=True)
    HTTPServer(("0.0.0.0", PUERTO), Manejador).serve_forever()
