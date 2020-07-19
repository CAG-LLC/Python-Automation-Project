import requests
from bs4 import BeautifulSoup

main_url = "https://codingbat.com/python"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

page1 = requests.get(main_url, headers=headers)

soup = BeautifulSoup(page1.content, "lxml")

base_url ='https://codingbat.com'

all_div = soup.find_all('div', class_= "summ")

all_links  = [base_url + div.a['href']for div in all_div]




for link in all_links:
    inner_page= requests.get(link, headers=headers)
    inner_soup = BeautifulSoup(inner_page.content, "lxml")
    page31_links=[base_url + div.a['href']for div in inner_soup.find_all('td', width='200')]

    div =  inner_soup.find('div', class_='tabc')
    page3_links=[base_url + td.a['href']for td in div.table.find_all('td')]









    for link1 in page31_links:
        final_page = requests.get(link1, headers=headers)
        final_soup = BeautifulSoup(final_page.content, "lxml")
        final_content = final_soup.find('div', class_= 'indent')
        problem_statement = final_content.table.div.string
        print(problem_statement)

