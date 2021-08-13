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
    account_sid = 'thyhrtyrtey45654363456456456'
    auth_token = 'yhtyrtyrtyrty565465'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="New room posting, Please check.",
        from_='+15156546546',
        to='+1456456456546'
    )

   # print(message.sid)




while (True):


    find_home()
    time.sleep(60*60*4)
