#define delay_time  100
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(A0, OUTPUT);

  digitalWrite(2, HIGH);
  digitalWrite(3, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, HIGH);
  digitalWrite(8, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(12, HIGH);
  digitalWrite(13, HIGH);
  digitalWrite(A0, HIGH);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(2, LOW);
  delay(delay_time);
  digitalWrite(2, HIGH);
  delay(delay_time);

  digitalWrite(3, LOW);
  delay(delay_time);
  digitalWrite(3, HIGH);
  delay(delay_time);

  digitalWrite(4, LOW);
  delay(delay_time);
  digitalWrite(4, HIGH);
  delay(delay_time);

  digitalWrite(5, LOW);
  delay(delay_time);
  digitalWrite(5, HIGH);
  delay(delay_time);

  digitalWrite(6, LOW);
  delay(delay_time);
  digitalWrite(6, HIGH);
  delay(delay_time);

  digitalWrite(7, LOW);
  delay(delay_time);
  digitalWrite(7, HIGH);
  delay(delay_time);

  digitalWrite(8, LOW);
  delay(delay_time);
  digitalWrite(8, HIGH);
  delay(delay_time);

  digitalWrite(9, LOW);
  delay(delay_time);
  digitalWrite(9, HIGH);
  delay(delay_time);

  digitalWrite(10, LOW);
  delay(delay_time);
  digitalWrite(10, HIGH);
  delay(delay_time);

  digitalWrite(11, LOW);
  delay(delay_time);
  digitalWrite(11, HIGH);
  delay(delay_time);

  digitalWrite(12, LOW);
  delay(delay_time);
  digitalWrite(12, HIGH);
  delay(delay_time);

    digitalWrite(13, LOW);
  delay(delay_time);
  digitalWrite(13, HIGH);
  delay(delay_time);

  
    digitalWrite(A0, LOW);
  delay(delay_time);
  digitalWrite(A0, HIGH);
  delay(delay_time);

}
