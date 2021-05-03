

const int SF = A5;
const int VG = A4;
const int BP = A3;
const int BH = A2;

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
  FreqSF = count;
  delay(1);
  FreqVG = count*2;
  delay(1);
  FreqBP = count;
  delay(1);
  FreqBH = count;
  delay(1);

  
  
  Serial.print(FreqSF);
  Serial.print(",");
  Serial.print(FreqVG);
  Serial.print(",");
  Serial.print(FreqBP);
  Serial.print(",");
  Serial.println(FreqBH);
  
  delay(500);
  count = count + 5; 
  }
