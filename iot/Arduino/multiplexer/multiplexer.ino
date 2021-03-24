
int S0 = 9;  // Digital Pin 3
int S1 = 10;  // Digital Pin 4
int S2 = 11;  // Digital Pin 5



void setup() {
  Serial.begin(9600);
  //all pins are outputs
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);

  pinMode(13, OUTPUT);



}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(S0, LOW);
  digitalWrite(S1, HIGH);
  digitalWrite(S2, HIGH);
  delay(500);
  Serial.println(analogRead(A0));              
}
