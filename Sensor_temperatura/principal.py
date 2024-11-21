from PyQt5 import uic, QtWidgets, QtCore
import requests
import time
from sensor_utils import envia_dados_para_thingspeak  # Função que envia para o ThingSpeak

class WorkerThread(QtCore.QThread):
    # Sinal para enviar dados da thread de trabalho para a thread principal
    dados_atualizados = QtCore.pyqtSignal(str, str)

    def run(self):
        while True:
            time.sleep(2)  # Intervalo de 2 segundos entre leituras
            resposta = requests.get('http://192.168.18.70/')  # Endereço do Arduino
            dados = resposta.text  # Dados recebidos do Arduino
            dados_separados = dados.split("e")
            umidade = dados_separados[0][0:4] + "%"  # Extraindo a umidade
            temperatura = dados_separados[1][0:4] + " °C"  # Extraindo a temperatura

            # Enviar dados para o ThingSpeak
            envia_dados_para_thingspeak(umidade, temperatura)

            # Emitir os dados obtidos para a interface
            self.dados_atualizados.emit(umidade, temperatura)


def atualiza_dados(umidade, temperatura):
    # Atualiza os labels da tela com os dados recebidos
    tela.label_6.setText(temperatura)
    tela.label_7.setText(umidade)


# Inicializa a aplicação Qt
app = QtWidgets.QApplication([])

# Carrega a interface
tela = uic.loadUi("C:/Users/freds/OneDrive/Documentos/Faculdade/Sensor/Sensor_temperatura/tela_monitor.ui")

# Cria e conecta o sinal para atualizar a UI
worker = WorkerThread()
worker.dados_atualizados.connect(atualiza_dados)

# Inicia a thread
worker.start()

# Exibe a interface
tela.show()

# Inicia o loop de eventos da aplicação
app.exec()
