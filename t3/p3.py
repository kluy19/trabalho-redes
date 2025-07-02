import socket
import socket
import pickle
import time

def main():
    print("=== Prog3: Recebe resultados e mostra na tela ===")

    host_p2 = input("Digite o IP do programa 2 (origem dos resultados): ").strip()
    port_p2 = 7000

    # Cria socket para ouvir prog2
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_p2:
        s_p2.bind(('', port_p2))
        s_p2.listen()

        print(f"Prog3: aguardando resultados do prog2 na porta {port_p2}...")

        while True:
            conn, addr = s_p2.accept()
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
                determinante = dados['determinante']
                timestamp_envio = dados['timestamp_envio']
                timestamp_proc = dados['timestamp_proc']
                timestamp_receb = time.time()

                tempo_total = timestamp_receb - timestamp_envio

                print(f"\nResultado da matriz #{indice}:")
                print(f"Determinante: {determinante}")
                print(f"Tempo total desde criação até recebimento: {tempo_total:.4f} segundos\n")

if __name__ == "__main__":
    main()

