from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from twilio.rest import Client


def find_home():


        driver = webdriver.Chrome()
        driver.get('https://www.kijiji.ca/b-apartments-condos/halifax/c37l80010')

        time.sleep(5)
        driver.find_element_by_tag_name('html').send_keys(Keys.END)
        res = driver.execute_script("return document.documentElement.outerHTML")
        time.sleep(3)
        driver.quit()

        soup = BeautifulSoup(res, "lxml")

        dates = soup.find_all('span', class_ = "date-posted")

        for date in dates:
            if ('minutes' in (date.string).lower() or 'minute' in (date.string).lower()) and ('1' in (date.string).lower() or '2' in (date.string).lower()):
                send_msg()




def send_msg():
    account_sid = 'ACa6ec4b8a63b29665c9a0cdd01cdf18af'
    auth_token = 'ffdb25ba5f2089d81eecde4d0a5fdd91'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="New room posting, Please check.",
        from_='+15136665963',
        to='+19025930170'
    )

   # print(message.sid)




while (True):


    find_home()
    time.sleep(60*60*4)
