#include <PID_v1.h>

//---------------------------------THROTTLE--------------------------//
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

//---------------------------------STEERING--------------------------//


//DC MOTOR
int EN = 6;
int R_PWM = 4;
int L_PWM = 5;

//DC MOTOR


// MPU PARAMETERS
#include "I2Cdev.h"

#include "MPU6050_6Axis_MotionApps20.h"

#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
#include "Wire.h"
#endif

MPU6050 mpu;

#define OUTPUT_READABLE_YAWPITCHROLL

#define INTERRUPT_PIN 19  // use pin 2 on Arduino Uno & most boards
#define LED_PIN 13 // (Arduino is 13, Teensy is 11, Teensy++ is 6)
bool blinkState = false;

// MPU control/status vars
bool dmpReady = false;  // set true if DMP init was successful
uint8_t mpuIntStatus;   // holds actual interrupt status byte from MPU
uint8_t devStatus;      // return status after each device operation (0 = success, !0 = error)
uint16_t packetSize;    // expected DMP packet size (default is 42 bytes)
uint16_t fifoCount;     // count of all bytes currently in FIFO
uint8_t fifoBuffer[64]; // FIFO storage buffer

// orientation/motion vars
Quaternion q;           // [w, x, y, z]         quaternion container
VectorInt16 aa;         // [x, y, z]            accel sensor measurements
VectorInt16 aaReal;     // [x, y, z]            gravity-free accel sensor measurements
VectorInt16 aaWorld;    // [x, y, z]            world-frame accel sensor measurements
VectorFloat gravity;    // [x, y, z]            gravity vector
float euler[3];         // [psi, theta, phi]    Euler angle container
float ypr[3];           // [yaw, pitch, roll]   yaw/pitch/roll container and gravity vector

// packet structure for InvenSense teapot demo
uint8_t teapotPacket[14] = { '$', 0x02, 0, 0, 0, 0, 0, 0, 0, 0, 0x00, 0x00, '\r', '\n' };


volatile bool mpuInterrupt = false;     // indicates whether MPU interrupt pin has gone high
void dmpDataReady() {
  mpuInterrupt = true;
}

double mpu_angle;
double current_angle;
//MPU PARAMETERS

//PID STEERING
double Setpoint_s, Input_s, Output_s;
double Kp_s = 2, Ki_s = 5, Kd_s = 1;
PID myPID_s(&Input_s, &Output_s, &Setpoint_s, Kp_s, Ki_s, Kd_s, DIRECT);
//PID STEERING




void setup() {
  Serial.begin(115200);  
    //-------------------------------STEERING-------------------------//
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
  //-------------------------------THROTTLE-------------------------//
               // configure serial for debug
  attachInterrupt(5, sens, RISING);  // hall sensor interrupt
  myPID_t.SetMode(AUTOMATIC);
  pinMode(extend_pin, OUTPUT);
  pinMode(retract_pin, OUTPUT);
  pinMode(throttle_pin, OUTPUT);

}



void loop() {
  //PARSING SPEED, ANGLE
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
  Setpoint_t  = atoi(valPosition);
  valPosition2 = strtok(NULL, delimiters);
  Setpoint_s = atoi(valPosition2);
  //PARSING SPEED, ANGLE

  //Serial.println("-----------------------PID STEERING------------------");
  current_angle = mpu_loop();
  Input_s = current_angle;
  myPID_s.Compute();
  pwmOut(Output_s);
  Serial.print("  Desired Angle: ");
  Serial.print(Setpoint_s);
  Serial.print(" Feedback Angle: ");
  Serial.print(Input_s);
  Serial.print(" Output: ");
  Serial.print(Output_s);
  Serial.print("  --------- ");
  Input_t = SPEED;
  linear_actuator_activate(Setpoint_t);
  myPID_t.Compute();
  
  //Serial.println("-----------------------PID THROTTLE------------------");
  Serial.print("Desired Speed: ");
  Serial.print(Setpoint_s);
  Serial.print("  Feedback: ");
  Serial.print(Input_t);
  Serial.print("  Output: ");
  Serial.println(Output_t);
  analogWrite(throttle_pin, Output_t);

  if ((millis() - lastturn) > 2000) {       // if there is no signal more than 2 seconds
    SPEED = 0;                              // so, speed is 0
  }

}


double mpu_loop()
{
  if (!dmpReady) return;

  // wait for MPU interrupt or extra packet(s) available
  while (!mpuInterrupt && fifoCount < packetSize) {
    if (mpuInterrupt && fifoCount < packetSize) {
      // try to get out of the infinite loop
      fifoCount = mpu.getFIFOCount();
    }
  }

  // reset interrupt flag and get INT_STATUS byte
  mpuInterrupt = false;
  mpuIntStatus = mpu.getIntStatus();

  // get current FIFO count
  fifoCount = mpu.getFIFOCount();
  if (fifoCount < packetSize) {
    //Lets go back and wait for another interrupt. We shouldn't be here, we got an interrupt from another event
    // This is blocking so don't do it   while (fifoCount < packetSize) fifoCount = mpu.getFIFOCount();
  }
  // check for overflow (this should never happen unless our code is too inefficient)
  else if ((mpuIntStatus & (0x01 << MPU6050_INTERRUPT_FIFO_OFLOW_BIT)) || fifoCount >= 1024) {
    // reset so we can continue cleanly
    mpu.resetFIFO();
    //  fifoCount = mpu.getFIFOCount();  // will be zero after reset no need to ask
    Serial.println(F("FIFO overflow!"));

    // otherwise, check for DMP data ready interrupt (this should happen frequently)
  } else if (mpuIntStatus & (0x01 << MPU6050_INTERRUPT_DMP_INT_BIT)) {

    // read a packet from FIFO
    while (fifoCount >= packetSize) { // Lets catch up to NOW, someone is using the dreaded delay()!
      mpu.getFIFOBytes(fifoBuffer, packetSize);
      // track FIFO count here in case there is > 1 packet available
      // (this lets us immediately read more without waiting for an interrupt)
      fifoCount -= packetSize;
    }
#ifdef OUTPUT_READABLE_YAWPITCHROLL
    // display Euler angles in degrees
    mpu.dmpGetQuaternion(&q, fifoBuffer);
    mpu.dmpGetGravity(&gravity, &q);
    mpu.dmpGetYawPitchRoll(ypr, &q, &gravity);
    mpu_angle = ypr[0] * 180 / M_PI;
    //Serial.println(mpu_angle);
    return mpu_angle;

#endif

    blinkState = !blinkState;
    digitalWrite(LED_PIN, blinkState);
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

void sens() {
  if (millis() - lastturn > 80) {    // simple noise cut filter (based on fact that you will not be ride your bike more than 120 km/h =)
    SPEED = w_length / ((float)(millis() - lastturn) / 1000) * 3.6;   // calculate speed
    SPEED = SPEED / 1.609;

    lastturn = millis();                                              // remember time of last revolution                                // calculate distance
  }
}




void mpu_setup()
{
  // join I2C bus (I2Cdev library doesn't do this automatically)
#if I2CDEV_IMPLEMENTATION == I2CDEV_ARDUINO_WIRE
  Wire.begin();
  Wire.setClock(400000); // 400kHz I2C clock. Comment this line if having compilation difficulties
#elif I2CDEV_IMPLEMENTATION == I2CDEV_BUILTIN_FASTWIRE
  Fastwire::setup(400, true);
#endif

  while (!Serial); // wait for Leonardo enumeration, others continue immediately

  // initialize device
  Serial.println(F("Initializing I2C devices..."));
  mpu.initialize();
  pinMode(INTERRUPT_PIN, INPUT);

  // verify connection
  Serial.println(F("Testing device connections..."));
  Serial.println(mpu.testConnection() ? F("MPU6050 connection successful") : F("MPU6050 connection failed"));
  Serial.println(F("Initializing DMP..."));
  devStatus = mpu.dmpInitialize();
  // supply your own gyro offsets here, scaled for min sensitivity
  mpu.setXGyroOffset(220);
  mpu.setYGyroOffset(76);
  mpu.setZGyroOffset(-85);
  mpu.setZAccelOffset(1788); // 1688 factory default for my test chip
  if (devStatus == 0) {
    // Calibration Time: generate offsets and calibrate our MPU6050
    mpu.CalibrateAccel(6);
    mpu.CalibrateGyro(6);
    mpu.PrintActiveOffsets();
    // turn on the DMP, now that it's ready
    Serial.println(F("Enabling DMP..."));
    mpu.setDMPEnabled(true);

    // enable Arduino interrupt detection
    Serial.print(F("Enabling interrupt detection (Arduino external interrupt "));
    Serial.print(digitalPinToInterrupt(INTERRUPT_PIN));
    Serial.println(F(")..."));
    attachInterrupt(digitalPinToInterrupt(INTERRUPT_PIN), dmpDataReady, RISING);
    mpuIntStatus = mpu.getIntStatus();

    // set our DMP Ready flag so the main loop() function knows it's okay to use it
    Serial.println(F("DMP ready! Waiting for first interrupt..."));
    dmpReady = true;

    // get expected DMP packet size for later comparison
    packetSize = mpu.dmpGetFIFOPacketSize();
  } else {
    // ERROR!
    // 1 = initial memory load failed
    // 2 = DMP configuration updates failed
    // (if it's going to break, usually the code will be 1)
    Serial.print(F("DMP Initialization failed (code "));
    Serial.print(devStatus);
    Serial.println(F(")"));
  }

  // configure LED for output
  pinMode(LED_PIN, OUTPUT);
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
