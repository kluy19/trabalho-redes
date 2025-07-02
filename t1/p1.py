import socket
import numpy as np
import pickle
import time

def cria_matriz(ordem):
    return np.random.randint(0, 10, (ordem, ordem))

def main():
    print("=== Prog1: Gerador e Envio de Matrizes ===")
    
    host_p2 = input("Digite o IP do programa 2 (destino): ").strip()
    port_p2 = 6000
    
    ordem = int(input("Digite a ordem da matriz: "))
    num_matrizes = int(input("Digite o número de matrizes a enviar: "))
    
    for i in range(num_matrizes):
        matriz = cria_matriz(ordem)
        print(f"\nMatriz #{i+1} gerada:\n{matriz}")
        
        dados = {
            'indice': i+1,
            'matriz': matriz,
            'timestamp': time.time()
        }
        
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host_p2, port_p2))
                dados_serializados = pickle.dumps(dados)
                s.sendall(dados_serializados)
                print(f"Matriz #{i+1} enviada para {host_p2}:{port_p2}")
        except Exception as e:
            print(f"Erro ao enviar matriz #{i+1}: {e}")
        
        time.sleep(1)  # só para espaçar o envio

if __name__ == "__main__":
    main()

