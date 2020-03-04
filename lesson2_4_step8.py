from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()


    valuex = browser.find_element_by_id("input_value")
    x = valuex.text


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)



    input1 = browser.find_element_by_id("answer")

    input1.send_keys(str(y))

    button = browser.find_element_by_id("solve")
    button.click()








finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()