import csv
import time
from uuid import uuid1
from typing import List
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def make_csv(filename: str, data, new=True):
    """make a csv file with the given filename
    and enter the data
    """
    mode = 'w' if new else 'a'
    with open(filename, mode, newline='') as f:
        f.writelines(data)


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

with open('city&town.csv', 'r') as file:
    csvreader = csv.DictReader(file)
    make_csv('Scraping Data.csv','City,Title,Address,Website,Phone Number\n', new=True)
    for row in csvreader:
        print(row["City"])
        city = row["City"]
        driver.get(f"https://www.google.com/maps/search/Gym in {city} USA")
        time.sleep(3)
        # break


        condition = EC.presence_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "HlvSq", " " ))]'))
        condition_div = EC.presence_of_element_located((By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]'))
        while True:
            try:
             element_div = WebDriverWait(driver, 5).until(condition_div)
             hieght = driver.execute_script('return arguments[0].scrollHeight', element_div)
             driver.execute_script(f'arguments[0].scroll(0, {hieght})', element_div)
             element = WebDriverWait(driver, 5).until(condition)
             print("You've reached the end of the list.")
             break
            except:
                print("Expected condition not located. Retrying...")

                # element.click()

        time.sleep(2)

        FULL_BOX = '//*[contains(concat( " ", @class, " " ), concat( " ", "hfpxzc", " " ))]'
        BUSINESS_TITLE = '//h1[@class="DUwDvf fontHeadlineLarge"]/span[1]'
        ADDRESS = '//div[div/div/img/@src="//www.gstatic.com/images/icons/material/system_gm/1x/place_gm_blue_24dp.png"]'
        WEBSITE = '//div[div/div/img/@src="//www.gstatic.com/images/icons/material/system_gm/1x/public_gm_blue_24dp.png"]'
        PHONE_NUMBER = '//div[div/div/img/@src="//www.gstatic.com/images/icons/material/system_gm/1x/phone_gm_blue_24dp.png"]'
        SUB_CHILD = "//div[@class='m6QErb DxyBCb kA9KIf dS8AEf']"
        time.sleep(5)
        
        children = driver.find_elements(By.XPATH, FULL_BOX)
        for child in children[2:]:
            try:
                child.click()
                time.sleep(8)
                SUB = EC.presence_of_element_located((By.XPATH, SUB_CHILD))
                element_child = WebDriverWait(driver, 5).until(SUB)
                hieght = driver.execute_script('return arguments[0].scrollHeight', element_child)
                driver.execute_script(f'arguments[0].scroll(0, {hieght})', element_child)
                time.sleep(2)
               
    
                try:
                    condition = EC.presence_of_element_located((By.XPATH, BUSINESS_TITLE))
                    element = WebDriverWait(driver, 5).until(condition)
                    time.sleep(5)
                    url = (driver.current_url)
                    Title = element.text
                except:
                    Title = "N/A"
            

                try:    
                    condition = EC.presence_of_element_located((By.XPATH, ADDRESS))
                    element = WebDriverWait(driver, 5).until(condition)    
                    Address = element.text
                except:
                        Address = "N/A"
                

                try:
                    condition = EC.presence_of_element_located((By.XPATH, WEBSITE))
                    element = WebDriverWait(driver, 5).until(condition)    
                    Website = element.text
                except:
                        Website = "N/A"

                try:
                    condition = EC.presence_of_element_located((By.XPATH, PHONE_NUMBER))
                    element = WebDriverWait(driver, 5).until(condition)    
                    Number = element.text
                    make_csv('Scraping Data.csv',f'{city},"{Title}","{Address}","{Website}","{Number}"\n', new=False)
                except:
                    Number = "N/A"
            except:
                pass 