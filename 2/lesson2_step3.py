from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/selects1.html")
    

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    num3 = int(num1.text)+int(num2.text)

    browser.find_element_by_id('dropdown').click()
    browser.find_element_by_css_selector(f'[value="{str(num3)}"]').click()




    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()