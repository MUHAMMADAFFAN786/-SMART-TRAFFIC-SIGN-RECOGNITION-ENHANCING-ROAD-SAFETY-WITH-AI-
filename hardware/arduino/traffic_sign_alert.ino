// this is new code of arduino 
#define WHITE 8
#define GREEN 9
#define BUZZER 10

void setup() {
  pinMode(WHITE, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BUZZER, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    if (data == "STOP") {
      digitalWrite(WHITE, HIGH);
      digitalWrite(GREEN, LOW);
      digitalWrite(BUZZER, HIGH);
    }
    else if (data == "SPEED") {
      digitalWrite(WHITE, LOW);
      digitalWrite(GREEN, HIGH);
      digitalWrite(BUZZER, LOW);
    }
    else if (data == "CLEAR") {
      digitalWrite(WHITE, LOW);
      digitalWrite(GREEN, LOW);
      digitalWrite(BUZZER, LOW);
    }
  }
}
