from selenium import webdriver
from time import sleep

import pandas as pd

def contacts(filename):
    all_contacts = pd.read_csv(filename)
    all_contacts = all_contacts[["Name"]]
    finalContacts = dict()
    for index, row in all_contacts.iterrows():
        print(str(row['Name']))
        finalContacts[str(row['Name'])] = str(row['Name'])
    return finalContacts

finalContacts = contacts('./contacts.csv')
driver = webdriver.Chrome('chromedriver')
driver.get('https://web.whatsapp.com')
sleep(12)
contacts = dict()
for i in range(100):
    for key, value in finalContacts.items():
        pre_msg = "*TOPPER* "
        post_msg = "*\nI'm a bot created by our legend, *Rishabh Purohit*"
        input_box = driver.find_element_by_css_selector("input[type='text']")
        input_box.click()
        input_box.send_keys(key)
        sleep(1)
        userbox = driver.find_element_by_css_selector("span[title='"+ key+"']")
        userbox.click()
        inputbox = driver.find_element_by_css_selector("div[data-tab='1']")
        inputbox.click()
        inputbox.send_keys(pre_msg+post_msg)
        send_button = driver.find_element_by_css_selector("span[data-icon='send']")
        send_button.click()
        sleep(1)
