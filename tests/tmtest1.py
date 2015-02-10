# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://192.168.4.171:8080/ticket-monster/#about")
    if not ("TicketMonster is an online ticketing demo application that gets you started with JBoss technologies, and helps you learn and evaluate them." in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_xpath("//div[@class='hero-unit']/p[5]").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
