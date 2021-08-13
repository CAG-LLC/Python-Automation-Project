import requests
from bs4 import BeautifulSoup
import time
import smtplib
from twilio.rest import Client
home_url = "https://jobs.cokecanada.com/search/?q=&q2=&alertId=&locationsearch=&title=&location=&date="

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def locate_find():

    ti = time.gmtime()
    page1 = requests.get(home_url, headers=headers)
    soup = BeautifulSoup(page1.content, "lxml")

    date = [td_date.span.string for td_date in soup.find_all('td', class_='colDate hidden-phone')]
    date1 = date[0]

    year = int(date1[7:11])

    month = date1[3:6]

    day = int(date1[0:2])

    month_mapping = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10,

                      'nov': 11, 'dec': 12}
    for key, value in month_mapping.items():
         if key == month.lower():
             num_mnth = int(value)





    td_location = soup.find_all('td', class_='colLocation hidden-phone')

    for td_location in td_location:
        locat = td_location.span.string


        if 'Sydney'.lower() in locat.lower() and day == ti[2]:
            send_email()
            send_msg()








def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # command sent by email server to identify  itself when connecting to another email sever to start the process of sending email.
    server.starttls() # Encrypt our connection
    server.ehlo()

    server.login('','')

    subject = 'New Job Posted  at Coke Canada !'

    body = "Check the  Link https://jobs.cokecanada.com/search/?createNewAlert=false&q=&locationsearch=sydney"

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        '',
        '',
        msg
    )

    print('Hey Email has been sent!')
    server.quit()



def send_msg():
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Job at Coke Canada ',
        from_='+14156632892',
        to=''
    )

    print(message.sid)


while(True):

    locate_find()
    time.sleep(60*60*4)
