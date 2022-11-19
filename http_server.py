from http.server import HTTPServer, BaseHTTPRequestHandler
import json


info_dict = {
  "id" : 1,
  "name" : "돼지",
  "별명" : "개돼지"
}

class MyHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response_only(200, 'OK')
    self.send_header('Content-Type', 'text/plain')
    self.end_headers()
    self.wfile.write(b"Hello World")
    with open("./info_dict.json", "w", encoding="UTF-8") as file:
      json.dump(info_dict, file, indent=2, ensure_ascii=False)
    
    read = open('icecream.js','r')
    print(read.read())

    
if __name__ == '__main__':
  server = HTTPServer(('', 8888), MyHandler)
  print("Started WebServer on port 8888....")
  print("Press ^C to quit WebServer.")
  server.serve_forever()




