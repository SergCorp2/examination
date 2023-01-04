import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from config import login_standart_user, password_standart_user
#from selenium.webdriver.support.ui import WebDriverWait



@pytest.fixture()
def go_page():

    driver = webdriver.Chrome(executable_path='D:\Scillfactory\pythonProject10\chromedriver.exe')
    base_url = ' https://b2c.passport.rt.ru/'
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(7)
    yield

@pytest.fixture()
def go_autorised():

    driver = webdriver.Chrome(executable_path='D:\Scillfactory\pythonProject10\chromedriver.exe')
    base_url = ' https://b2c.passport.rt.ru/'
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(5)
    button_post = driver.find_element(By.ID, 't-btn-tab-mail')
    button_post.click()
    user_name = driver.find_element(By.ID, "username")
    user_name.send_keys(login_standart_user)
    print("input login")
    user_password = driver.find_element(By.ID, "password")
    user_password.send_keys(password_standart_user)
    print("input password")
    button_login = driver.find_element(By.XPATH, '//*[@id="kc-login"]')
    button_login.click()
    print("click login button")
    time.sleep(5)
    text_last_name = driver.find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div/h2/span[1]')
    value_last_name = text_last_name.text
    print(value_last_name)
    assert value_last_name == "Сергей"
    #time.sleep(5)
    yield
    driver.quit()