import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from config import login_standart_user, password_standart_user

driver = webdriver.Chrome(executable_path='/chromedriver.exe')
base_url = 'https://b2c.passport.rt.ru/'
driver.implicitly_wait(10)

# login_standart_user = "593179@mail.ru "
# password_standart_user = "PSB5fACjc@eXekq"


def test_autorised_bad_login():

    driver.get(base_url)
    driver.maximize_window()

    button_post = driver.find_element(By.ID, 't-btn-tab-mail').click()
    button_post = driver.find_element(By.ID, 'username').send_keys('qwerty')
    button_post = driver.find_element(By.ID, 'password').send_keys(password_standart_user)
    button_post = driver.find_element(By.ID, 'kc-login').click()

    time.sleep(5)

    text_worning = driver.find_element(By.ID, 'form-error-message')
    value_worning = text_worning.text
    print(value_worning)
    assert value_worning == "Неверный логин или пароль"
    driver.quit()
    print('негативный тест, неверный логин- успешно')

def test_autorised_zero_login_password():

    driver.get(base_url)
    driver.maximize_window()

    button_post = driver.find_element(By.ID, 't-btn-tab-mail').click()
    button_post = driver.find_element(By.ID, 'username').send_keys('')
    button_post = driver.find_element(By.ID, 'password').send_keys('')
    button_post = driver.find_element(By.ID, 'kc-login').click()

    time.sleep(5)

    text_worning = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    value_worning = text_worning.text
    print(value_worning)
    assert value_worning == "Введите адрес, указанный при регистрации"
    driver.quit()
    print('негативный тест, логин пароль пустые- успешно')



