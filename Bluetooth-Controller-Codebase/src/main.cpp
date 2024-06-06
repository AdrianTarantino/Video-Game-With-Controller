#include <Arduino.h>

int number;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while(!Serial.available());
  number = Serial.readString().toInt();
  Serial.print(number + 1);
}