from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Para usar wait
from selenium.webdriver.support import expected_conditions as EC


# Este script faz login numa conta wikipédia e realiza uma busca.
# Abre o arquivo para usar no Login.
file = open(r'C:\Users\Felipe\Documents\Senha_Wiki.txt', 'r')
l = file.readlines(); usuario = l.pop(0).strip(); senha = l.pop(0).strip()
pesquisa = input(f'{usuario} Digite o que deseja saber: ')

# Função para pesquisar.
def pesquisar(wait, pesquisa):
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchInput"]'))).send_keys(pesquisa)
    driver.find_element(By.XPATH, '//*[@id="searchButton"]').click()
    return None

#Driver e requisição.
driver = webdriver.Edge()
driver.get("https://en.wikipedia.org/wiki/List_of_HTTP_status_codes")
wait = WebDriverWait(driver, 7)

# Login.
driver.find_element(By.XPATH, '//*[@id="pt-login"]/a/span').click()
driver.find_element(By.XPATH, '//*[@id="wpName1"]').send_keys(usuario)
driver.find_element(By.XPATH, '//*[@id="wpPassword1"]').send_keys(senha)
driver.find_element(By.XPATH, '//*[@id="wpLoginAttempt"]').click()

# Pesquisa.
pesquisar(wait, pesquisa)
# Alerta de sucesso
driver.execute_script("alert('Estou vivo, embora seja apenas uma máquina.');")