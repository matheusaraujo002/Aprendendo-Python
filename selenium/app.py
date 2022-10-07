# Bibliotecas
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inserindo webdriver do Chrome (Versão 106.0.5249.91)
navegador = webdriver.Chrome()

navegador.minimize_window

# Coleta de dados da moeda Dólar

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoDolar = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor do Dólar (em Real):", cotacaoDolar)

# Coleta de dados da moeda Euro

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoEuro = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor do Euro (em Real):", cotacaoEuro)

# Coleta de dados da moeda Iene Japonês

navegador.get("https://www.google.com.br/")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação iene")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

cotacaoIene = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print("Valor do Iene (em Real):", cotacaoIene)

pyautogui.hotkey("Ctrl", "w")

###############################################

import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)