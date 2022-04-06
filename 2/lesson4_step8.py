import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Firefox()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100')
    )
browser.find_element_by_class_name('btn').click()
browser.execute_script("window.scrollBy(0, 100);")
s =str(calc(int((browser.find_element_by_id('input_value')).text)))
browser.find_element_by_id('answer').send_keys(s)

browser.find_element_by_id('solve').click()
time.sleep(30)
browser.quit()