import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://www.sunlifeglobalinvestments.com/"


def get_height(url):
    chrome_options = Options()
    # chrome_options.set_headless(True)
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    # pause 3 second to let page load
    time.sleep(3)
    # get scroll Height
    height = driver.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")
    print("Document height found: " + str(height))
    # close browser
    driver.close()


get_height(url)
print("done")
