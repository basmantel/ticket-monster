
from selenium import webdriver

sauce_url = "http://jimleitch:3eb84966-ba07-4e0d-98a5-ed1d2f3e2ef8@ondemand.saucelabs.com:80/wd/hub"

desired_capabilities = {
    'platform': "Mac OS X 10.9",
    'browserName': "chrome",
    'version': "31",
}

driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=sauce_url)
driver.implicitly_wait(10)




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
