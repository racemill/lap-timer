#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import beamUtils
import logging

homepagePath = "/usr/local/lap-timer/index.html"
hostName = "192.168.50.7"
serverPort = 80
logging.basicConfig(filename='/var/log/beam.log', format=' %(message)s %(asctime)s', datefmt='%I:%M:%S %p %m/%d/%Y', level=logging.DEBUG)

class BellServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.handleHomepageRequest()
            return

        self.send_response(404)
           
    def do_POST(self):   # This is where you land when pressing the "Simulate Beam Break" button on web page.
        if self.path == "/ring":
            logging.info("Sim Beam        ")
            self.handleRingBellRequest();

    def handleHomepageRequest(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        content = open(homepagePath, 'rb').read()
        self.wfile.write(content)

    def handleRingBellRequest(self):
        lapResult = beamUtils.lapTime()
        if lapResult == 429:       # Too soon after previous ring
           self.send_response(429)
        elif lapResult == 200:     # All good, worked.
           self.send_response(200)
        else:
           self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()

def run_server():
    webServer = HTTPServer((hostName, serverPort), BellServer)
    #print("Server started http://%s:%s" % (hostName, serverPort))
    logging.info('Server Started..')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

if __name__ == "__main__":        
    beamUtils.initialize()
    try:
        run_server()
    finally:
        beamUtils.cleanup()

