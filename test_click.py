import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='/chromedriver.exe')
base_url = ' https://b2c.passport.rt.ru/'
driver.implicitly_wait(10)


def test_click_mail():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 't-btn-tab-mail')
    button_post.click()
    time.sleep(5)
    driver.quit()
    print('нажатие почта- успешно')

def test_click_login():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 't-btn-tab-login')
    button_post.click()
    time.sleep(5)
    driver.quit()
    print('нажатие логин- успешно')

def test_click_personal_account():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 't-btn-tab-ls')
    button_post.click()
    time.sleep(5)
    driver.quit()
    print('нажатие лицевой счет- успешно')

def test_click_checkbox():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.login-form__remember-forgot-con > label > span.rt-checkbox__shape.rt-checkbox__shape--circular.rt-checkbox__shape--orange > svg')
    button_post.click()
    time.sleep(5)
    driver.quit()
    print('нажатие checkbox запомнить меня- успешно')

def test_click_forgot_password():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'forgot_password')
    button_post.click()
    time.sleep(5)
    text_forgot_password = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    value_forgot_password = text_forgot_password.text
    print(value_forgot_password)
    assert value_forgot_password == "Восстановление пароля"
    driver.quit()
    print('переход на страницу восстановления пароля- успешно')

def test_click_registration():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.XPATH, '//*[@id="kc-register"]')
    button_post.click()
    time.sleep(5)
    text_registration = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    value_registration = text_registration.text
    print(value_registration)
    assert value_registration == "Регистрация"
    driver.quit()
    print('переход на страницу регистрация- успешно')

def test_click_enter():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'kc-login')
    button_post.click()
    time.sleep(5)
    text_worning = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
    value_worning = text_worning.text
    print(value_worning)
    assert value_worning == "Введите номер телефона"
    driver.quit()
    print('нажатие войти и предупреждение- успешно')

def test_click_user_agreement():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/a')
    button_post.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[1])
    driver.save_screenshot('user agreement.png')
    driver.quit()
    print('нажатие пользовательское соглашение- успешно')

def test_click_social_network_vk():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'oidc_vk')
    button_post.click()
    time.sleep(5)
    text_vk = driver.find_element(By.XPATH, '//*[@id="oauth_wrap_content"]/div[2]/div/b')
    value_vk = text_vk.text
    print(value_vk)
    assert value_vk == "ВКонтакте"
    driver.save_screenshot('VK.png')
    driver.quit()
    print('нажатие соц сети VK- успешно')

def test_click_social_network_mail():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'oidc_mail')
    button_post.click()
    time.sleep(5)
    text_mail = driver.find_element(By.XPATH, '//*[@id="wrp"]/div[1]/span')
    value_mail = text_mail.text
    print(value_mail)
    assert value_mail == "Мой Мир@Mail.Ru"
    driver.save_screenshot('Mail.png')
    driver.quit()
    print('нажатие соц сети Mail- успешно')

def test_click_social_network_ok():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'oidc_ok')
    button_post.click()
    time.sleep(5)
    text_ok = driver.find_element(By.XPATH, '//*[@id="widget-el"]/div[1]/div')
    value_ok = text_ok.text
    print(value_ok)
    assert value_ok == "Одноклассники"
    driver.save_screenshot('OK.png')
    driver.quit()
    print('нажатие соц сети одноклассники- успешно')

def test_click_social_google():
    driver.get(base_url)
    driver.maximize_window()
   # time.sleep(5)
    button_post = driver.find_element(By.ID, 'oidc_google')
    button_post.click()
    time.sleep(5)
    text_ok = driver.find_element(By.XPATH, '//*[@id="initialView"]/div[2]/div/div[1]/div/div[2]')
    value_ok = text_ok.text
    print(value_ok)
    assert value_ok == "Войдите в аккаунт Google"
    driver.save_screenshot('Google.png')
    driver.quit()
    print('нажатие google- успешно')

def test_click_social_yandex():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'oidc_ya')
    button_post.click()
    time.sleep(5)
    text_yn = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/h1/span')
    value_yn = text_yn.text
    print(value_yn)
    assert value_yn == "Войдите с Яндекс ID"
    driver.save_screenshot('YN.png')
    driver.quit()
    print('нажатие яндекс успешно')

def test_click_hiden_eye():
    driver.get(base_url)
    driver.maximize_window()
    #time.sleep(5)
    button_post = driver.find_element(By.ID, 'password')
    button_post.send_keys('qwerty')
    time.sleep(5)
    button_post = driver.find_element(By.CSS_SELECTOR, '#page-right > div > div > div > form > div.rt-input-container > div > div.rt-input__action > svg')
    button_post.click()
    time.sleep(5)
    driver.save_screenshot('EYE.png')
    driver.quit()
    print('нажатие показа пароля- успешно')





