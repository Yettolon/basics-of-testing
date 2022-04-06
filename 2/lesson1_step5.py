from selenium import webdriver
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/math.html")


    input1 = browser.find_element_by_id('input_value')
    x = calc(input1.text)

    input2 = browser.find_element_by_id('answer')
    input2.send_keys(x)
    input3 = browser.find_element_by_css_selector('[for="robotCheckbox"]').click()

    input4 = browser.find_element_by_css_selector('[for="robotsRule"]').click()


    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
