import os 
import ssl
import socket

hostname = 'cable.99ner.br'
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('/etc/ssl/certs/99ner.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock: 
    with context.wrap_socket(sock, server_hostname=hostname) as ssock: 
        print(ssock.version())