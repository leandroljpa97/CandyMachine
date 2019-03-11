# CandyMachine
Projeto por parte do núcleo Hackerchool.
Aplicação android que permite o confronto entre dois jogadores num Quiz (mesmas perguntas para os dois). As perguntas estão armazenadas numa base de dados SQL, e a REST API a correr num servidor. O vencedor do jogo, tem direito a receber doces. Um arduino faz rodar um servo de uma máquina para o lado que faz saír os doces pelo lado do jogador vencedor.

## Parte Mecânica: https://github.com/JoaoLuisGois
## REST API e arduino: Leandro Pereira
## Aplicação Android: https://github.com/vcandeias

# Instruções para o uso da máquina em Bancas:
0) ter doces e colocar na máquina (Malteasers ou assim)

1) Abrir a máquina e retirar o arduino. Fio amarelo do servo liga-se ao PIN D4

2) Ir ap código do arduino por baixo do que diz HOST DO MEU PCe fazer o seguinte:
HOTSPOT com o telemovel ou com o pc, pois nao dá para apanhar a net do IST diretamente por causa das medidas de segurança. E meter no ssid = "<identificador da internet hotspot>"; e em password" <password>";
  -> Carregam o programa para o arduino. O cabo esta dentro da máquina!!
  
 Se houver algum problema com os jogo em si, desligar a aplicação dos 2 telemoveis (ATENÇAO TÊM DE JOGAR 2 JOGADORES SENAO NAO DÁ), depois vir a este link (pelo computador ou telemovel, basta uma pessoa) http://hackerschool.io:8080/fresh e reiniciar as aplicações.
 
 3) A aplicação têm de pedir a algum membro da HS que tenha, e enviavos o apk e têm de a ter instalda no telemovel.
