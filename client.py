import json
import socket


def avvia_client():
    HOST = "127.0.0.1"
    PORT = 65432

    print("CLIENT")
    testo = input("Inserisci una frase da inviare al server: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        client_socket.sendall(testo.encode("utf-8"))

        data = client_socket.recv(4096)

        risposta = json.loads(data.decode("utf-8"))

    print("RISULTATI")
    print(f"Stringa con marcatore:         {risposta['originale']}")
    print(f"Messaggio codificato (BWT):    {risposta['bwt']}")
    print(f"Indice riga:                   {risposta['indice']}")
    print(f"Messaggio decodificato (IBWT): {risposta['decodificata']}")


if __name__ == "__main__":
    avvia_client()
