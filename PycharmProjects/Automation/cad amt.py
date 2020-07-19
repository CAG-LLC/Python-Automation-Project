import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://www.xe.com/currencyconverter/convert/?Amount=1&From=CAD&To=INR')
res= driver.execute_script("return document.documentElement.outerHTML")
time.sleep(7)
driver.quit()

def check_price():


    soup = BeautifulSoup(res, "html.parser")
    div = soup.find('span', class_ = 'converterresult-toAmount')

    if float(div.text) < 52.5815:
        send_email()





def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('gags231290@gmail.com','rfmcjdnbchottjmx')

    subject = 'CAD PRICE HAS FALL! (div.text)'

    body = "Check the  Link https://www.xe.com/currencyconverter/convert/?Amount=1&From=CAD&To=INR"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'gags231290@gmail.com',
        'gags23deep@gmail.com',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()

while(True):

    check_price()
    time.sleep(60*60*3)