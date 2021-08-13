import requests
from bs4 import BeautifulSoup
import time
import smtplib
from twilio.rest import Client

home_url = "https://www.mynslc.com/en/About-NSLC/Careers/Career-Opportunities/Retail/Casual-Store-Clerk"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


def locate_find():
    page1 = requests.get(home_url, headers=headers)

    soup = BeautifulSoup(page1.content, "lxml")

    ul = soup.find('ul', style = 'list-style-type: disc;' )
    list_city = [li.string for li in ul.children]
    for i in range(5):
        list_city.remove('\n')




    for list in list_city:
        if (('mine' in list.lower()) == False ) and ('sydney'in list.lower()):
            send_email()
            send_msg()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('fgrgh456765@gmail.com','546547fghdfeh')

    subject = 'New Job Posted  at NSLC!'

    body = "Check the  Link https://www.mynslc.com/en/About-NSLC/Careers/Career-Opportunities/Retail/Casual-Store-Clerk"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'ujikuikuki@gmail.com',
        'bvbcvbxcvb@gmail.com',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()

def send_msg():
    account_sid = 'hghfthghrtyrtyertyteryre'
    auth_token = '4567456743fghefghfgh'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Job at NSLC ',
        from_='+14675675676',
        to='+14567676457'
    )

    print(message.sid)


while(True):

    locate_find()
    time.sleep(60*60*3)



