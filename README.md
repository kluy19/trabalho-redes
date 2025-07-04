**Trabalho de Redes - Comunicação entre Containers Docker**

**Aluno: Kuyvert Ananias Nunes**
**Aluno: Rhuan Carvalho dos Santos**

Este projeto implementa três programas em Python que se comunicam via sockets para troca de matrizes e cálculo de determinantes. Cada programa roda em um container Docker separado e pode ser executado em máquinas diferentes.

---

Descrição dos Programas

- prog1: Gera matrizes aleatórias e envia para o prog2.
- prog2: Recebe matrizes do prog1, calcula a transposta e o determinante, e envia o resultado para o prog3.
- prog3: Recebe os resultados do prog2 e exibe o determinante e o tempo total desde a criação da matriz.

---

Pré-requisitos

- Docker instalado em todas as máquinas que irão rodar os containers.
- Rede configurada para permitir comunicação entre as máquinas (IPs e portas liberadas).
- Imagens Docker disponíveis no Docker Hub sob o usuário mestrekan (ou build local das imagens).

---

Configuração de Rede

- prog1 envia matrizes para prog2 na porta 6000.
- prog2 envia resultados para prog3 na porta 7000.
- prog3 escuta resultados na porta 7000.

Cada programa precisa saber o IP da máquina onde o próximo programa está rodando para estabelecer a conexão.

---

Como Executar

Passo 1: Baixar as imagens Docker do Docker Hub

Se você preferir usar as imagens já disponíveis no Docker Hub, basta executar:

docker pull mestrekan/prog1-image
docker pull mestrekan/prog2-image
docker pull mestrekan/prog3-image

---

Passo 2: Rodar os containers na ordem correta

1. Rodar o prog3 (escuta resultados do prog2):

docker run --rm -it -p 7000:7000 mestrekan/prog3-image

2. Rodar o prog2 (recebe matrizes do prog1, processa e envia para prog3):

docker run --rm -it -p 6000:6000 mestrekan/prog2-image

Na execução, será solicitado o IP da máquina onde o prog3 está rodando.

3. Rodar o prog1 (gera matrizes e envia para prog2):

docker run --rm -it -p 5000:5000 mestrekan/prog1-image

Na execução, será solicitado o IP da máquina onde o prog2 está rodando.

---

Observações Importantes

- As portas 6000 e 7000 precisam estar liberadas no firewall e roteadores para comunicação funcionar.
- Sempre rode os containers na ordem: prog3 → prog2 → prog1 para evitar erros de conexão.
- Use IPs corretos e acessíveis na rede onde os containers estão executando.
- A comunicação entre containers pode ser feita tanto em uma mesma máquina (usando localhost) quanto entre máquinas diferentes (usando IPs reais da rede).
- Se quiser automatizar, é possível criar um docker-compose.yml para orquestrar os três containers.

---

Contato

Qualquer dúvida ou sugestão, abra uma issue no repositório ou me contate diretamente.

