//----------------------------------PID STEERING-----------------------------
#include <PID_v1.h>
//DC MOTOR
int EN = 6;
int R_PWM = 4;
int L_PWM = 5;

//DC MOTOR


// MPU PARAMETERS
#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;

// Timers
unsigned long timer = 0;
float timeStep = 0.01;

// Pitch, Roll and Yaw values
float pitch = 0;
float roll = 0;
float yaw = 0;


double mpu_angle;
double current_angle;
//MPU PARAMETERS

//PID STEERING
double Setpoint_s, Input_s, Output_s;
double Kp_s = 2, Ki_s = 5, Kd_s = 1;
PID myPID_s(&Input_s, &Output_s, &Setpoint_s, Kp_s, Ki_s, Kd_s, DIRECT);
//PID STEERING

//---------------------------------------PID THROTTLE------------------------
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
double Kp_t = 2, Ki_t = 5, Kd_t = 1;
PID myPID_t(&Input_t, &Output_t, &Setpoint_t, Kp_t, Ki_t, Kd_t, DIRECT);
#define throttle_pin 9
//THROTTLE PID

void setup() {
  Serial.begin(115200);
  //------------------------------------------PID STEERING--------------------
  //add delay here to rotate motor max in cc
  //MOTOR
  pinMode(EN, OUTPUT);
  pinMode(R_PWM, OUTPUT);
  pinMode(L_PWM, OUTPUT);
  digitalWrite(EN, HIGH);
  myPID_s.SetMode(AUTOMATIC);
  //myPID_s.SetSampleTime(1);  // refresh rate of PID controller
  myPID_s.SetOutputLimits(-125, 125);
  pwmOut(130);
  delay(3000);
  analogWrite(R_PWM, 0);         // Enabling motor enable pin to reach the desire angle
  analogWrite(L_PWM, 0);
  //MOTOR
  mpu_setup();
  //------------------------------------------PID THROTTLE--------------------
  attachInterrupt(1, sens, RISING);  // hall sensor interrupt
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
  if (Serial.available() > 0) {

    str = Serial.readStringUntil('\n');

  }
  int str_len = str.length() + 1;
  char char_array[str_len];
  str.toCharArray(char_array, str_len);
  char delimiters[] = "[!:,]";
  char* valPosition;
  char* valPosition2;
  valPosition = strtok(char_array, delimiters);
  Setpoint_s  = atoi(valPosition);
  valPosition2 = strtok(NULL, delimiters);
  Setpoint_t = atoi(valPosition2);

  current_angle = mpu_loop();
  Input_s = current_angle;
  myPID_s.Compute();
  pwmOut(Output_s);
  Serial.print("Desired Angle: ");
  Serial.print(Setpoint_s);
  Serial.print(" Feedback Angle: ");
  Serial.print(Input_s);
  Serial.print(" Output PWM: ");
  Serial.print(Output_s);

  Serial.print(" ----------- ");
  Input_t = SPEED;
  linear_actuator_activate(Setpoint_t);
  myPID_t.Compute();
  Serial.print("Desired Speed: ");
  Serial.print(Setpoint_s);
  Serial.print("  Feedback Speed: ");
  Serial.print(Input_t);
  Serial.print(" Output PWM: ");
  Serial.println(Output_t);
  analogWrite(throttle_pin, Output_t);

  if ((millis() - lastturn) > 2000) {       // if there is no signal more than 2 seconds
    SPEED = 0;                              // so, speed is 0
  }





}


void pwmOut(int out) {
  if (out > 0) {                         // if REV > encoderValue motor move in forward direction.
    analogWrite(R_PWM, out);         // Enabling motor enable pin to reach the desire angle
    analogWrite(L_PWM, 0);                           // calling motor to move forward
  }
  else {
    analogWrite(L_PWM, abs(out));         // Enabling motor enable pin to reach the desire angle
    analogWrite(R_PWM, 0);                           // calling motor to move reverse
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



double mpu_loop()
{
   timer = millis();

  // Read normalized values
  Vector norm = mpu.readNormalizeGyro();

  // Calculate Pitch, Roll and Yaw
  pitch = pitch + norm.YAxis * timeStep;
  roll = roll + norm.XAxis * timeStep;
  yaw = yaw + norm.ZAxis * timeStep;

  return yaw;
  delay((timeStep*1000) - (millis() - timer));


}

void mpu_setup()
{
// Initialize MPU6050
  while(!mpu.begin(MPU6050_SCALE_2000DPS, MPU6050_RANGE_2G))
  {
    Serial.println("Could not find a valid MPU6050 sensor, check wiring!");
    delay(500);
  }
  
  // Calibrate gyroscope. The calibration must be at rest.
  // If you don't want calibrate, comment this line.
  mpu.calibrateGyro();

  // Set threshold sensivty. Default 3.
  // If you don't want use threshold, comment this line or set 0.
  mpu.setThreshold(3);
}
