# CandyMachine
Projeto por parte do núcleo Hackerchool

Procedimento para a APP:
1) fazes um post para o endpoint /index (TROQUEI O NOME ATENÇÃO) e eu envio-te um code-> 0, 1 ou 2. Se for 0, é pq nao dá para jogar. Se for 1 és o jogador 1, se for 2 es o 2.
2) Fazes um get ao endpoint /questions e eu mando-te as perguntas.
3) vais fazer de segundo a segundo um get no endpoint /wait, e vou-te retornar uma flag.  Se for 0 vai estar a aparecer " WAITING... " se for 1, começa a jogar!!
4) mandas os resultados para /results. Além disso, mandas o code (1 ou 2) para eu saber qual  e cada jogador.
mandas 'time''correct'],'total','id' (nr de aluno ) e o code ( 1 ou 2).
