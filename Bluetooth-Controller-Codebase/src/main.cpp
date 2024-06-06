#include <Arduino.h>

String data = "";

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while(!Serial.available());
  data = Serial.readString();
  Serial.print(data);
}