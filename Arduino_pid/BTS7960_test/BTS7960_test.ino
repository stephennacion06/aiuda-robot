 

int EN = 6;
int R_PWM = 4;
int L_PWM = 5;


void setup() {
  // put your setup code here, to run once:
 pinMode(EN, OUTPUT);
 pinMode(R_PWM, OUTPUT);
 pinMode(L_PWM, OUTPUT);
 digitalWrite(EN, HIGH);

      Serial.begin (9600);
   // Reads the initial state of the outputA
   aLastState = digitalRead(outputA);
   Serial.print(aLastState);
}

void loop() {
  int i;
  for(i = 0; i <= 255; i= i+10){ //clockwise rotation
   analogWrite(R_PWM, i);
   analogWrite(L_PWM, 0);
   print_decoder();
   delay(500);
  }
  delay(500);
  for(i = 0; i <= 255; i= i+10){ //counter clockwise rotation
   analogWrite(R_PWM, 0);
   analogWrite(L_PWM, i);
   print_decoder();
   delay(500);
  }
  delay(500);
}

void print_decoder(){

  aState = digitalRead(outputA); // Reads the "current" state of the outputA
   Serial.print(aState);
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB) != aState) { 
       counter ++;
     } else {
       counter --;
     }
     Serial.print("Position: ");
     Serial.println(counter);
   } 
   aLastState = aState; // Updates the previous state of the outputA with the current state
}
