from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import time

starturl = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('/Users/pc/Downloads/chromedriver_win32')
browser.get(starturl)
time.sleep(10)

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    star_data = []
    soup = BeautifulSoup(browser.page_source,'html.parser')
    for thtag in soup.find_all('th',attrs = {'class','exoplanet'}):
        temp_list = []
        for index,trtag in enumerate(trtag):
            if(index == 0):
                temp_list.append(trtag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(trtag.contents[0])
                except:
                    temp_list.append('')
        
        star_data.append(temp_list)

    browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('Scrapper.csv','w')as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(star_data)

scrape()