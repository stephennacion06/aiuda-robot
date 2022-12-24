#include <PIDController.h>
volatile long int encoder_pos = 0;
PIDController pos_pid; 
int motor_value = 255;
unsigned int integerValue=0;  // Max value is 65535
char incomingByte;
void setup() {

  Serial.begin(9600);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  digitalWrite(6,HIGH);
  attachInterrupt(digitalPinToInterrupt(2), encoder, RISING);

  pos_pid.begin();    
  pos_pid.tune(15, 0, 2000);    
  pos_pid.limit(-255, 255);
}

void loop() {

if (Serial.available() > 0) {  
    integerValue = 0;        
    while(1) {           
      incomingByte = Serial.read();
      if (incomingByte == '\n') break;   
      if (incomingByte == -1) continue;  
      integerValue *= 10;  
      integerValue = ((incomingByte - 48) + integerValue);
      pos_pid.setpoint(integerValue);
    }
}

   motor_value = pos_pid.compute(encoder_pos/5);
if(motor_value > 0){
  MotorCounterClockwise(motor_value);
}else{
  MotorClockwise(abs(motor_value));
}
  Serial.println(encoder_pos/5);
  delay(10);
}



void encoder(){

  if(digitalRead(2) == HIGH){
    encoder_pos++;
  }else{
    encoder_pos--;
  }
}

void MotorClockwise(int power){
  if(power > 100){
  analogWrite(5, power);
  digitalWrite(4, LOW);
  }else{
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
  }
}

void MotorCounterClockwise(int power){
  if(power > 100){
  analogWrite(4, power);
  digitalWrite(5, LOW);
  }else{
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
  }
}
