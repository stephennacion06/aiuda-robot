volatile unsigned long lastturn, time_press;
volatile float SPEED;
volatile float DIST;
float w_length = 2.050;
boolean flag;

void setup() {
  Serial.begin(9600);                // configure serial for debug
  attachInterrupt(1, sens, RISING);  // hall sensor interrupt

}

void sens() {
  if (millis() - lastturn > 80) {    // simple noise cut filter (based on fact that you will not be ride your bike more than 120 km/h =)
    SPEED = w_length / ((float)(millis() - lastturn) / 1000) * 3.6;   // calculate speed
    SPEED = SPEED/1.609;

    lastturn = millis();                                              // remember time of last revolution                                // calculate distance
  }
}

void loop() {
 Serial.println(SPEED);
 
  if ((millis() - lastturn) > 2000) {       // if there is no signal more than 2 seconds
    SPEED = 0;                              // so, speed is 0
  }
}
