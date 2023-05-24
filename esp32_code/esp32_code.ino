//backup from 08/05/2023

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

int LED_DIR_PIN = 2; //set pin G2 
int LED_ESQ_PIN = 22;//set pin G22
int MOTOR_1_ESQ = 19;
int MOTOR_1_DIR = 18; 
int MOTOR_1_CIMA = 17;
int MOTOR_1_BAIXO = 21;

void BT_STATUS(esp_spp_cb_event_t event, esp_spp_cb_param_t *param){
  if (event == ESP_SPP_SRV_OPEN_EVT){
    Serial.println("connected!");
    digitalWrite(LED_ESQ_PIN, HIGH);
    digitalWrite(LED_DIR_PIN, LOW);
  }else{
    digitalWrite(LED_ESQ_PIN, LOW);
    Serial.println("disconnected!");
    for(int tentativa=1; tentativa <= 3 && event != ESP_SPP_SRV_OPEN_EVT; tentativa++){
      digitalWrite(LED_DIR_PIN, HIGH);
      delay(100);
      digitalWrite(LED_DIR_PIN, LOW);
      delay(100);
    }
    digitalWrite(LED_DIR_PIN, HIGH);
  } 
}
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_DIR_PIN, OUTPUT);
  pinMode(LED_ESQ_PIN, OUTPUT);

  pinMode(MOTOR_1_ESQ, OUTPUT);
  pinMode(MOTOR_1_DIR, OUTPUT);
  pinMode(MOTOR_1_CIMA, OUTPUT);
  pinMode(MOTOR_1_BAIXO, OUTPUT);
  
  Serial.begin(115200);
  Serial.println("Board Setup running...");
  SerialBT.begin("RAH_Controller"); //Bluetooth device name
  Serial.println("Running modules test");
  digitalWrite(LED_DIR_PIN, HIGH);
  digitalWrite(LED_DIR_PIN, LOW);
  digitalWrite(LED_ESQ_PIN, HIGH);
  digitalWrite(LED_ESQ_PIN, LOW);
  Serial.println("The device started, now you can pair it with bluetooth!");
  SerialBT.register_callback (BT_STATUS);
  Serial.println("Board Setup complete!");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    SerialBT.write(Serial.read());
  }
  if (SerialBT.available()) {
    char comando = SerialBT.read();
    Serial.println(comando);
    if (comando == 'q' || comando == 'Q'){
      digitalWrite(MOTOR_1_ESQ, HIGH);
      digitalWrite(MOTOR_1_DIR, LOW);
      digitalWrite(MOTOR_1_CIMA, HIGH);
      digitalWrite(MOTOR_1_BAIXO, LOW);
      Serial.println("Q");
      delay(1);
    }else if(comando == 'e' || comando == 'E'){
      digitalWrite(MOTOR_1_DIR, HIGH);
      digitalWrite(MOTOR_1_ESQ, LOW);
      digitalWrite(MOTOR_1_CIMA, HIGH);
      digitalWrite(MOTOR_1_BAIXO, LOW);
      Serial.println("E");
      delay(1);
    }else if(comando == 'c' || comando == 'C'){
      digitalWrite(MOTOR_1_DIR, HIGH);
      digitalWrite(MOTOR_1_ESQ, LOW);
      digitalWrite(MOTOR_1_BAIXO, HIGH);
      digitalWrite(MOTOR_1_CIMA, LOW);
      Serial.println("C");
      delay(1);
    }else if(comando == 'z' || comando == 'Z'){
      digitalWrite(MOTOR_1_ESQ, HIGH);
      digitalWrite(MOTOR_1_DIR, LOW);
      digitalWrite(MOTOR_1_BAIXO, HIGH);
      digitalWrite(MOTOR_1_CIMA, LOW);
      Serial.println("Z");
      delay(1);
    }
  }
  delay(1000);
}