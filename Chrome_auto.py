# chrome driver exe should be in the same directory

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class ytbot:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://youtube.com") 
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys(name+'\n')
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys('\t\t\t\t\t\t\t\t\t\t\t\t\n')
        time.sleep(1)
        url=self.driver.current_url
        self.driver.get("https://ytmp3.cc/en13/")
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]").send_keys(url+'\n')
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]").click()
        time.sleep(1)
        self.driver.get("https://youtube.com")
n=int(input("No. of songs: "))
i=1
while i<=n:
    name=input("Enter song name you want to download: ")
    ytbot()
    i+=1

x=input()

