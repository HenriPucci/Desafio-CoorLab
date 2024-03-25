import http.server
import json
from urllib.parse import urlparse, parse_qs

# Carregar dados do arquivo JSON
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extrair cidades dos dados
destinys = [destiny['city'] for destiny in data['transport']]

# Classe para o manipulador de requisições HTTP
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    # Método para tratar requisições GET
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query = parse_qs(parsed_path.query)
        
        if path == '/destinys':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')  
            self.end_headers()
            self.wfile.write(json.dumps({'destinys': destinys}).encode())
        elif path == '/trips':
            destiny = query.get('destiny', [''])[0]
            if not destiny:
                self.send_response(400)
                self.end_headers()
                self.wfile.write('destiny não especificado'.encode('utf-8'))
                return

            trips = [trip for trip in data['transport'] if trip['city'] == destiny]

            if not trips:
                self.send_response(404)
                self.end_headers()
                self.wfile.write('Nenhuma trip encontrada para o destiny especificado'.encode('utf-8'))
                return

            try:
                confortable_trip = min(trips, key=lambda x: float(x['price_confort'].replace('R$ ', '').replace(',', '.')))
                economic_trip = min(trips, key=lambda x: float(x['price_econ'].replace('R$ ', '').replace(',', '.')))
            except ValueError:
                self.send_response(500)
                self.end_headers()
                self.wfile.write('Erro ao processar os dados das trips'.encode('utf-8'))
                return

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*') 
            self.end_headers()
            self.wfile.write(json.dumps({
                'confortable_trip': confortable_trip,
                'economic_trip': economic_trip
            }).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write('Endpoint nao encontrado'.encode('utf-8'))

# Criar servidor na porta 3000
with http.server.HTTPServer(('localhost', 3000), SimpleHTTPRequestHandler) as server:
    print('Servidor iniciado na porta 3000...')
    server.serve_forever()
