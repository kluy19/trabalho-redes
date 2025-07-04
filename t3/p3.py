import socket
import pickle
import struct
import time

def receber_dados(sock):
    tamanho_pacote = sock.recv(8)
    if not tamanho_pacote:
        return None
    tamanho = struct.unpack('!Q', tamanho_pacote)[0]

    pacote = b''
    while len(pacote) < tamanho:
        parte = sock.recv(min(4096, tamanho - len(pacote)))
        if not parte:
            raise ConnectionError("Conexão interrompida.")
        pacote += parte

    return pickle.loads(pacote)

def main():
    port_p3 = 7000
    print("=== Prog3: Recebe resultados do Prog2 e exibe ===")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port_p3))
        s.listen(1)
        print(f"Prog3 aguardando resultados na porta {port_p3}...")

        conn, addr = s.accept()
        with conn:
            print(f"Conectado por {addr}")
            while True:
                try:
                    resultado = receber_dados(conn)
                    if resultado is None:
                        break

                    indice = resultado['indice']
                    determinante = resultado['determinante']
                    start_time = resultado['start_time']

                    tempo_total = time.time() - start_time

                    print(f"\nMatriz #{indice}:")
                    print(f"Determinante: {determinante:.2f}")
                    print(f"Tempo total (geração até exibição): {tempo_total:.4f} segundos")

                except Exception as e:
                    print(f"Erro ao receber dados: {e}")
                    break

if __name__ == "__main__":
    main()

