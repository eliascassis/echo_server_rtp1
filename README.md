# Echo App

Este repositório foi criado para desenvolvimento do trabalho da disciplina de Redes de Computadores. Nele é proposto uma implementação de uma Aplicação de Eco, contendo o lado servidor e o lado cliente; apresentando juntamente uma documentação para a aplicação proposta. 

## Desenvolvimento

O trabalho foi desenvolvido com a linguagem **Python** em sua versão **3.8.10**. Tal linguagem foi escolhida devido a sua versatilidade, o que contribui não somente para o desenvolvimento de aplicações em diversos domínios como também auxilia no aprendizado da própria linguagem, permitindo aplicá-la em um cenário distinto do habitual sem maiores problemas. Além disso, a linguagem Python possui vasta documentação e tem sido muito utilizada.

Um dos requisitos do trabaho prático proposto define que a aplicação deve ser *multithreaded*, i. e., deve suportar que vários clientes se conectem ao servidor e consigam enviar mensagens de forma simultânea. Para isso, utilizou-se neste trabalho duas bibliotecas: uma para identificar os processos cliente e o processo servidor (*socket*) e outra para permitir várias conexões (*_thread*). Em relação ao número de *threads* suportado pela aplicação, foi definido que, se o número de conexões ultrapassar um número **X** definido pelo usuário, o servidor não aceitará mais conexões. Tal decisão contribui de forma significativa para a análise de complexidade do programa.

**OBS**: a biblioteca *socket* do python tem por padrão o uso do protocolo TCP para transporte, o que facilita e muito a definição e desenvolvimento do protocolo para a aplicação de eco implementada neste trabalho.

### Funcionamento

A Aplicação de Eco contém duas entidades necessárias a seu funcionamento: uma entidade **cliente** e uma entidade **servidor**. O **protocolo** que define as regras de comunicação é **assimétrico** - somente a entidade cliente dá parte no envio de mensagens, enquanto a entidade servidor apenas responde às requisições feitas. Ainda, é preciso ressaltar que o protocolo é **orientado à conexão**, havendo uma troca inicial de mensagens para **estabelecimento da conexão**. O DET (Diagrama de Estados e Transições) abaixo apresenta o funcionamento do protocolo implementado, onde as entidades cliente (*Echo Client*) e servidor (*Echo Server*) podem ser vistas como **entidades de protocolo**.

![det_echo_protocol](images/det/echo_DET.jpg)

*Figura 1: entidades de protocolo cliente e servidor para aplicação de eco*

A **entidade de protocolo cliente** (*Echo Client*) possui os seguintes elementos:

Estados:

- Idle: é o estado inicial da aplicação. Após ser inicializado, o lado cliente aguarda que o usuário entre com uma informação a ser enviada.

- Wait: é o estado de espera. Após enviar uma requisição, o lado cliente aguarda a resposta do servidor. 

Eventos:

- connection request: ao ser inicializado, o lado cliente envia uma requisição de conexão ao lado servidor.

- connection response: resposta do servidor à conexão. O servidor aceita a conexão ou recusa a conexão quando o número de clientes conectados for maior que **X**. 

- message: representa o envio da mensagem ao servidor.

- response: representa o recebimento da resposta do servidor. 

- TO: *timeout*. Na ocorrência de falta de resposta a aplicação cliente é encerrada.

Ações: 

- A1: função de leitura é ativada na aplicação. O lado cliente fica aguardando que o usuário entre com uma mensagem a ser enviada. 

- A2: encerra o lado cliente. 

- A3: imprime na tela a resposta do servidor.

Condições:

- C1: executa (A1) se a conexão for aceita e (A2) caso contrário.

A **entidade de protocolo servidor** (*Echo Server*) possui os seguintes elementos:

Estados:

- Idle: é o estado inicial da aplicação. Após ser inicializado, o lado cliente aguarda que o usuário entre com uma informação a ser enviada.

Eventos:

- connection request delivery: representa a entrega da requisição de conexão no servidor.

- message delivery: representa a entrega da mensagem no servidor.

Ações: 

- A3: servidor aceita a conexão.

- A4: servidor recusa a conexão pelo limite **X** de clientes ter sido atingido. 

- A5: recebe a mensagem do cliente.

- A6: responde a mensagem do cliente. 

**OBS**: o DET apresentado contém uma versão simplificada da captura do funcionamento do protocolo. O recurso foi utilizado para apresentar a visão geral do funcionamento da aplicação e para facilitar a preparação dos testes e o levantamento de novos requisitos. 

O cenário abaixo representa o fluxo normal de execução do protocolo.

    **<ELABORAR CENÁRIO>**

**OBS: AINDA FALTA DESCREVER OS CASOS DE TESTE**

### Módulos











