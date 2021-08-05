int reed_PIN = 11;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(reed_PIN, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(reed_PIN) == HIGH)
    Serial.println("open");
}
