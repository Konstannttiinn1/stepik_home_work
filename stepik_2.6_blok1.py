from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(11)

    #price = browser.text_to_be_present_in_element(By.ID, 'price')
    #browser.text_to_be_present_in_element(By.ID, 'price')

    # Ожидание, пока цена дома не уменьшится до $100
    wait = WebDriverWait(browser, 12)
    price_div = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    #first_window = browser.window_handles[0]
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)
    #alert = browser.switch_to.alert
    #alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    y = x_element.text
    x = calc(y)
    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(x)

    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text)

    #button = browser.find_element(By.ID, "#solve")
    #button.click()


    """option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()"""


    """option3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    option3.click()"""



finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

