# PROJETO CDBot

# PARTE 1
# Automação do acesso

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import bs4
import pandas as pd
import requests
import urllib.request

from urllib.request import urlopen
from bs4 import BeautifulSoup

proposicoes = webdriver.Chrome()
proposicoes.implicitly_wait(10)

proposicoes.get('https://dadosabertos.camara.leg.br')
proposicoes.find_element(By.XPATH, '//*[@id="so-api"]/div/div/section[2]/a/div/h2').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div/div').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[1]/div[2]/button').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/button').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div/input').send_keys('PEC')
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/button').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[2]/input').send_keys('PLP')
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/button').click()
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/div[2]/div[3]/input').send_keys('PL')
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[12]/td[2]/input').send_keys('2021-09-21')
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[2]/div[2]/table/tbody/tr[13]/td[2]/input').send_keys('2021-09-24')
proposicoes.find_element(By.XPATH, '//*[@id="operations-Proposições-searchUsingGET_2"]/div[2]/div/div[3]/button').click()
proposicoes.find_element(By.CLASS_NAME, 'request-url').text

# URL - resultado da automação

request_url = proposicoes.find_element(By.CLASS_NAME, 'request-url').text
request_url

# PARTE 2
# Extração e tratamento de dados

response = urlopen(request_url)
html = response.read()
html = html.decode('utf-8')
html.split()
" " .join(html.split())
" " .join(html.split()).replace('> <', '><')

def data_html(input):
    return " ".join(input.split()).replace('> <', '><')

pcontent = BeautifulSoup(html, 'html.parser')
pcontent

# Criação de dicionário

pcontent = pdict

pdict = {"dados":[{"id":15419,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/15419","siglaTipo":"PL","codTipo":139,"numero":407,"ano":1999,"ementa":"Dá nova redação ao art. 7º e ao art. 12 da Lei nº 8.935, de 18 de novembro de 1994, ampliando a competência dos oficiais de registro civil das pessoas naturais e de interdições e tutelas."},{"id":15646,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/15646","siglaTipo":"PL","codTipo":139,"numero":606,"ano":1999,"ementa":"Dispõe sobre a suspensão do pagamento das prestações habitacionais do Sistema Financeiro da Habitação pelos mutuários desempregados das Regiões Norte, Nordeste e Centro-Oeste."},{"id":19217,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/19217","siglaTipo":"PL","codTipo":139,"numero":3174,"ano":1997,"ementa":"Altera a Lei nº 5.700, de 1º de setembro de 1971, que dispõe sobre a forma e a apresentação dos Símbolos Nacionais e dá outras providências."},{"id":19886,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/19886","siglaTipo":"PL","codTipo":139,"numero":3587,"ano":2000,"ementa":"Dispõe sobre aerolevantamento e levantamento espacial no território nacional, e dá outras providências."},{"id":20718,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/20718","siglaTipo":"PL","codTipo":139,"numero":4186,"ano":1998,"ementa":"Modifica a Lei nº 9.612, de 19 de fevereiro de 1998, que \"Institui o Serviço de Radiodifusão Comunitária e dá outras providências\"."},{"id":20888,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/20888","siglaTipo":"PL","codTipo":139,"numero":4445,"ano":1998,"ementa":"Revoga a Lei nº 7.960, de 1989 que dispõe sobre prisão temporária."},{"id":20956,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/20956","siglaTipo":"PL","codTipo":139,"numero":4550,"ano":1998,"ementa":"Altera o art. 389 do Decreto-Lei nº 5.452, de 1º de maio de 1943 (Consolidação das Leis do Trabalho - CLT)."},{"id":336532,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/336532","siglaTipo":"PL","codTipo":139,"numero":7576,"ano":2006,"ementa":"Altera a Lei nº 9.250, de 26 de dezembro de 1995, que altera a legislação do imposto de renda das pessoas físicas e dá outras providências, para fixar prazo e encargos financeiros relativos ao valor a restituir do imposto de renda das pessoas físicas pago a maior."},{"id":339301,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/339301","siglaTipo":"PL","codTipo":139,"numero":7700,"ano":2006,"ementa":"Altera o art. 2º da Lei nº 11.096, de 13 de janeiro de 2005, para estender o atendimento do Programa Universidade para Todos aos estudantes beneficiados com bolsa parcial no ensino médio privado."},{"id":340144,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/340144","siglaTipo":"PL","codTipo":139,"numero":64,"ano":2007,"ementa":"Cria o Índice Nacional de Responsabilidade Social - INRS e o Cadastro Nacional de Inadimplentes Sociais - CNIS."},{"id":345103,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/345103","siglaTipo":"PL","codTipo":139,"numero":478,"ano":2007,"ementa":"Dispõe sobre o Estatuto do Nascituro e dá outras providências."},{"id":359891,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/359891","siglaTipo":"PL","codTipo":139,"numero":1609,"ano":2007,"ementa":"Dispõe sobre a substituição gradativa, em todo o território nacional, de combustíveis derivados de petróleo por outros produzidos a partir da biomassa, e dá outras providências."},{"id":363834,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/363834","siglaTipo":"PL","codTipo":139,"numero":1836,"ano":2007,"ementa":"Altera o § 1º do art. 19-I da Lei nº 8.080, de 19 de setembro de 1990, incluído pela Lei nº 10.424, de 15 de abril de 2002, para acrescentar ao Sistema Único de Saúde - SUS o fornecimento de medicamentos de uso continuado não sujeitos a controle especial, entre outros, necessários ao cuidado integral dos pacientes em seu domicílio."},{"id":404399,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/404399","siglaTipo":"PL","codTipo":139,"numero":3723,"ano":2008,"ementa":"Dispõe sobre o tratamento tributário aplicável às sociedades cooperativas em geral no âmbito federal."},{"id":415684,"uri":"https://dadosabertos.camara.leg.br/api/v2/proposicoes/415684","siglaTipo":"PL","codTipo":139,"numero":4294,"ano":2008,"ementa":"Acrescenta parágrafo ao art. 1.632 da Lei nº 10.406, de 10 de janeiro de 2002 -  Código Civil e ao art. 3° da Lei nº 10.741, de 1ª de outubro de 2003 - Estatuto do Idoso,  de modo a estabelecer a indenização por dano moral em razão do abandono afetivo."}],"links":[{"rel":"self","href":"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&amp;siglaTipo=PLP&amp;siglaTipo=PL&amp;dataInicio=2021-09-21&amp;dataFim=2021-09-24&amp;ordem=ASC&amp;ordenarPor=id"},{"rel":"next","href":"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&amp;siglaTipo=PLP&amp;siglaTipo=PL&amp;dataInicio=2021-09-21&amp;dataFim=2021-09-24&amp;ordem=ASC&amp;ordenarPor=id&amp;pagina=2&amp;itens=15"},{"rel":"first","href":"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&amp;siglaTipo=PLP&amp;siglaTipo=PL&amp;dataInicio=2021-09-21&amp;dataFim=2021-09-24&amp;ordem=ASC&amp;ordenarPor=id&amp;pagina=1&amp;itens=15"},{"rel":"last","href":"https://dadosabertos.camara.leg.br/api/v2/proposicoes?siglaTipo=PEC&amp;siglaTipo=PLP&amp;siglaTipo=PL&amp;dataInicio=2021-09-21&amp;dataFim=2021-09-24&amp;ordem=ASC&amp;ordenarPor=id&amp;pagina=58&amp;itens=15"}]}

del pdict ["links"]
pdict

print(pdict['dados'])

# Preparação dos dados

pdata = [{'id': 15419, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/15419', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 407, 'ano': 1999, 'ementa': 'Dá nova redação ao art. 7º e ao art. 12 da Lei nº 8.935, de 18 de novembro de 1994, ampliando a competência dos oficiais de registro civil das pessoas naturais e de interdições e tutelas.'}, {'id': 15646, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/15646', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 606, 'ano': 1999, 'ementa': 'Dispõe sobre a suspensão do pagamento das prestações habitacionais do Sistema Financeiro da Habitação pelos mutuários desempregados das Regiões Norte, Nordeste e Centro-Oeste.'}, {'id': 19217, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/19217', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 3174, 'ano': 1997, 'ementa': 'Altera a Lei nº 5.700, de 1º de setembro de 1971, que dispõe sobre a forma e a apresentação dos Símbolos Nacionais e dá outras providências.'}, {'id': 19886, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/19886', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 3587, 'ano': 2000, 'ementa': 'Dispõe sobre aerolevantamento e levantamento espacial no território nacional, e dá outras providências.'}, {'id': 20718, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/20718', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 4186, 'ano': 1998, 'ementa': 'Modifica a Lei nº 9.612, de 19 de fevereiro de 1998, que "Institui o Serviço de Radiodifusão Comunitária e dá outras providências".'}, {'id': 20888, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/20888', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 4445, 'ano': 1998, 'ementa': 'Revoga a Lei nº 7.960, de 1989 que dispõe sobre prisão temporária.'}, {'id': 20956, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/20956', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 4550, 'ano': 1998, 'ementa': 'Altera o art. 389 do Decreto-Lei nº 5.452, de 1º de maio de 1943 (Consolidação das Leis do Trabalho - CLT).'}, {'id': 336532, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/336532', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 7576, 'ano': 2006, 'ementa': 'Altera a Lei nº 9.250, de 26 de dezembro de 1995, que altera a legislação do imposto de renda das pessoas físicas e dá outras providências, para fixar prazo e encargos financeiros relativos ao valor a restituir do imposto de renda das pessoas físicas pago a maior.'}, {'id': 339301, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/339301', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 7700, 'ano': 2006, 'ementa': 'Altera o art. 2º da Lei nº 11.096, de 13 de janeiro de 2005, para estender o atendimento do Programa Universidade para Todos aos estudantes beneficiados com bolsa parcial no ensino médio privado.'}, {'id': 340144, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/340144', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 64, 'ano': 2007, 'ementa': 'Cria o Índice Nacional de Responsabilidade Social - INRS e o Cadastro Nacional de Inadimplentes Sociais - CNIS.'}, {'id': 345103, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/345103', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 478, 'ano': 2007, 'ementa': 'Dispõe sobre o Estatuto do Nascituro e dá outras providências.'}, {'id': 359891, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/359891', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 1609, 'ano': 2007, 'ementa': 'Dispõe sobre a substituição gradativa, em todo o território nacional, de combustíveis derivados de petróleo por outros produzidos a partir da biomassa, e dá outras providências.'}, {'id': 363834, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/363834', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 1836, 'ano': 2007, 'ementa': 'Altera o § 1º do art. 19-I da Lei nº 8.080, de 19 de setembro de 1990, incluído pela Lei nº 10.424, de 15 de abril de 2002, para acrescentar ao Sistema Único de Saúde - SUS o fornecimento de medicamentos de uso continuado não sujeitos a controle especial, entre outros, necessários ao cuidado integral dos pacientes em seu domicílio.'}, {'id': 404399, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/404399', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 3723, 'ano': 2008, 'ementa': 'Dispõe sobre o tratamento tributário aplicável às sociedades cooperativas em geral no âmbito federal.'}, {'id': 415684, 'uri': 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/415684', 'siglaTipo': 'PL', 'codTipo': 139, 'numero': 4294, 'ano': 2008, 'ementa': 'Acrescenta parágrafo ao art. 1.632 da Lei nº 10.406, de 10 de janeiro de 2002 -  Código Civil e ao art. 3° da Lei nº 10.741, de 1ª de outubro de 2003 - Estatuto do Idoso,  de modo a estabelecer a indenização por dano moral em razão do abandono afetivo.'}]

# Criação do dataframe

pframe = pd.DataFrame.from_dict(pdata)
pframe

# PARTE 3
# Geração do código MD5 - um exemplo

import hashlib

id_15419 = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/15419'
phash = id_15419

phash = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes/15419'.encode()
print('MD5:', hashlib.md5(phash).hexdigest())

# PARTE 4
# Exportação do dataframe e armazenamento

pframe.to_csv('D:\pidsg\Documentos\GitHub\data-projects\CDBot-Project\proposicoes.csv')