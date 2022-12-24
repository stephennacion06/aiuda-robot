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
double pid_p = 0, pid_i = 0, pid_d = 0;
PID myPID_s(&Input_s, &Output_s, &Setpoint_s, Kp_s, Ki_s, Kd_s, DIRECT);
//PID STEERING


//PARSING SPEED,ANGLE
String str;
//PARSING SPEED, ANGLE

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

}

void loop() {
  // Read Input
  if (Serial.available() > 0) {

    str = Serial.readStringUntil('\n');

  }
  
  int str_len = str.length() + 1;
  char char_array[str_len];
  str.toCharArray(char_array, str_len);
  char delimiters[] = "[!:,]";
  char* valPosition;
  char* valPosition2;
  char* valPosition3;
  char* valPosition4;
  valPosition = strtok(char_array, delimiters);
  Setpoint_s  = atoi(valPosition);
  valPosition2 = strtok(NULL, delimiters);
  pid_p = atoi(valPosition2);
  valPosition3 = strtok(NULL, delimiters);
  pid_i = atoi(valPosition3);
  valPosition4 = strtok(NULL, delimiters);
  pid_d = atoi(valPosition4);
  
  
  current_angle = mpu_loop();
  Input_s = current_angle;
  
  // Update PID Parameters
  myPID_s.SetTunings(pid_p, pid_i, pid_d);
  
  // Compute PID Parameters 
  myPID_s.Compute();

  // PWM the output of PID
  pwmOut(Output_s);

  // Display Output
  Serial.print("Kp: ");
  Serial.print(pid_p);
  Serial.print(" Ki: ");
  Serial.print(pid_i);
  Serial.print(" Kd: ");
  Serial.print(pid_d);
  Serial.print(" Desired Angle: ");
  Serial.print(Setpoint_s);
  Serial.print(" Feedback Angle: ");
  Serial.print(Input_s);
  Serial.print(" Output PWM: ");
  Serial.println(Output_s);
  
}



// Function for Steering

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





// MPU FUNCTIONS

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
