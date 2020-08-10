import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from twilio.rest import Client

result1= []
result2= []
driver = webdriver.Chrome()
driver.get('https://www.careers.staples.ca/search')
res= driver.execute_script("return document.documentElement.outerHTML")
time.sleep(7)
driver.quit()
ti = time.gmtime()

def locate_find():

    soup = BeautifulSoup(res, "html.parser")
    tbody= soup.tbody

    # Find Date
    td=tbody.tr.td


    for child in td.children:
           result1 .append (child if child is not None else ' ')

    day = (result1[2].text)

    # Find Location
    for child1 in tbody.tr.children:
        result2.append(child1 if child1 is not None else ' ')

    td_loc = result2[2]

    location = td_loc.span.span.text


    if "sydney".lower() in (location.replace(',','')).lower() and int(day[9:10]) == ti[2]:
        send_email()




def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('gags231290@gmail.com','rfmcjdnbchottjmx')

    subject = 'New Job Posted at Staple!'

    body = "Check the  Link https://www.careers.staples.ca/search"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'gags231290@gmail.com ',
        'gags23deep@gmail.com ',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()



while(True):

    locate_find()
    time.sleep(60*60*4)

















