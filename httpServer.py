from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from fake_weather_data import list_cities, get_weather
from urllib.parse import urlparse, parse_qs

HOST = "127.0.0.1"
PORT = 5000

class WeatherRequestHandler(BaseHTTPRequestHandler):    
    def do_GET(self):       
        parsed_path = urlparse(self.path)
        print("Path received:",parsed_path.path)
        if parsed_path.path == "/":
            self.send_response(200)
            print("Serving homepage....")
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        elif parsed_path.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
                <html>
                             <head><tittle>weather API</tittle></head>
                             <body>
                                 <h1>Welcome to the Weather API</h1>
                                <p>Available endpoints:</p>
                                <ul>
                                    <li><a href="/weather/cities">/weather/cities</a></li>
                                    <li><a href="/get_weather?city=Paris">/get_weather?city=Paris</a></li>
                                    <li><a href="/get_weather?city=Berlin">/get_weather?city=Berlin</a></li>
                                    <li><a href="/get_weather?city=Madrid">/get_weather?city=Madrid</a></li>
                                    <li><a href="/get_weather?city=Rome">/get_weather?city=Rome</a></li>
                                    <li><a href="/get_weather?city=Lisbon">/get_weather?city=Lisbon</a></li>
                                    <li><a href="/get_weather?city=Vienna">/get_weather?city=Vienna</a></li>
                             </body>
                </html>
            """)
            
        elif parsed_path.path == "/weather/cities":
            cities = list_cities()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"cities": cities}).encode())
        elif parsed_path.path == "/get_weather":
            query = parse_qs(parsed_path.query)
            city = query.get("city", [None])[0]
            weather = get_weather(city)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"weather": weather}, ensure_ascii=False).encode())
       
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    print(f"Starting server at http://{HOST}:{PORT}")
    server = HTTPServer((HOST, PORT), WeatherRequestHandler)
    server.serve_forever()