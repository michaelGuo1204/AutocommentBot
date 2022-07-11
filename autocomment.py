# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
import time

global usrname
username=  #Replace your usrname
global password
password = #Replace your password

def login(driver):
    options=FirefoxOptions()
    options.set_preference('devtools.jsonview.enabled', False)
    time.sleep(3)
    wait = WebDriverWait(driver, timeout=10000)
    id_box = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    #id_box=driver.find_element_by_name('username')
    id_box.send_keys(username)
    ps_box=driver.find_element_by_name('pwd')
    ps_box.send_keys(password)
    login_but=driver.find_element_by_id('account_login')
    login_but.click()
    return
def selectTask(driver):
    wait = WebDriverWait(driver, 100)
    prepare = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'logged-box')))
    portal=driver.find_element_by_link_text("班干部")
    portal.click()
    driver.get('view-source:https://nsa.xjtu.edu.cn/zftal-xgxt-web/bizFlow/dblist.zf?showCount=999')
    content = driver.page_source
    content = driver.find_element_by_tag_name('pre').text
    parsed_json = json.loads(content)
    return parsed_json

def workProcess(driver,task):
    for item in tasks['data']['rows']:
        formcode=item['FORMCODE']
        bizcode=item['BIZ_CODE']
        exeid=item['EXECUTIONID']
        taskid=item['TASKID']
        location='https://nsa.xjtu.edu.cn/sgyb/ybmjsckdetail/{}/{}/check/{}?taskId={}&curTab=db'.format(bizcode,formcode,exeid,taskid)
        driver.get(location)
        wait = WebDriverWait(driver, 1000000)
        prepare = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'el-textarea__inner')))
        prepare.send_keys("Good, keep moving")
        time.sleep(3)
        wait = WebDriverWait(driver, 1000000)
        confirmbut = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='el-button el-button--primary el-button--small']")))
        confirmbut.click()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver=webdriver.Firefox()#executable_path='/usr/bin/firefox')
    driver.get('https://nsa.xjtu.edu.cn')
    login(driver)
    tasks=selectTask(driver)
    workProcess(driver,tasks)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
