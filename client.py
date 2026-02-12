
from pathlib import Path

p = Path("data/message.txt")

s = p.read_text(encoding="utf-8")

print(type(s), len(s))
print(s)


b = p.read_bytes()

print(type(b), len(b))
print(b[:20])


b2 = s.encode("utf-8")
s2 = b.decode("utf-8")

print(len(b2), type(b2))
print(type(s2))







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
