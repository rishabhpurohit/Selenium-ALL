from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "type your roll no."
password = "type password"
driver = webdriver.Chrome()
driver.get("http://www.msftconnecttest.com/redirect")
element = driver.find_element_by_id("ft_un")
element.send_keys(user_name)
element = driver.find_element_by_id("ft_pd")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
