import requests
import json #pega dicionario web da api
import pandas #permite importar e exporta dados do excell
import decimal

url = "http://data.fixer.io/api/latest?access_key=8479e3100a9ac573e9b901eceab2b187"
print("Acessando base de dados do Fixer.io...")
resposta = requests.get(url)
print(resposta)

if resposta.status_code == 200:
    print("Acesso realizado com sucesso")
    print("Buscando informações...")
    dados = resposta.json()

    #Moeda que usa para conversão de resultados é o EURO
    dolar_real = round(dados["rates"]["BRL"]/dados["rates"]["USD"],2)
    euro_real = round(dados["rates"]["BRL"]/dados["rates"]["EUR"],2)
    btc_real = round(dados["rates"]["BRL"]/dados["rates"]["BTC"],2)

    tela = pandas.DataFrame({
        "moedas":["Dólar", "Euro", "Bitcoin"],
        "valores":[dolar_real, euro_real, btc_real]
    })
    tela.to_csv("valores.csv", index=False, sep=";", decimal=",")
    print("Arquivo exportado com sucesso")
else:
    print("Erro na base de dados")
