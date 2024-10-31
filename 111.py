from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from time import sleep

with open("output.txt", 'r') as file:
    # Read the contents of the file and convert it to an integer
    file_contents = file.read().strip()
    start_page = int(file_contents)

print(start_page)

driver = webdriver.Chrome()
# driver.maximize_window()

while True:
    url = f"https://privatekeyfinder.io/private-keys/bitcoin/{start_page}"
    driver.get(url)
    sleep(1)
    while True:
        try:
            total_balance_parent = driver.find_element(By.CSS_SELECTOR, "span[id=\"total-balance\"]")
            total_balance = total_balance_parent.find_element(By.TAG_NAME, 'span')
            if "Total balance" in total_balance.text:
                break
        except:
            pass
        sleep(0.1)
    if total_balance.text != "Total balance 0":
        print(total_balance.text)
        with open("data.txt", 'w') as file:
            file.write(driver.current_url)
        
            
    start_page += 1
    with open("output.txt", 'w') as file:
        file.write(str(start_page))
