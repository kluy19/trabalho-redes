import socket
import pickle
import numpy as np
import time

def main():
    print("=== Prog2: Recebe matriz, processa e envia resultado ===")

    host_p1 = input("Digite o IP do programa 1 (origem das matrizes): ").strip()
    port_p1 = 6000

    host_p3 = input("Digite o IP do programa 3 (destino do resultado): ").strip()
    port_p3 = 7000

    # Cria socket para ouvir prog1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_p1:
        s_p1.bind(('', port_p1))
        s_p1.listen()

        print(f"Prog2: aguardando matrizes do prog1 na porta {port_p1}...")

        while True:
            conn, addr = s_p1.accept()
            with conn:
                print(f"Conexão recebida de {addr}")
                dados_serializados = b''
                while True:
                    parte = conn.recv(4096)
                    if not parte:
                        break
                    dados_serializados += parte

                dados = pickle.loads(dados_serializados)
                indice = dados['indice']
                matriz = dados['matriz']
                timestamp_envio = dados['timestamp']

                print(f"Matriz #{indice} recebida de prog1:\n{matriz}")

                # Inverte a matriz (transposição)
                matriz_invertida = np.transpose(matriz)
                print(f"Matriz #{indice} invertida:\n{matriz_invertida}")

                # Calcula determinante
                det = np.linalg.det(matriz_invertida)
                print(f"Determinante da matriz #{indice}: {det}")

                # Prepara dados para enviar ao p3
                resultado = {
                    'indice': indice,
                    'determinante': det,
                    'timestamp_envio': timestamp_envio,
                    'timestamp_proc': time.time()
                }

                # Envia para p3
                try:
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_p3:
                        s_p3.connect((host_p3, port_p3))
                        dados_serializados = pickle.dumps(resultado)
                        s_p3.sendall(dados_serializados)
                        print(f"Resultado da matriz #{indice} enviado para prog3")
                except Exception as e:
                    print(f"Erro ao enviar resultado para prog3: {e}")

if __name__ == "__main__":
    main()

