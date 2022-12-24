#include <PID_v1.h>
//HALL EFFECT SENSOR
volatile unsigned long lastturn, time_press;
volatile float SPEED;
volatile float DIST;
float w_length = 2.050;
boolean flag;
//HALL EFFECT SENSOR

//PARSING SPEED,ANGLE
String str;
//PARSING SPEED, ANGLE

//LINEAR ACTUATOR
#define extend_pin 8
#define retract_pin 7
//LINEAR ACTUATOR


//THROTTLE PID
double Setpoint_t, Input_t, Output_t;
double Kp_t=2, Ki_t=5, Kd_t=1;
PID myPID_t(&Input_t, &Output_t, &Setpoint_t, Kp_t, Ki_t, Kd_t, DIRECT);
#define throttle_pin 9
//THROTTLE PID
void setup() {
  Serial.begin(9600);                // configure serial for debug
  attachInterrupt(5, sens, RISING);  // hall sensor interrupt
  myPID_t.SetMode(AUTOMATIC);
  pinMode(extend_pin, OUTPUT);
  pinMode(retract_pin, OUTPUT);
  pinMode(throttle_pin, OUTPUT);
}

void sens() {
  if (millis() - lastturn > 80) {    // simple noise cut filter (based on fact that you will not be ride your bike more than 120 km/h =)
    SPEED = w_length / ((float)(millis() - lastturn) / 1000) * 3.6;   // calculate speed
    SPEED = SPEED / 1.609;

    lastturn = millis();                                              // remember time of last revolution                                // calculate distance
  }
}

void loop() {
  //PARSING SPEED, ANGLE
  if (Serial.available() > 0) {

 str = Serial.readStringUntil('\n');

  }
      
         
          int str_len = str.length() + 1;

          // Prepare the character array (the buffer)
          char char_array[str_len];

          // Copy it over
          str.toCharArray(char_array, str_len);

          char delimiters[] = "[!:,]";
          char* valPosition;
          char* valPosition2;

          valPosition = strtok(char_array, delimiters);
          Setpoint_t  = atoi(valPosition);
          //valPosition2 = strtok(NULL, delimiters);
          //setpoint_angle = atoi(valPosition2);

//PARSING SPEED, ANGLE
  Input_t = SPEED;
  linear_actuator_activate(Setpoint_t);
  myPID_t.Compute();
  //analogWrite(PIN_OUTPUT, Output);
 Serial.print("Feedback: ");
 Serial.print(Input_t);
 Serial.print("  Output: ");
 Serial.println(Output_t);
 analogWrite(throttle_pin,Output_t);
 
  if ((millis() - lastturn) > 2000) {       // if there is no signal more than 2 seconds
    SPEED = 0;                              // so, speed is 0
  }

}

void linear_actuator_activate(double(Setpoint_t))
{
  if (Setpoint_t == 0)
  {
    digitalWrite(retract_pin, LOW);
    digitalWrite(extend_pin, HIGH);
  }
  else
  {
    digitalWrite(retract_pin, HIGH);
    digitalWrite(extend_pin, LOW);
  }
}
