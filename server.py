# Servidor local OPCIONAL del overlay de bonos.
# Los datos ya viven en Firebase: este servidor solo sirve las páginas
# para probar en local. En OBS puedes usar directamente el archivo
# overlay.html, y el panel está publicado en GitHub Pages.
#
# Ejecutar:  python server.py   (o doble clic en iniciar-overlay.bat)
#   Overlay:  http://localhost:5599/
#   Panel:    http://localhost:5599/panel
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

BASE = os.path.dirname(os.path.abspath(__file__))
PORT = 5599

RUTAS = {"/": "overlay.html", "/overlay": "overlay.html",
         "/panel": "index.html"}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)

    def do_GET(self):
        limpia = self.path.split("?")[0]
        if limpia in RUTAS:
            self.path = "/" + RUTAS[limpia]
        super().do_GET()

    def log_message(self, *args):
        pass  # sin ruido en la consola


if __name__ == "__main__":
    print(f"Overlay:  http://localhost:{PORT}/")
    print(f"Panel:    http://localhost:{PORT}/panel")
    print("Ctrl+C para parar.")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
