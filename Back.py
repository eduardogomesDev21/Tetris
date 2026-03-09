import http.server
import socketserver
import webbrowser
import os

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.path = '/Front.html'
        return super().do_GET()

    def end_headers(self):
        # Desabilita o cache para facilitar o desenvolvimento
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

def run_server():
    print("=" * 50)
    print(" 👾 INICIANDO SERVIDOR CYBERPUNK TETRIS 👾 ")
    print("=" * 50)
    print(f"Servidor rodando porta: {PORT}")
    print(f"Acesse no navegador: http://localhost:{PORT}")
    print("Pressione CTRL+C para desligar o servidor.")
    print("=" * 50)
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            # Tenta abrir o navegador automaticamente
            webbrowser.open(f'http://localhost:{PORT}')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🔌 Servidor finalizado. Câmbio desligo!")
    except OSError as e:
        print(f"\n❌ Erro ao iniciar na porta {PORT}: {e}")
        print("A porta pode já estar em uso. Tente usar uma porta diferente.")

if __name__ == '__main__':
    run_server()
