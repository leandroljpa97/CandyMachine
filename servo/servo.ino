#include <Servo.h>  // Include the Servo library

int servoPin = 2;  // Declare the Servo pin

Servo Servo1;  // Create a servo object
void setup() {
  Serial.begin(9600);

Servo1.attach(servoPin); 
}
void loop(){ 
  Servo1.write(90);
delay(800);
Servo1.write(15); // Make servo go to 0 degrees
delay(800);
Servo1.write(90);
delay(800);
Servo1.write(165); 
delay(800);

}
