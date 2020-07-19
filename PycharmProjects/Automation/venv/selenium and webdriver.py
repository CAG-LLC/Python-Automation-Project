from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup



driver = webdriver.Chrome()
driver.get('https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=25222&siteid=5011#home')



search_bar = driver.find_element_by_id('initialSearchBox__00Q')
search_bar.send_keys( 'sydney')

search_button1 = driver.find_element_by_id('searchControls_BUTTON_2')
search_button1.click()

driver.get('https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=25222&siteid=5011#keyWordSearch=sydney&locationSearch=')
soup =BeautifulSoup(driver.page_source, 'lxml')

print(soup.find_all('ul' ))

sleep(10)

driver.close()
