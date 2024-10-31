from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from time import sleep
import bot


def concurrent_run_bots(brower_count):
    # Set the number of browsers you want to start
    num_browsers = brower_count

    # Set the path to your ChromeDriver executable

    # Create a list to store the browser instances
    browsers = []

    # Start the browsers
    for _ in range(num_browsers):

        # Set up browser instance
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
        # browser = webdriver.Chrome()
        browser.maximize_window()

        # Append the browser instance to the list
        browsers.append(browser)


    def perform_task(browser):
        # Example task: Open a webpage in each browser
        bot.run_bot(browser)



    # Create a thread pool executor with the number of desired workers
    with ThreadPoolExecutor(max_workers=num_browsers) as executor:
        # Submit the tasks to the executor
        # while(True):
        executor.map(perform_task, browsers)

    # Close all browsers
    # for browser in browsers:
    #     browser.quit()
