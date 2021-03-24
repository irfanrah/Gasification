#include "max6675.h"

const int SF = A0;
const int VG = A2;
const int BP = A1;
const int BH = A5;

const int thermoDO1 = 9;
const int thermoCS1 =10;
const int thermoCLK1 = 11;
const int thermoDO2 = 7;
const int thermoCS2 = 6;
const int thermoCLK2 = 7;
const int thermoDO3 = 8;
const int thermoCS3 = 9;
const int thermoCLK3 = 10;
const int thermoDO4 = 13;
const int thermoCS4 = 12;
const int thermoCLK4 = 11;

int FreqSF = 0;
int FreqVG = 0;
int FreqBP = 0;
int FreqBH = 0;

float temp1 = 0;
float temp2 = 0;
float temp3 = 0;
float temp4 = 0;


MAX6675 thermocouple1(thermoCLK1, thermoCS1, thermoDO1);
MAX6675 thermocouple2(thermoCLK2, thermoCS2, thermoDO2);
MAX6675 thermocouple3(thermoCLK3, thermoCS3, thermoDO3);
MAX6675 thermocouple4(thermoCLK4, thermoCS4, thermoDO4);


int motor[6] = {0,0,0,0,0,0};
int temp[6] = {0,0,0,0,0,0};


void setup() {
 
  Serial.begin(9600);
}

void loop() {
  FreqSF = analogRead(SF);
  delay(10);
  FreqVG = analogRead(VG);
  delay(10);
  FreqBP = analogRead(BP);
  delay(10);
  FreqBH = analogRead(BH);
  delay(10);

  temp1 = thermocouple1.readCelsius();
  delay(10);
  temp2 = thermocouple2.readCelsius();
  delay(10);
  temp3 = thermocouple3.readCelsius();
  delay(10);
  temp4 = thermocouple4.readCelsius();
  delay(10);

  motor[0] = FreqSF;
  motor[1] = FreqVG;
  motor[2] = FreqBP;
  motor[3] = FreqBH;
  delay(10);

  temp[0] = temp1;
  temp[1] = temp2;
  temp[2] = temp3;
  temp[3] = temp4;

  /*Serial.print(motor[0]);
  Serial.print(" ");
  Serial.print(motor[2]);
  Serial.print(" ");
  Serial.println(motor[3]);
  */
  /*for(int i = 0; i < 5; i++){
    Serial.print(motor[i]);
    Serial.print(" , ");
  }
  Serial.println(" ");
  for(int i = 0; i < 5; i++){
    Serial.print(temp[i]);
    Serial.print(" , ");
  }
  Serial.println(" ");
  //Serial.print(motor);
  //Serial.println(temp);
  */
  Serial.println(thermocouple1.readCelsius());
  
  delay(500); 

}
