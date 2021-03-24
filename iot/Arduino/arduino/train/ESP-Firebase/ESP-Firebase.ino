

#include <FirebaseESP8266.h>
#include <ESP8266WiFi.h>


//1. Change the following info

#define FIREBASE_HOST "iot-gasification-default-rtdb.firebaseio.com/" //Without http:// or https:// schemes
#define FIREBASE_AUTH "lR2KGi82Mfxohs4EdMupz8n1qUnDd8PpDHmehEeF"
#define WIFI_SSID "Pucang Anom"
#define WIFI_PASSWORD "Dukuhkt1244"



//2. Define FirebaseESP8266 data object for data sending and receiving
FirebaseData firebaseData;
int Motor_1;
int Motor_2;
int Motor_3;
int Motor_4;

void setup()
{

  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  
}


void loop()
{
  Motor_1 = random(10,100);
  Motor_2 = random(-100,0);
  Motor_3 = random(100,1000); 
  Motor_4 = random(10000,10100);
   // set value 
  Firebase.setInt(firebaseData,"Motor/Motor_1",Motor_1);
  Firebase.setInt(firebaseData,"Motor/Motor_2",Motor_2);
  Firebase.setInt(firebaseData,"Motor/Motor_3",Motor_3);
  Firebase.setInt(firebaseData,"Motor/Motor_4",Motor_4);
  Serial.print(Motor_1);
  Serial.print(Motor_2);
  Serial.print(Motor_3);
  Serial.println(Motor_4);
  
  delay(500); 
  


}
