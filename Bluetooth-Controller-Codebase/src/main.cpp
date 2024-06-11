// #include <Arduino.h>

// String data = "";

// int const JOYSTICK_AXIS_X = A0;
// int const JOYSTICK_AXIS_Y = A1;

// void setup() {
//   Serial.begin(9600);
//   Serial.setTimeout(1);
// }

// void loop() {
//   while(!Serial.available());

//   int joyStickXAxisValue = analogRead(JOYSTICK_AXIS_X);
//   int joyStickYAxisValue = analogRead(JOYSTICK_AXIS_Y);

//   Serial.println("Value");
//   Serial.print(joyStickXAxisValue);
//   Serial.print(",");
//   Serial.println(joyStickYAxisValue);
//   delay(500);
// }

#include <Arduino.h>

int xAxis = A0;
int yAxis = A1;
int range = 12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int xReading = analogRead(xAxis);
  xReading = map(xReading, 0, 1023, 0, range);

  int yReading = analogRead(yAxis);
  yReading = map(yReading, 0 , 1023, 0, range);

  Serial.print(xReading);
  Serial.print(",");
  Serial.println(yReading);
}


