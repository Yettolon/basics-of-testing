from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/alert_accept.html")

    
    x = browser.find_element_by_class_name('btn')
    
    x.click()
    
    
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)
    s = browser.find_element_by_id('input_value')
    xx = calc(int(s.text))
    ss = browser.find_element_by_id('answer').send_keys(str(xx))






    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()