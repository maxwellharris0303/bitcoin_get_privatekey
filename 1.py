from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
from time import sleep
import requests

BOT_TOKEN = "6597001968:AAG3SQh2eYDVY0vyeoXE9FtYfec3tJEr9qg"
CHAT_ID = 6330172738
def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = { "chat_id": CHAT_ID, "text": msg }
    requests.get(url, params=params)

FILENAME = "data.txt"
def data_save(data):
    with open(FILENAME, "a") as file:
        file.write(data + "\n")
driver = webdriver.Chrome()
driver.maximize_window()

url = "https://privatekeyfinder.io/private-keys/bitcoin/667022349516659127880046210541421348548035081175201705646070865431666896757"

driver.get(url)
index = 0
while(True):
    try:
        index += 1
        print(index)
        driver.find_element(By.XPATH, '//*[@id="cache_data"]/div/div[2]/div/div/div[4]/div/div[3]').click()
        sleep(2)
        
        total_balance_parent = driver.find_element(By.CSS_SELECTOR, "span[id=\"total-balance\"]")
        total_balance = total_balance_parent.find_element(By.TAG_NAME, 'span')
        
        if total_balance.text != "Total balance 0":
            print(total_balance.text)
            data_save(driver.current_url)
            send_message("Success")
    except:
        sleep(10)
        try:
            driver.refresh()
        except:
            pass
        sleep(10)
        pass

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# browser = webdriver.Chrome(options=chrome_options)
# browser.maximize_window()
# run_bot(browser)