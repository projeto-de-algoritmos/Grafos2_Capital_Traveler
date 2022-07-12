# Capital_Traveler

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
Dupla 18

|Matrícula | Aluno |
| -- | -- |
| 19/0111836 |  Luan Vasco Cavalcante |
| 18/0130889  |  Sávio Cunha de Carvalho |

## Sobre 
O objetivo do trabalho é mostrar como o **Dijkstra** funciona usando uma representação **fictícia** de um mapa do Brasil. O algoritmo de cheapest path do Dijkstra calcula o caminho mais curto entre os 2 nós do grafo escolhido.

A imagem abaixo representa rodovias **fictícias** entre **capitais** brasileiras. 
O objetivo é escolher um ponto de partida e um ponto de chegada e o caminho mais **curto** é escolhido com base na **distância** que serão os **pesos** das arestas.

A tabela de distâncias utilizadas foi encontrada no link : https://goodway.com.br/distancias.htm .

Foi levado em conta que esses são os únicos caminhos rodoviários. É uma representação **fictícia**.
Não foram adicionados os pesos das arestas para não poluir as imagens.

![alt text](https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler/blob/master/media/BrasilArestas.png)

![alt text](https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler/blob/master/media/BrasilSemAresta.jpeg)

## Screenshots
É printado um menu com escolha de uma cidade por número inteiro.
Primeiro uma cidade de partida e depois uma cidade de chegada.
![alt text](https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler/blob/master/media/menu.png)

Resultado do algoritmo de cheapest path com **Dijkstra**
![alt text](https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler/blob/master/media/funcionamento.png)

Outro exemplo : Brasília -> Fortaleza
![alt text](https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler/blob/master/media/bsbfortal.png)

## Instalação 
**Linguagem**: Python<br>
**Framework**: N/A<br>

Pré-requisitos :
Ter python3 instalada na máquina.

## Uso 

O código roda no próprio terminal e seu uso é bem simples. Você escolhe uma capital de uma lista enumerada como ponto de partida e escolhe outra como ponto de chegada.

**Todas as entradas são numeros inteiros e devem estar no intervalo proposto.**

Comece clonando o repositório com o comando :<br>
    git clone https://github.com/projeto-de-algoritmos/Grafos2_Capital_Traveler.git

Entre na pasta clonada :<br>
    cd Grafos2_Capital_Traveler

Execute o arquivo :<br>
    python3 main.py

## Outros

O Sistema Operacional utilizado foi Ubuntu 20.04.




