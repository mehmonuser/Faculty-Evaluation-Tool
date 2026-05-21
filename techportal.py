from logging import setLogRecordFactory
from os import link, pipe
from string import capwords
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
browser_location = r"C:\Program Files\[Browser Folder]"
option.binary_location = browser_location

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\chromedriver.exe", chrome_options=option)

student_portal = "[student portal website]"
driver.get(student_portal)

main_window = driver.current_window_handle

#student number
student_num = driver.find_element_by_xpath("//*[@id=\"student_number\"]")
student_num.send_keys("student_number")

#password
password = driver.find_element_by_xpath("//*[@id=\"password\"]")
password.send_keys("password")

#submit
click = driver.find_element_by_xpath("//*[@id=\"body-login\"]/div[2]/form/input[3]")
click.click()

#course card
card = driver.find_element_by_xpath("//*[@id=\"TABLE_1\"]/tbody/tr/td[1]/ul[1]/li[3]/a").click()

#terms
# two methods to pick in dropdown menu
#1
element = driver.find_element_by_id("term")
term = Select(element)
term.select_by_index(3)

#school year and 2nd method
el = driver.find_element_by_name("school_year")
year = Select(el)
year.select_by_visible_text("year")

#submit in course card
sub = driver.find_element_by_xpath("//*[@id='TABLE_1']/tbody/tr/td[2]/form/span[3]/input").click()

#clicking for evaluation if needed
eval_link = driver.find_element_by_link_text("Click here").click()
print(driver.current_window_handle) # CDwindow-F9EC7C2DF88FCF3D30200A13362DC776 - parent window


#trial to using new window, id number nd password
driver.switch_to.window(driver.window_handles[1])
idnum = driver.find_element_by_xpath("/html/body/div/div/form/div[1]/input")
idnum.send_keys("student_number")

idpass = driver.find_element_by_name("password")
idpass.send_keys("password")
 #sign in button
sign = driver.find_element_by_xpath("/html/body/div/div/form/div[3]/div[2]/button").click()

#picking who to evaluate (change path depending on who to evaluate)
prof = "/html/body/div/div/div/section[2]/div/div[2]/div[1]/div[1]/div/div/p[3]/a" 
evaluation = driver.find_element_by_xpath(prof).click()

#for number rating 1648 to 1669

first_evaluation = driver.find_element_by_name("ratings_1648")
pick = Select(first_evaluation)
pick.select_by_visible_text("ABOVE AVERAGE")
 
x = 1649
for i in range(1649,1702):
    first_element = driver.find_element_by_name("ratings_" + str(x))
    pick = Select(first_element)
    pick.select_by_visible_text("AVERAGE")
    x += 1
    if x == 1662:
        sub_element = driver.find_element_by_name("ratings_1662")
        sub_pick = Select(sub_element)
        sub_pick.select_by_visible_text("ABOVE AVERAGE")
        continue

    if x == 1670:
        x = 1670
        for num in range(1670,1699):
            second_element = driver.find_element_by_name("ratings_" + str(x))
            second_pick = Select(second_element)
            second_pick.select_by_visible_text("AGREE")
            x += 1
            if x == 1699:
                x = 1699
                for num in range(1699,1702):
                    third_element = driver.find_element_by_name("ratings_" + str(x))
                    third_pick = Select(third_element)
                    third_pick.select_by_visible_text("3")
                    x += 1
            else:
                continue
    else:
        continue
print("YEEEHHEYYYYY!!!!1")

#NUMBERS to above average [1662]
