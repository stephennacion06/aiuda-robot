/*
  Switch statement with serial input

  Demonstrates the use of a switch statement. The switch statement allows you
  to choose from among a set of discrete values of a variable. It's like a
  series of if statements.

  To see this sketch in action, open the Serial monitor and send any character.
  The characters a, b, c, d, and e, will turn on LEDs. Any other character will
  turn the LEDs off.

  The circuit:
  - five LEDs attached to digital pins 2 through 6 through 220 ohm resistors

  created 1 Jul 2009
  by Tom Igoe

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/SwitchCase2
*/
int led = 2;
int brighthness = 45;
int relay_activate = 13;
void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  //pinMode(led,OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000); 
}

void loop() {
                      // wait for a second
  if (Serial.available() > 0) {
    int inByte = Serial.read();
    // do something different depending on the character received.
    // The switch statement expects single number values for each case; in this
    // example, though, you're using single quotes to tell the controller to get
    // the ASCII value for the character. For example 'a' = 97, 'b' = 98,
    // and so forth:

    switch (inByte) {
      case 'a':
        brighthness=45;
        break;
      case 'b':
        brighthness=brighthness+1;
        break;
      case 'c':
        brighthness=brighthness-1;
        break;
      case 'd':
        brighthness=175;
        break;
    }
  }
  if(brighthness > 200){
    brighthness = 200;
  }
  Serial.println(brighthness);
  analogWrite(led,brighthness);
}
