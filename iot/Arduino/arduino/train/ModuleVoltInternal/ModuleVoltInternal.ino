const int voltageSensor = 7;

float vOUT = 0.0;
float vIN = 0.0;
float R1 = 30000.0;
float R2 = 7500.0;
int value = 0;
int value2 = 0;


void setup()
{
Serial.begin(9600);
analogReference(DEFAULT);
delay(1000);
}

void loop()
{
  value = analogRead(voltageSensor);
  vOUT = (value * 5.0) / 1024.0;
  vIN = vOUT / (R2/(R1+R2));
  //Serial.print("Input = ");
  //Serial.println(vIN);
  Serial.print("v1: ");
  Serial.println(vIN);
//  vOUT = (value2 * 5.0) / 1024.0;
//  vIN = vOUT / (R2/(R1+R2));
//  Serial.print("v2 : ");
//  Serial.println(vIN/4.65);
  delay(1000);
}
