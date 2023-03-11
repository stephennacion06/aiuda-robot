int box_1;
int box_2 ;
int box_3;
int box_4;
int box_5;
int box_6;
int box_7;
int box_8;
int box_9;
int box_10;
int box_11;
int box_12;
int led_control;

String str;
void setup() {

  Serial.begin(9600);

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

  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  digitalWrite(8, LOW);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  digitalWrite(A0, LOW);

}


void loop() {
  if (Serial.available() > 0) {

    str = Serial.readStringUntil('\n');

    int str_len = str.length() + 1;

    // Prepare the character array (the buffer)
    char char_array[str_len];

    // Copy it over
    str.toCharArray(char_array, str_len);

    char delimiters[] = "[!:,]";
    char* valPosition;
    char* valPosition2;
    char* valPosition3;
    char* valPosition4;
    char* valPosition5;
    char* valPosition6;
    char* valPosition7;
    char* valPosition8;
    char* valPosition9;
    char* valPosition10;
    char* valPosition11;
    char* valPosition12;
    char* valPosition13;

    valPosition = strtok(char_array, delimiters);
    box_1  = atoi(valPosition);
    valPosition2 = strtok(NULL, delimiters);
    box_2 = atoi(valPosition2);
    valPosition3 = strtok(NULL, delimiters);
    box_3 = atoi(valPosition3);
    valPosition4 = strtok(NULL, delimiters);
    box_4 = atoi(valPosition4);
    valPosition5 = strtok(NULL, delimiters);
    box_5 = atoi(valPosition5);
    valPosition6 = strtok(NULL, delimiters);
    box_6 = atoi(valPosition6);
    valPosition7 = strtok(NULL, delimiters);
    box_7 = atoi(valPosition7);
    valPosition8 = strtok(NULL, delimiters);
    box_8 = atoi(valPosition8);
    valPosition9 = strtok(NULL, delimiters);
    box_9 = atoi(valPosition9);
    valPosition10 = strtok(NULL, delimiters);
    box_10 = atoi(valPosition10);
    valPosition11 = strtok(NULL, delimiters);
    box_11 = atoi(valPosition11);
    valPosition12 = strtok(NULL, delimiters);
    box_12 = atoi(valPosition12);
    valPosition13 = strtok(NULL, delimiters);
    led_control = atoi(valPosition13);



    control_box();

  }




}
/*
  [1,1,1,1,1,1,1,1,1,1,1,1,1]
  [0,0,0,0,0,0,0,0,0,0,0,0,0]
  [1,0,1,0,1,0,1,0,1,0,1,0,1]


  if(str == "[1,1,1,1,0,0,0,0,0,0]")
  {
   digitalWrite(2,HIGH);
    digitalWrite(3,HIGH);
     digitalWrite(4,HIGH);
      digitalWrite(5,HIGH);
  }
  else if(str == "[0,0,0,0,0,0,0,0,0,0]")
  {
  digitalWrite(2,LOW);
    digitalWrite(3,LOW);
     digitalWrite(4,LOW);
      digitalWrite(5,LOW);
  }
*/





void control_box() {

  if (box_1 == 1) {
    digitalWrite(2, HIGH);
  }
  else {
    digitalWrite(2, LOW);
  }

  if (box_2 == 1) {
    digitalWrite(3, HIGH);
  }
  else {
    digitalWrite(3, LOW);
  }
  if (box_3 == 1) {
    digitalWrite(4, HIGH);
  }
  else {
    digitalWrite(4, LOW);
  }


  if (box_4 == 1) {
    digitalWrite(5, HIGH);
  }
  else {
    digitalWrite(5, LOW);
  }

  if (box_5 == 1) {
    digitalWrite(6, HIGH);
  }
  else {
    digitalWrite(6, LOW);
  }


  if (box_6 == 1) {
    digitalWrite(7, HIGH);
  }
  else {
    digitalWrite(7, LOW);
  }

  if (box_7 == 1) {
    digitalWrite(8, HIGH);
  }
  else {
    digitalWrite(8, LOW);
  }

  if (box_8 == 1) {
    digitalWrite(9, HIGH);
  }
  else {
    digitalWrite(9, LOW);
  }

  if (box_9 == 1) {
    digitalWrite(10, HIGH);
  }
  else {
    digitalWrite(10, LOW);
  }

  if (box_10 == 1) {
    digitalWrite(11, HIGH);
  }
  else {
    digitalWrite(11, LOW);
  }

  if (box_11 == 1) {
    digitalWrite(12, HIGH);
  }
  else {
    digitalWrite(12, LOW);
  }

  if (box_12 == 1) {
    digitalWrite(13, HIGH);
  }
  else {
    digitalWrite(13, LOW);
  }

    if (led_control == 1) {
    digitalWrite(A0, HIGH);
  }
  else {
    digitalWrite(A0, LOW);
  }

}
