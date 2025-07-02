# Trabalho de Redes - Comunicação entre Containers Docker

Este projeto implementa três programas em Python que se comunicam via sockets para troca de matrizes e cálculo de determinantes. Cada programa roda em um container Docker separado e pode ser executado em máquinas diferentes.

---

## Descrição dos Programas

- **prog1**: Gera matrizes aleatórias e envia para o prog2.
- **prog2**: Recebe matrizes do prog1, calcula a inversa e o determinante, e envia o resultado para o prog3.
- **prog3**: Recebe os resultados do prog2 e exibe o determinante e o tempo total desde a criação da matriz.

---

## Pré-requisitos

- Docker instalado em todas as máquinas que irão rodar os containers.
- Rede configurada para permitir comunicação entre as máquinas (IPs e portas liberadas).
- Imagens Docker disponíveis no Docker Hub sob o usuário `mestrekan`.

---

## Configuração de Rede

- **prog1** envia matrizes para **prog2** na porta **5000**.
- **prog2** envia resultados para **prog3** na porta **6000**.
- **prog3** escuta resultados na porta **7000**.

Cada programa precisa saber o IP da máquina onde o próximo programa está rodando para estabelecer a conexão.

---

## Como Executar

### 1. Rodar o prog3 (recebe resultados)

```bash
docker run --rm -it -p 7000:7000 mestrekan/prog3-image
