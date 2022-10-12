

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#  Selenium custom exception that gets raised when an element cannot be found
from selenium.common.exceptions import NoSuchElementException


# ZEUT_NUMBER = "311874481"
# YEAR_OF_BIRTH='1986'
# PHONE_NUMBER= '0548367811'

ZEUT_NUMBER = "032684177"
YEAR_OF_BIRTH='1986'
PHONE_NUMBER= '0544343835'

zeut_number = ZEUT_NUMBER
year_of_birth = YEAR_OF_BIRTH
phone_number=PHONE_NUMBER


chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


URL = 'https://e-services.clalit.co.il/onlinewebquick/he-il/quicklogin'
driver.get(URL)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entrance page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
id_number = driver.find_element("name", "InputModel.UserId")
id_number.send_keys(zeut_number)

birth_year = driver.find_element("id", "InputModel_BirthYear")
birth_year.send_keys(year_of_birth)

sing_in_button = driver.find_element("id", "LoginBtn").click()
#sing_in_button.click()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Second page~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# service_choice
driver.find_element("xpath", '//*[@id="ddlRequestType"]/option[2]').click()


time.sleep(2)

# in this version, it's only possible to order recipes for 4 month for easier client usage
month_of_pills = driver.find_element("css selector", "#NumberOfMonths")
month_of_pills.send_keys("4")
month_of_pills.click()

inserted_phone_number_code=driver.find_element("css selector", '#HomePhoneCode')
inserted_phone_number_code.send_keys(phone_number[0:3])
inserted_phone_number_code.click()

phone_number_body=driver.find_element("css selector", "#HomePhoneNumber")
phone_number_body.send_keys(phone_number[3:])
phone_number_body.click()

# send_request
driver.find_element("css selector","#btnSendRequest").click()

time.sleep(60)
driver.quit()