# Trabalho de Redes - Comunicação entre Containers Docker

Este projeto implementa três programas em Python que se comunicam via socket para trocar matrizes e calcular determinantes.

## Descrição dos programas

- **prog1**: Gera matrizes aleatórias e envia para o prog2.
- **prog2**: Recebe matrizes, calcula a inversa e o determinante, e envia o resultado para o prog3.
- **prog3**: Recebe os resultados e exibe o determinante e o tempo total desde a criação da matriz.

Cada programa roda em um container Docker distinto, podendo ser executados em máquinas diferentes.

## Pré-requisitos

- Docker instalado em todas as máquinas
- Rede que permita comunicação entre as máquinas (IPs e portas liberadas)
- Imagens Docker publicadas no Docker Hub com o usuário `mestrekan`.

## Como rodar

### 1. Rodar o prog3

```bash
docker run --rm -it -p 7000:7000 mestrekan/prog3-image
