#include <Servo.h>

// Define servos for the fingers
Servo thumbServo;
Servo indexServo;
Servo middleServo;
Servo ringServo;
Servo pinkyServo;

// Servo pin connections
const int thumbServoPin = 9;
const int indexServoPin = 10;
const int middleServoPin = 11;
const int ringServoPin = 12;
const int pinkyServoPin = 13;

void setup() {
  // Start the serial communication
  Serial.begin(9600);

  // Attach the servos to their respective pins
  thumbServo.attach(thumbServoPin);
  indexServo.attach(indexServoPin);
  middleServo.attach(middleServoPin);
  ringServo.attach(ringServoPin);
  pinkyServo.attach(pinkyServoPin);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming byte:
    String data = Serial.readStringUntil('\n');

    // Split the data into servo positions
    int positions[5];
    int lastIndex = 0, nextIndex = 0, i = 0;

    while (nextIndex != -1 && i < 5) {
      nextIndex = data.indexOf(',', lastIndex);
      positions[i++] = data.substring(lastIndex, nextIndex).toInt();
      lastIndex = nextIndex + 1;
    }

    // Move servos to the received positions
    thumbServo.write(positions[0]);
    indexServo.write(positions[1]);
    middleServo.write(positions[2]);
    ringServo.write(positions[3]);
    pinkyServo.write(positions[4]);
  }
}
