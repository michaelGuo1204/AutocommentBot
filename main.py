# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import json
import time




def getCitylist(driver):
    driver.get("view-source:https://map.variflight.com/dist/js/home/static_data/citiesinbyarea.js")
    #rawdata=driver.page_source
    rawdata = driver.find_element_by_tag_name('pre').text
    data=re.findall(r"airportCode:\"([A-Z]*)\"",rawdata)
    return data
def getExcel(data,driver):
    driver.get('https://map.variflight.com/stat')
    judge=True
    for city in data:
        wait = WebDriverWait(driver, timeout=10000)
        id_box = wait.until(EC.presence_of_element_located((By.ID, 'APT')))
        id_box.clear()
        id_box.send_keys(city+'\n')
        element = driver.find_element_by_xpath("//div[@class='cityFilterBox FilterBox']")
        driver.execute_script("arguments[0].style.visibility='hidden'", element)
        if judge:
            try:
                isCross = driver.find_element_by_xpath("//li[contains(text(), '经停')]")
                isCross.click()
            except NoSuchElementException:
                pass
            try:
                isDomestic = driver.find_element_by_xpath("//li[contains(text(), '跨境')]")
                isDomestic.click()
            except NoSuchElementException:
                pass
            judge=False
        find=wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '查询')]")))
        find.click()
        download = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), '导出Excel')]")))
        download.click()


        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager.showWhenStarting", False)
    profile.set_preference("browser.download.dir", "/home/bili/Downloads/Anne_Air")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

    driver = webdriver.Firefox(firefox_profile=profile)
    #driver=webdriver.Firefox()#executable_path='/usr/bin/firefox')
    citylist=getCitylist(driver)
    getExcel(citylist,driver)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
