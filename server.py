import socket
import hashlib

HOST = "127.0.0.1"
PORT = 12346

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serveur UDP sur {HOST}:{PORT}")

    while True:
        data, addr = s.recvfrom(2048)

        try:
            # Séparer message et hash
            message, hash_hex = data.split(b"\x00", 1)

            # Recalculer hash
            calc = hashlib.sha256(message).hexdigest().encode("ascii")

            if calc == hash_hex:
                print("Message valide reçu")
                s.sendto(b"Message et hachage valides", addr)
            else:
                print("Hash invalide")
                s.sendto(b"Erreur de hachage", addr)

        except Exception:
            s.sendto(b"Format invalide", addr)
