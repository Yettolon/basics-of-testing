from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/execute_script.html")
    browser.execute_script("window.scrollBy(0, 100);")
    
    x = browser.find_element_by_id('input_value')
    
    s = str(calc(int(x.text)))
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(s))




    input3 = browser.find_element_by_id('robotCheckbox').click()

    input4 = browser.find_element_by_id('robotsRule').click()


    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()