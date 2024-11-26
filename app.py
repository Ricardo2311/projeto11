from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
import random
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

produto = input('Digite o produto que quer pesquisar: ')


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']

    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'C:\\Users\\rgeba\\OneDrive\\Documentos\\CURSO DEV APRENDER\\selenium'

    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_settings_values.automatic_downloads": 1,
    })

    driver = uc.Chrome(options=chrome_options)
    return driver


driver = iniciar_driver()


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)


driver.get('https://www.americanas.com.br')
sleep(3)

campo_pesquisar_produto = driver.find_element(
    By.XPATH, "//input[@name='conteudo']")
sleep(1)
digitar_naturalmente(produto, campo_pesquisar_produto)

botao_pesquisar = driver.find_element(
    By.XPATH, "//button[@aria-label='pesquisar']")
sleep(1)
botao_pesquisar.click()

input('')
