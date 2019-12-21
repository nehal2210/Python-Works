l=[]
with open("put_list.txt","r") as f:
    content=f.read()
for i in content.split(","):
    if i.strip('"')!="#":
        l.append(i.strip('"'))

    
from selenium import webdriver
import time

for i in l:
    time.sleep(5)
    driver=webdriver.Chrome()
    driver.maximize_window()    
    driver.get("https://y2mate.com")
    
    driver.find_element_by_id("txt-url").send_keys(i)
    time.sleep(5)
    driver.find_element_by_xpath("//*[@id='btn-submit']").click()
    time.sleep(20)
    driver.find_element_by_xpath("//*[@id='mp4']/table/tbody/tr[2]/td[3]/a").click()
    time.sleep(15)
    driver.find_element_by_xpath("//*[@id='process-result']/div/a").click()
 #if your net speed is slow then increase this time in seconds
    time.sleep(200)
    driver.close()
  






