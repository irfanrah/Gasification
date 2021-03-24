

#include <FirebaseESP8266.h>
#include <ESP8266WiFi.h>


//1. Change the following info

#define FIREBASE_HOST "iot-gasification-default-rtdb.firebaseio.com/" //Without http:// or https:// schemes
#define FIREBASE_AUTH "lR2KGi82Mfxohs4EdMupz8n1qUnDd8PpDHmehEeF"
#define WIFI_SSID "Pucang Anom"
#define WIFI_PASSWORD "Dukuhkt1244"



//2. Define FirebaseESP8266 data object for data sending and receiving
FirebaseData firebaseData;
int numb;
String myString;

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
  numb = random(10,100);
  myString = String(numb); 
  Serial.println(myString); 
   // set value 
  Firebase.setString(firebaseData,"Status",myString);
  delay(500); 


}
