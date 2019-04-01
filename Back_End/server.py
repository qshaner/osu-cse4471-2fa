import SocketServer as socketserver
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SimpleHTTPServer
from flask import Flask


PORT = 8080
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

#class Handler():
    # with socketserver.TCPServer(("", PORT), Handler) as httpd:

httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.ikey = "DITMW1Y90LZLQLB0DGMF"
httpd.skey = "ZurpCXglNKm31Hwyht8PFyqpGKaVa2egoQDKqKJK"
httpd.akey = "abcdefghijkllmnopqrstuvwxyzabcdefghijkllmnopqrstuvwxyz"
httpd.host = "api-7ab09f67.duosecurity.com"

print("serving at port", PORT)
print("Httpd ",httpd.host)
httpd.serve_forever()

app = Flask(__name__)
app.route('/')