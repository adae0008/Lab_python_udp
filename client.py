import socket
import hashlib
from pathlib import Path

HOST = "127.0.0.1"
PORT = 12346

#Ici c'est pour lire message
msg = Path("data/message.txt").read_text(encoding="utf-8").encode("utf-8")

h = hashlib.sha256(msg).hexdigest()

# Créer payload : message + séparateur + hash
payload = msg + b"\x00" + h.encode("ascii")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(payload, (HOST, PORT))

    data, _ = s.recvfrom(1024)
    print("Réponse serveur :", data.decode("utf-8"))
