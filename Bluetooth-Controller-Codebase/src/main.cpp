#include <Arduino.h>

String data = "";

int const UP_BTN = 2;
int const DOWN_BTN = 4;
int const LEFT_BTN = 5;
int const RIGHT_BTN = 3;
int const E_BTN = 6;
int const F_BTN = 7;
int const JOYSTICK_BTN = 8;
int const JOYSTICK_AXIS_X = A0;
int const JOYSTICK_AXIS_Y = A1;
int buttons[] = {UP_BTN, DOWN_BTN, LEFT_BTN, RIGHT_BTN, E_BTN, F_BTN, JOYSTICK_BTN, JOYSTICK_AXIS_X, JOYSTICK_AXIS_Y};
int buttonsResults[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};

void setup() {
  for(int buttonIndex = 0; buttonIndex < 9; buttonIndex++) {
    pinMode(buttons[buttonIndex], INPUT);
  }

  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  while(!Serial.available());

  for(int buttonIndex = 0; buttonIndex < 7; buttonIndex++) {
    buttonsResults[buttonIndex] = digitalRead(buttons[buttonIndex]);
  }

  buttonsResults[7] = analogRead(buttons[7]);
  buttonsResults[8] = analogRead(buttons[8]);

  for(int buttonResultIndex = 0; buttonResultIndex < 9; buttonResultIndex++) {
    Serial.print(buttonsResults[buttonResultIndex]);
  }
  Serial.println("");
  delay(500);
}



