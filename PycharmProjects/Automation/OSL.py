import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client

driver = webdriver.Chrome()
driver.get("https://canadaengcareers-oslrs.icims.com/jobs/search?ss=1&mobile=false&width=888&height=500&bga=true&needsRedirect=false&jan1offset=-240&jun1offset=-180")

time.sleep(5)
driver.find_element_by_tag_name('html').send_keys(Keys.END)
page_source_overview = driver.page_source
time.sleep(10)



soup = BeautifulSoup(  page_source_overview , "lxml")

div = soup.find_all("div",class_="container-fluid iCIMS_JobsTable")


print(div)
