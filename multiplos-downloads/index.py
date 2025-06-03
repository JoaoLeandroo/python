import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Caminho onde os arquivos serão salvos
download_dir = r"C:\caminho\para\downloads"  # altere para a sua pasta

# Configurações do Chrome
options = Options()
options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.default_directory": download_dir,
    "safebrowsing.enabled": True
})

driver = webdriver.Chrome(options=options)
driver.get("link_site")

# Espera o carregamento dos elementos
time.sleep(5)

# Coleta todos os links com '_RS.zip'
links = driver.find_elements("xpath", "//a[contains(@href, 'RS.zip')]")

# Clica em cada link para baixar
for link in links:
    try:
        link.click()
        time.sleep(1)  # Dá tempo para iniciar o download
    except:
        print("Erro ao clicar em link")

print(f"Iniciados {len(links)} downloads. Aguardando conclusão...")

# Espera até que todos os arquivos .crdownload desapareçam
def downloads_em_andamento():
    return any(filename.endswith(".crdownload") for filename in os.listdir(download_dir))

# Aguarda até que todos os downloads terminem ou tempo limite (10 minutos)
timeout = time.time() + 60 * 10  # 10 minutos
while downloads_em_andamento():
    if time.time() > timeout:
        print("Tempo limite atingido. Alguns downloads podem não ter terminado.")
        break
    time.sleep(2)

print("Todos os downloads concluídos.")
# driver.quit()  # Feche manualmente se quiser, ou descomente esta linha
