#include <Adafruit_CircuitPlayground.h>

void setup() {
  CircuitPlayground.begin();
}

void loop() {
  CircuitPlayground.redLED(HIGH);
  delay(10);
  CircuitPlayground.redLED(LOW);
  delay(10);
}
