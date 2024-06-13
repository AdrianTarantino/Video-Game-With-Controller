#include <Arduino.h>

int joystickXPin = A0;
int joystickYPin = A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int joystickXValue = analogRead(joystickXPin);
  int joystickYValue = analogRead(joystickYPin);  

  String joystickData = String(joystickXValue) + "," + String(joystickYValue);
  Serial.println(joystickData);
  delay(10);
}