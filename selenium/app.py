# Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Inserindo webdriver do Chrome (Versão 106.0.5249.91)
navegador = webdriver.Chrome()

## Navegador invisível Em Breve ##

navegador.minimize_window()

print("●❯────────────────────────────────────────────❮●")

# Coleta de dados da moeda Dólar.

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoDolar = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor atual do Dólar (em Real):", cotacaoDolar)

# Coleta de dados da moeda Euro.

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoEuro = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor atual do Euro (em Real):", cotacaoEuro)

# Coleta de dados da moeda Iene Japonês.

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação iene")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoIene = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor atual do Iene (em Real):", cotacaoIene)

# Fechar navegador após a conclusão da coleta de dados.
navegador.quit()

print("●❯──────────────────────────────────────────────────────────────────────────────────────────❮●")

import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")

tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacaoDolar)

tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacaoEuro)

tabela.loc[tabela["Moeda"] == "Iene", "Cotação"] = float(cotacaoIene)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

print(tabela)
print("●❯──────────────────────────────────────────────────────────────────────────────────────────❮●")

# Criando novo documento com a tabela atualizada.
tabela.to_excel("Produtos Novo.xlsx", index=False)