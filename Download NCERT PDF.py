import time

from selenium import webdriver
#pause the test for few seconds using Time class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
user="306632454"
pw="PANDEY"


driver = webdriver.Edge("msedgedriver")
driver.maximize_window()



driver.get("https://ncert.nic.in/textbook.php")
select = Select(driver.find_element_by_xpath("/html/body/div[3]/div/div/div/center/table/tbody/tr/td/form/table/tbody/tr/td[2]/select[1]"))
select.select_by_visible_text('Class XII')

select = Select(driver.find_element_by_xpath("/html/body/div[3]/div/div/div/center/table/tbody/tr/td/form/table/tbody/tr/td[2]/select[2]"))
select.select_by_visible_text('Physics')

select = Select(driver.find_element_by_xpath("/html/body/div[3]/div/div/div/center/table/tbody/tr/td/form/table/tbody/tr/td[2]/select[3]"))
select.select_by_visible_text('Bhautiki-I')
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/center/table/tbody/tr/td/form/table/tbody/tr/td[2]/input").click()
time.sleep(3)

for it in range(2,9):
    print(f"over {it} Book")
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div/center/p/table[1]/tbody/tr/td[1]/div/table/tbody/tr["+str(it)+"]/td/table/tbody/tr/td[2]/a").send_keys(Keys.CONTROL+'t')
    

    
print("Ho hi gaya")
