import smtplib
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client




def locate():
    try:
        driver = webdriver.Chrome()
        driver.get('https://myview.wd3.myworkdayjobs.com/en-US/loblaw_retail/jobs')

        time.sleep(5)
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        res = driver.execute_script("return document.documentElement.outerHTML")
        time.sleep(2)
        driver.quit()

        soup = BeautifulSoup(res, "lxml")

        loc = soup.find_all('span', class_ = "gwt-InlineLabel WF2F WE1F")


        for loc in loc:
            if 'sydney' in (loc.string).lower() or 'north' in (loc.string).lower()  and 'today' in loc.string.lower() :
                send_email()
                send_msg()

    except:
        print("Error in Location Block")

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('gags231290@gmail.com','rfmcjdnbchottjmx')

    subject = 'New Job Posted - Loblaw '

    body = "Check the  Link https://myview.wd3.myworkdayjobs.com/en-US/loblaw_retail/jobs"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'gags231290@gmail.com',
        'gags23deep@gmail.com',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()

def send_msg():
    account_sid = 'AC26b55fc8f5461f0ac69131ad2a00a18c'
    auth_token = '8eb7607f669985079ecd0a330ba9744b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Job at loblaw Company ',
        from_='+14156632892',
        to='+19022170188'
    )

    print(message.sid)

while(True):

    locate()
    time.sleep(60*60*5)