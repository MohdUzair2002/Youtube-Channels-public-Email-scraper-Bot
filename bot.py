from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import re
chrome_options =webdriver.ChromeOptions()

##chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8000")
s=Service(ChromeDriverManager().install())
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# chrome_options.add_experimental_option('useAutomationExtension', False)
# chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=s,options=chrome_options)
url='https://www.youtube.com/results?search_query=plumber&sp=EgIQAg%253D%253D'
chrome.get(url)
wait=WebDriverWait(chrome, 60)
no_ofchannels=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='content-section']")))
no_ofchannels=chrome.find_elements(By.XPATH,"//div[@id='content-section']")
length=0
links=[]
email_found_descripton=[]
while (length <5):
 no_ofchannels=chrome.find_elements(By.XPATH,"//div[@id='content-section']")[0:2]
 chrome.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
 time.sleep(8)
#  length=len(no_ofchannels)
 length+=1
#  print(length)
linksextracted=chrome.find_elements(By.XPATH,"//a[@class='channel-link yt-simple-endpoint style-scope ytd-channel-renderer'][@id='main-link']")
print(linksextracted)
# time.sleep(500)
for link in linksextracted:
    href=link.get_attribute('href')
    print(href)
    links.append(href)
# if (length > 2):
#  del(linksextracted[2:])
print(links)
print(len(links))
j=0
while(j < 100):
 print(j+1)
 try:
    chrome.get(links[j])
    video_section=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='tab-content style-scope tp-yt-paper-tab']")))
    video_section=chrome.find_elements(By.XPATH,"//div[@class='tab-content style-scope tp-yt-paper-tab']")[1]
    chrome.execute_script("arguments[0].click();", video_section)
    video1=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='style-scope ytd-grid-video-renderer']//a")))
    video1=chrome.find_element(By.XPATH,"//div[@class='style-scope ytd-grid-video-renderer']//a")
    chrome.execute_script("arguments[0].click();", video1)#  chrome.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    #  show_more=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='style-scope ytd-expander']")))
    time.sleep(6)
    show_more=chrome.find_elements(By.XPATH,"//*[@class='style-scope ytd-expander']")[-1]
    chrome.execute_script("arguments[0].click();", show_more)
    #  description=wait.until((By.XPATH,"//*[@slot='content']/yt-formatted-string"))
    time.sleep(30)

    chrome.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    description=chrome.find_element(By.XPATH,"//*[@slot='content']/yt-formatted-string")
    #  print(description)

    description_text=description.text
    print(description_text)
    email_found=re.findall("\S+@\S+", description_text)
    print(email_found)
    if(len(email_found) > 0):
        email_found_descripton.append(1)
    else:
        email_found_descripton.append(0)
    #  time.sleep(500)
    j+=1
 except:
    chrome.get(links[j])
    video_section=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='tab-content style-scope tp-yt-paper-tab']")))
    video_section=chrome.find_elements(By.XPATH,"//div[@class='tab-content style-scope tp-yt-paper-tab']")[1]
    chrome.execute_script("arguments[0].click();", video_section)
    video1=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='style-scope ytd-grid-video-renderer']//a")))
    video1=chrome.find_element(By.XPATH,"//div[@class='style-scope ytd-grid-video-renderer']//a")
    chrome.execute_script("arguments[0].click();", video1)#  chrome.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    #  show_more=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@class='style-scope ytd-expander']")))
    time.sleep(6)
    show_more=chrome.find_elements(By.XPATH,"//*[@class='style-scope ytd-expander']")[-1]
    chrome.execute_script("arguments[0].click();", show_more)
    #  description=wait.until((By.XPATH,"//*[@slot='content']/yt-formatted-string"))
    time.sleep(30)

    chrome.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    description=chrome.find_element(By.XPATH,"//*[@slot='content']/yt-formatted-string")
    #  print(description)

    description_text=description.text
    print(description_text)
    email_found=re.findall("\S+@\S+", description_text)
    print(email_found)
    if(len(email_found) > 0):
        email_found_descripton.append(1)
    else:
        email_found_descripton.append(0)
    #  time.sleep(500)
    j+=1
# print(len(email_found_descripton))
sum1=sum(email_found_descripton)
percenatge=(sum1/2)*100
print(percenatge)

 

