import json
import socket

import Main


def avvia_server():
    HOST = "127.0.0.1"
    PORT = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f"Server BWT in ascolto su {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connessione stabilita con il client: {addr}")

        with conn:
            data = conn.recv(1024)
            if not data:
                break

            testo_utente = data.decode("utf-8")
            stringa_speciale = testo_utente + "$"

            risultato_bwt, indice = Main.bwt(stringa_speciale)
            stringa_ricostruita = Main.ibwt(risultato_bwt, indice)

            risposta = {
                "originale": stringa_speciale,
                "bwt": risultato_bwt,
                "indice": indice,
                "decodificata": stringa_ricostruita,
            }

            conn.sendall(json.dumps(risposta).encode("utf-8"))

        print("Elaborazione completata, in attesa di nuove richieste...\n")


if __name__ == "__main__":
    avvia_server()
