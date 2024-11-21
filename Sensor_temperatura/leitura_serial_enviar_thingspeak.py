import serial
import time

# Configure a porta serial (substitua pelo seu número de porta)
arduino = serial.Serial('COM4', 115200)  # No Windows geralmente é COM1, COM3, etc.
time.sleep(2)  # Aguarda a conexão ser estabelecida

while True:
    if arduino.in_waiting > 0:
        dados = arduino.readline().decode('utf-8').strip()
        print(f'Dados recebidos: {dados}')
        # Agora, você pode passar os dados para o ThingSpeak ou outra API.
