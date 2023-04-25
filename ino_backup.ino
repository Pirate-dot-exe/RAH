//backup from 24/04/2023

#include "BluetoothSerial.h"

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

int LED_DIR_PIN = 2; //set pin G2 
int LED_ESQ_PIN = 22;

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
      delay(250);
      digitalWrite(LED_DIR_PIN, LOW);
      delay(250);
    }
    digitalWrite(LED_DIR_PIN, HIGH);
  } 
}
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_DIR_PIN, OUTPUT);
  pinMode(LED_ESQ_PIN, OUTPUT);
  Serial.begin(115200);
  Serial.println("Board Setup running...");
  SerialBT.begin("RAH_Controller"); //Bluetooth device name
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
    if (comando == 'd' || comando == 'D'){
      digitalWrite(LED_DIR_PIN, HIGH);
      digitalWrite(LED_ESQ_PIN, LOW);

      Serial.println("LED direito acesso");
    }else if(comando == 'e' || comando == 'E'){
      digitalWrite(LED_ESQ_PIN, HIGH);
      digitalWrite(LED_DIR_PIN, LOW);
      Serial.println("LED esquerdo acesso");
    }
  }
  delay(1000);
}
