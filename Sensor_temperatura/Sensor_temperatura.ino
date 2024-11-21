#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include "DHTesp.h"

DHTesp dht;

const char* ssid = "Intelbras";
const char* password = "Junior04";

ESP8266WebServer server(80);

void handleRoot() {
  String umidade = String(dht.getHumidity());
  String temperatura = String(dht.getTemperature());
 
  server.send(200, "text/plain", umidade + " e " + temperatura);  // 70.0 e 23.0
}

void handleNotFound(){
  String message = "File Not Found\n";
  server.send(404, "text/plain", message);
}

void setup(void){
  dht.setup(14, DHTesp::DHT11); // D5
  Serial.begin(115200);
  Serial.println("Iniciando...");
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("Tentando conectar ao Wi-Fi...");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");  // Exibe ponto enquanto tenta conectar
  }

  Serial.println("");
  Serial.print("Conectado a ");
  Serial.println(ssid);
  Serial.print("Endereço IP: ");
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    Serial.println("MDNS responder iniciado");
  }

  server.on("/", handleRoot);
  server.onNotFound(handleNotFound);

  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

void loop(void){
  server.handleClient();
  delay(1500);
  float u = dht.getHumidity();
  float t = dht.getTemperature();

  Serial.print("Umidade (%): ");
  Serial.print(u, 1);
  Serial.print("\t");
  Serial.print("Temperatura (C): ");
  Serial.print(t, 1);
  Serial.println();
}

