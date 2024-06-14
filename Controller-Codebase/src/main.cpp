#include <Arduino.h>

int joystickXPin = A0;
int joystickYPin = A1;

int up_button     = 2; // Boton Amarillo - A
int down_button   = 4; // Boton Amarillo - C 
int left_button   = 5; // Boton Azul     - D 
int right_button  = 3; // Boton Azul     - B


void setup() {
  Serial.begin(9600);
}

void loop() {
  int joystickXValue = analogRead(joystickXPin);
  int joystickYValue = analogRead(joystickYPin);  

  int upButtonValue = digitalRead(up_button);
  int downButtonValue = digitalRead(down_button);
  int leftButtonValue = digitalRead(left_button);
  int rightButtonValue = digitalRead(right_button);

  String controllerData = String(joystickXValue) + ',' +
                          String(joystickYValue) + ',' +
                          String(upButtonValue) + ',' +
                          String(downButtonValue) + ',' +
                          String(leftButtonValue) + ',' +
                          String(rightButtonValue);
                          
  Serial.println(controllerData);
  delay(10);
}