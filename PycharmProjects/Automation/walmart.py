import requests
from bs4 import BeautifulSoup
import time
import smtplib
from twilio.rest import Client

home_url = "https://ca.indeed.com/jobs?q=Walmart+Canada&l=Nova+Scotia&fromage=last&radius=25&sort=date"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page1 = requests.get(home_url, headers=headers)

soup = BeautifulSoup(page1.content, "lxml")

def locate_find():


    location =[loc.string for loc in soup.find_all('span', class_ = 'location accessible-contrast-color-location')]



    date = [dt.string for dt  in soup.find_all('span', class_='date')]


    for i in range(len(location)):
       if 'Sydney'.lower() in location[i].lower() and 'Today'.lower() in date[i].lower():
           send_email()
           send_msg()



def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('dfdfdfdf@gmail.com','fgfgfgfgfdnbchottjmx')

    subject = 'New Job Posted - Walmart '

    body = "Check the  Link https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=25222&siteid=5011#home"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'dfdfdsfdsfd@gmail.com',
        'sdfdfsdfds@gmail.com',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()

def send_msg():
    account_sid = 'dfdfdf1f0ac69131ad2a00a18c'
    auth_token = 'dfdfdsfdfdfda330ba9744b'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Job at walmart ',
        from_='+14743632892',
        to='+134343170188'
    )

    print(message.sid)


while(True):

    locate_find()
    time.sleep(60*60*3)
