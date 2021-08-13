import requests
from bs4 import BeautifulSoup
import time
import smtplib
from twilio.rest import Client
p=4
home_url = "https://jobs.sobeyscareers.com/search/?createNewAlert=false&q=&locationsearch=sydney%2CNova+Scotia%2C+Canada"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
def locate_find():
    global p

    page1 = requests.get(home_url, headers=headers)

    soup = BeautifulSoup(page1.content, "lxml")


    location = [div.span.string for div in soup.find_all('span', class_ = 'jobLocation visible-phone' )]

    #print(location)

    for loc in location:
        if 'sydney'.lower() in loc.lower():

            send_email()
            p=12





def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('sadfdsfasdfdsf@gmail.com','vcdfvdfgsdrfgfgsdfgfd')

    subject = 'New Job Posted  at  Sobeys!'

    body = "Check the  Link https://jobs.sobeyscareers.com/search/?createNewAlert=false&q=&locationsearch=sydney%2CNova+Scotia%2C+Canada"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'dfgsdatgfghfsd@gmail.com',
        'fgdfgdfgdfg@gmail.com',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()




while(True):

    locate_find()
    time.sleep(60*60*p)


