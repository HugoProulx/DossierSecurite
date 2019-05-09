import socket
import threading
import os


def thread_recevoir(client_socket):
    while True:
        request = client_socket.recv(1024)
        print(request)

def thread_nv_client(server):
    i = 0
    while True:
        print("Le serveur attend une connexion")
        client,addr = server.accept()
        tabclient.append(client)
        thread_recevoir_client = threading.Thread(target=thread_recevoir, args={client,})
        thread_recevoir_client.start()
        i = (i + 1)

i = 0
client = []

bind_ip = "69.69.69.69"
bind_port = 4200

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

tableSocket = []
tabclient = []
thread_nv_client_start = threading.Thread(target=thread_nv_client, args={server,})
thread_nv_client_start.start()

while True:
    print("On attend la commande.")
    texte = str.encode(input())
    if tabclient.count == 0:
        print("Tableau vide!")
    for c in tabclient:
        c.send(texte)
