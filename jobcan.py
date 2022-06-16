from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from webdriver_manager.firefox import GeckoDriverManager

import time
import os

import day

if day.is_holiday():
    pass
else:
    # webdriver managerでdriverをgithubからダウンロードするためのgithub個人トークン
    os.environ['GH_TOKEN'] = ""

    # webdriver取得時のsslエラーを回避するため
    os.environ['WDM_SSL_VERIFY'] = '0'

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get("https://id.jobcan.jp/users/sign_in")

    user_email = driver.find_element(by=By.ID, value="user_email")
    user_email.send_keys("")
    time.sleep(1)
    user_password = driver.find_element(by=By.ID, value="user_password")
    user_password.send_keys("")
    time.sleep(1)
    login_button = driver.find_element(by=By.ID, value="login_button")
    login_button.click()
    time.sleep(2)

    # class=jbc-app-linkの要素は2つあり、最初に見つかる方はdisplay:noneでクリックできないため
    # (ElementNotInteractableExceptionが発生する)2つ目の要素をクリック
    jbc_app_link = driver.find_elements(by=By.CLASS_NAME, value="jbc-app-link")[1]
    jbc_app_link.click()
    time.sleep(2)

    # 出勤ボタンのあるページは新しいタブで開かれるため
    driver.switch_to.window(driver.window_handles[1])
    adit_button_push = driver.find_element(by=By.ID, value="adit-button-push")
    adit_button_push.click()
    time.sleep(2)
    driver.quit()