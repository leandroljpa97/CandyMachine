# CandyMachine
Projeto por parte do núcleo Hackerchool.
2 participantes ligam-se através de uma aplicação android onde colocam os seus dados (que ficam armazenados numa base de dados), e jogam um contra o outro um quiz (em que as perguntas estão armazenadas numa base de dados e são aleatórias). O vencedor recebe doces. Mas como? A máquina tem duas saídas possíveis para os doces. Uma para o lado de cada jogador. Se ganhar o jogador1 , os doces saem pelo lado do jogador 1. Se ganhar o jogador 2, os doces saem pelo lado do jogador 2. Para isso a máquina tem um arduino com módulo wi-fi e um servo. O arduino comunica com uma REST API (realizada em Flask e online num servidor), que diz se ganhou o jogador 1 ou 2. O arduino indica ao servo para que lado rodar, para os doces sairem.
A aplicação comunica também com a REST API

Entidades: Sensores/Arduino, REST API (e base de dados), Aplicação Android.




## Parte Mecânica: [João Góis](https://github.com/JoaoLuisGois)
## REST API e arduino: [Leandro Pereira](https://github.com/leandroljpa97)
## Aplicação Android: [Vasco Candeias](https://github.com/vcandeias)
