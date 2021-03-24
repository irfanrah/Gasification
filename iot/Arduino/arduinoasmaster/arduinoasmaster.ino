#include <ModbusMaster.h>               //Library for using ModbusMaster
#include <LiquidCrystal.h>              //Library for using LCD display

#define MAX485_DE      3
#define MAX485_RE_NEG  2

ModbusMaster node;                    //object node for class ModbusMaster

LiquidCrystal lcd(8,9,10,11,12,13);
int anta= 777;
float value = 69;
int ada = 1;
int b= 999;
char c = "woii";


void preTransmission()            //Function for setting stste of Pins DE & RE of RS-485
{
  digitalWrite(MAX485_RE_NEG, 1);             
  digitalWrite(MAX485_DE, 1);
}

void postTransmission()
{
  digitalWrite(MAX485_RE_NEG, 0);
  digitalWrite(MAX485_DE, 0);
}

void setup()
{
  lcd.begin(16,2);
  lcd.print("CIRCUIT DIGEST");
  delay(3000);
  lcd.clear();
  lcd.print("Arduino");
  lcd.setCursor(0,1);
  lcd.print("Modbus Master");
  delay(3000);
  lcd.clear();
  
  pinMode(MAX485_RE_NEG, OUTPUT);
  pinMode(MAX485_DE, OUTPUT);
  
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  
  digitalWrite(MAX485_RE_NEG, 0);
  digitalWrite(MAX485_DE, 0);

  Serial.begin(115200);             //Baud Rate as 115200

  node.begin(1, Serial);            //Slave ID as 1
  node.preTransmission(preTransmission);         //Callback for configuring RS-485 Transreceiver correctly
  node.postTransmission(postTransmission);

}

void loop()
{
  
  
  node.writeSingleRegister(0x40001,value);        //Writes value to 0x40000 holding register
  node.writeSingleRegister(0x40002,anta);
  node.writeSingleRegister(0x40003,b);
  node.writeSingleRegister(0x40004,ada);
  
 
  anta = anta + 1;                          //Reads state of push button 
  ada = ada *2 ;
  delay(300);
  if (ada > 8000){
    ada = 1;
  }
  
  
 
}
