import pyautogui
import time
from urllib.parse import urlparse, urljoin, urlsplit

pyautogui.PAUSE = 1

pyautogui.FAILSAFE = True


def take_screenshot_in_default_browser(url):
    pyautogui.hotkey("win", "r")
    parsed_url = urlparse(url)
    getname = parsed_url.path.split("/")[-1]
    print(getname)

    if getname == "":
        getname = "Homepage"

    time.sleep(2)
    pyautogui.typewrite(url + " \n")

    time.sleep(10)
    pyautogui.click(1800, 100)
    time.sleep(1)

    for i in range(6):
        pyautogui.screenshot("IE_screenshot_" + getname + "_" + str(i) + ".png")
        pyautogui.scroll(-500)
        time.sleep(1)

    time.sleep(2)
    pyautogui.click(1904, 10)
    time.sleep(1)
    pyautogui.typewrite("enter")
    print("done")


if __name__ == '__main__':
    urls = ["https://www.sunlifeglobalinvestments.com/Slgi/Prices+and+Performance?vgnLocale=en_CA",
            "https://www.sunlifeglobalinvestments.com/"]
    for url in urls:
        take_screenshot_in_default_browser(url)
