from selenium import webdriver
import time

import os


try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/file_input.html")
    
    
    x = browser.find_element_by_name('firstname')
    x.send_keys('First Name')
    x1 = browser.find_element_by_name('lastname')
    x1.send_keys('Last Name')
    x2 = browser.find_element_by_name('email')
    x2.send_keys('Email Name')

    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'sd.txt')
    file.send_keys(file_path)




    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()