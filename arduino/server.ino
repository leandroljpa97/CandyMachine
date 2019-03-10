#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Servo.h>  // Include the Servo library
int servoPin = 2;  // Declare the Servo pin
Servo Servo1;  // Create a servo object

/*
//MINHA CASA
const char* ssid = "ZON-8E40";
const char* password = "759769fada90";  */

//HOTSPOT DO MEU PC
const char* ssid = "DESKTOP-AN1JALD 0704";
const char* password = "03Y,7n80";

WiFiServer server(80);

void setup() {
  Serial.begin(9600);
  // Connect to WiFi network
  Serial.print("Conetando a: ");
  Serial.println(ssid);

  // Inicia a ligação ao wifi
  WiFi.begin(ssid, password);

  // Testa a ligação
  while (WiFi.status() != WL_CONNECTED) {
    delay(50);
    Serial.print(".");
  }
  Servo1.attach(servoPin);
  Servo1.write(90); // Posição inicial servo
  shake();


}


void loop() {
 // Servo1.write(90);
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    HTTPClient http;  //Declare an object of class HTTPClient

    http.begin("http://hackerschool.io:8080/start");  //Specify request destination
    int httpCode = http.GET(); //Send the request
    if (httpCode > 0) { //Check the returning code

      String payload = http.getString();   //Get the request response payload

      //se ganhar o jogador 1 roda para um lado
       if(payload.toInt()==1){
        Servo1.write(0); // Make servo go to 0 degrees
        delay(1000);
        Servo1.write(90);
        shake();
      }
      //se ganhar o jogador 2 roda para o lado contrario
      else if(payload.toInt()==2){
        Servo1.write(180);
        delay(2000);
        Servo1.write(90);
        shake();
      }
    }
    http.end();   //Close connection
  }
  delay(1000);
}
// Função para evitar que os doces fiquem presos.
void shake() {
  for (i=0; i <= 5; i++){
    Servo1.write(80);
    delay(100);
    Servo1.write(100);
    delay(100);
    Servo1.write(90);
    delay(100);
  }
