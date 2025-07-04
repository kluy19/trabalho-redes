import socket
import pickle
import struct
import numpy as np
import time

def processar_matriz(matriz):
    matriz_transposta = np.transpose(matriz)
    determinante = np.linalg.det(matriz)
    return matriz_transposta, determinante

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

def enviar_dados(sock, dados):
    pacote = pickle.dumps(dados)
    tamanho = struct.pack('!Q', len(pacote))
    sock.sendall(tamanho)
    sock.sendall(pacote)

def main():
    print("=== Prog2: Recebe matriz, processa e envia resultado ===")
    host_p3 = input("Digite o IP do programa 3 (destino): ").strip()
    port_p3 = 7000
    port_p2 = 6000

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_p3:
                s_p3.connect((host_p3, port_p3))
                print(f"Conectado ao programa 3 em {host_p3}:{port_p3}")

                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_p2:
                    s_p2.bind(('', port_p2))
                    s_p2.listen(1)
                    print("Prog2: aguardando matrizes de prog1...")

                    conn, addr = s_p2.accept()
                    with conn:
                        print(f"Prog2: conexão recebida de {addr}")
                        while True:
                            dados = receber_dados(conn)
                            if dados is None:
                                break

                            indice = dados['indice']
                            matriz = dados['matriz']
                            start_time = dados['start_time']

                            print(f"\nMatriz #{indice} recebida. Processando...")

                            transposta, determinante = processar_matriz(matriz)

                            resultado = {
                                'indice': indice,
                                'determinante': determinante,
                                'start_time': start_time  # repassa para p3 calcular tempo total
                            }

                            enviar_dados(s_p3, resultado)
                            print(f"Resultado da matriz #{indice} enviado para prog3.")

        except Exception as e:
            print(f"Erro em prog2: {e}")
            print("Reiniciando o loop de conexão...")
            time.sleep(2)

if __name__ == "__main__":
    main()

