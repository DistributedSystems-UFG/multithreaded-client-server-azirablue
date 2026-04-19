[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yQPZ0SBC)

# ClientServerBasics - Multithread

Extensão do sistema cliente-servidor com suporte a multithreading no cliente e no servidor, geração automática de requisições e experimentos de desempenho comparativo.

---

## Arquitetura

A comunicação ocorre via protocolo TCP. A aplicação é composta pelos seguintes arquivos:

- **`server.py`**: servidor single-thread, aceita múltiplas conexões sequencialmente, processando uma requisição por vez.
- **`server_multithread.py`**: servidor multithread, cuja thread principal aceita a conexão e recebe a requisição, disparando uma nova thread apenas para executá-la e responder ao cliente.
- **`client_singlethread_auto.py`**: cliente single-thread com geração automática de requisições, abre uma conexão por requisição de forma sequencial.
- **`client_multithread.py`**: cliente multithread, dispara uma nova thread por requisição, cada uma abrindo sua própria conexão TCP, enviando a requisição e aguardando a resposta.
- **`constCS.py`**: define o endereço IP e a porta de comunicação.

---

## Modelo de Comunicação

O cliente envia mensagens de texto contendo um comando seguido de um argumento. O servidor interpreta a primeira palavra como a operação a ser executada.

Formato geral da mensagem:

```
COMANDO texto
```

As mensagens são delimitadas por `\n` para garantir a correta separação no buffer TCP.

---

## Operações Disponíveis

- **UPPER**: converte o texto para letras maiúsculas
- **LOWER**: converte o texto para letras minúsculas
- **REVERSE**: inverte a ordem dos caracteres
- **COUNT**: retorna a quantidade de caracteres

Exemplos:

```
UPPER hello world
REVERSE abcde
COUNT banana
```

---

## Execução do Sistema

### Servidor single-thread

```bash
python3 server.py
```

### Servidor multithread

```bash
python3 server_multithread.py
```

### Cliente single-thread automatizado

```bash
python3 client_singlethread_auto.py
```

### Cliente multithread automatizado

```bash
python3 client_multithread.py
```

O número de requisições pode ser ajustado pela variável `TOTAL_REQUISICOES` nos arquivos de cliente automatizado.

---

## Medição de Desempenho

O sistema mede tempo em dois níveis:

- **Servidor**: tempo de processamento de cada requisição
- **Cliente**: tempo entre envio e recebimento de cada resposta, e tempo total do experimento
