

const int SF = A2;
const int VG = A4;
const int BP = A5;
const int BH = A3;

int motor[6] = {0,0,0,0,0,0};

float FreqSF = 0;
float FreqVG = 0;
float FreqBP = 0;
float FreqBH = 0;

int count = 0;

void setup() {
 
  Serial.begin(9600);
}

void loop() {
  FreqSF = analogRead(SF);
  delay(1);
  FreqVG = analogRead(VG);
  delay(1);
  FreqBP = analogRead(BP);
  delay(1);
  FreqBH = analogRead(BH);
  delay(1);

  
  
  Serial.print(FreqSF);
  Serial.print(",");
  Serial.print(FreqVG);
  Serial.print(",");
  Serial.print(FreqBP);
  Serial.print(",");
  Serial.println(FreqBH);
  
  delay(500); 

  if(count == 5){
    Serial.flush();
  }

  count = count + 1;
  }
