import requests

# Função para enviar os dados para o ThingSpeak
def envia_dados_para_thingspeak(umidade, temperatura):
    # Substitua com sua chave de escrita do ThingSpeak
    chave_de_escrita = "RR6H1FEGDH0C41OK"

    # Configurar os parâmetros para enviar os dados ao ThingSpeak
    url = f"https://api.thingspeak.com/update?api_key={chave_de_escrita}&field1={temperatura}&field2={umidade}"

    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            print("Dados enviados com sucesso para o ThingSpeak!")
        else:
            print(f"Erro ao enviar dados: {resposta.status_code}")
    except Exception as e:
        print(f"Erro ao se comunicar com o ThingSpeak: {e}")
