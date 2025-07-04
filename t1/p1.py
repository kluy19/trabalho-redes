import socket
import pickle
import struct
import numpy as np
import time

def cria_matriz(ordem):
    return np.random.randint(0, 10, (ordem, ordem))

def enviar_dados(sock, dados):
    pacote = pickle.dumps(dados)
    tamanho = struct.pack('!Q', len(pacote))
    sock.sendall(tamanho)
    sock.sendall(pacote)

def main():
    print("=== Prog1: Gerador e Envio de Matrizes ===")
    host_p2 = input("Digite o IP do programa 2 (destino): ").strip()
    port_p2 = 6000

    ordem = int(input("Digite a ordem da matriz: "))
    num_matrizes = int(input("Digite o número de matrizes a enviar: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host_p2, port_p2))

        for i in range(num_matrizes):
            matriz = cria_matriz(ordem)
            print(f"\nMatriz #{i+1} gerada:")
            print(matriz)  # Mostra a matriz gerada no terminal
            
            start_time = time.time()  # Tempo local da geração da matriz

            dados = {
                'indice': i + 1,
                'matriz': matriz,
                'start_time': start_time  # Passa o timestamp para medir o tempo total depois
            }
            enviar_dados(s, dados)
            print(f"Matriz #{i+1} enviada para o programa 2.")

    print("Envio finalizado.")

if __name__ == "__main__":
    main()

