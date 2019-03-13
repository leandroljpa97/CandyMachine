# CandyMachine
Projeto por parte do núcleo Hackerchool.
Aplicação android que permite o confronto entre dois jogadores num Quiz (mesmas perguntas para os dois). As perguntas estão armazenadas numa base de dados SQL, e a REST API a correr no servidor da HS. O vencedor do jogo, tem direito a receber doces. Um arduino faz rodar o servo da máquina para o lado que faz saír os doces pelo lado do jogador vencedor.

## Parte Mecânica: [João Góis](https://github.com/JoaoLuisGois)
## REST API e arduino: [Leandro Pereira](https://github.com/leandroljpa97)
## Aplicação Android: [Vasco Candeias](https://github.com/vcandeias)

# Instruções para o uso da máquina em Bancas:

Comprar m%ms ou Malteasers se não houver e não os gastem logo todos PFF!

1) Ter doces e colocar na máquina (Recomedado usar m&ms ou maltesers).

2) Abrir a máquina e retirar o arduino. Fio amarelo do servo liga-se ao PIN D4.

3) O mcu é alimentado por uma pilha de 9v, ligar fio terra da pilha a um pino ground do mcu e ligar o fio de fase ao pino vin (Atenção: ligar o fio de fase a qualquer outro pino poderá danificar o arduino)

4) (Opcional) Testar se o sistema está operacional, para isso carregar o código "servo.ino" para o mcu. O programa "servo.ino" é também útil caso seja necessário ajustar os valores dos ângulos do servo, desta forma é possível controlar a quantidade de doces.

5) Ir ao código do arduino (server.io) por baixo do que diz HOST DO MEU PC e fazer o seguinte:
HOTSPOT com o telemóvel ou com o pc, pois nao dá para apanhar a net do IST diretamente por causa das medidas de segurança. E meter no ssid = "*identificador da internet hotspot*"; e em password = "*password*";
  -> Carregam o programa para o arduino. O cabo está dentro da máquina!! ATENÇÃO: É UM NODE MCU, POR ISSO NAS CONFIGURAÇÕES DO arduinoIDE SELECIONAR O NODE MCU E INSTALAR O QUE É NECESSÁRIO. CASO NAO TENHAM:
  Como instalar a placa NodeMCU: http://www.instructables.com/id/Quick-Start-to-Nodemcu-ESP8266-on-Arduino-IDE

6) Antes de começar a jogar é necessário centrar a peça preta móvel (a que tem os dentes), para isto, basta afastar o servo ligeiramente para trás e central a peça preta. Nota: O servo tem que estar a 90º, para isso basta correr liga-lo ao mcu (o programa no mcu automaticamente mete o servo a 90º).

7) Instalar a aplicação. A aplicação apenas pode ser instalada em telemovéis android. Descarregar o APK deste link: https://drive.tecnico.ulisboa.pt/download/570023764607247. Nota: são necessários dois telemovéis com a aplicação instalada para jogar. A aplicação deve ser apenas usada quando se prentende jogar. 
  
8) Se houver algum problema com o jogo em si, desligar a aplicação nos dois telemóveis, depois ir a este link (pelo computador ou telemóvel, basta uma pessoa) http://hackerschool.io:8080/fresh e reiniciar as aplicações.
 
