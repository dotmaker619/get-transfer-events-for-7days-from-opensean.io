import gc
import time
import pandas as pd
from selenium import webdriver

url = "https://opensea.io/collection/boredapeyachtclub?tab=activity"
option = webdriver.ChromeOptions()
# option.add_argument("--headless")
option.add_argument("window-size=1200,800")

driver = webdriver.Chrome("chromedriver", options=option)
driver.get(url)
time.sleep(3)

H = 1280
h = 0

fields = ['Name', 'Amount', 'Timestamp']
data = []
flg = False

while True :
    if flg :
        break

    driver.execute_script("window.scrollTo({}, {});".format(0, H))
    time.sleep(3)

    for i in range(0, 8) :
        try :
            name = driver.find_elements_by_css_selector("div[style*='top: {height}px;'] div[class*='Overflowreact']".format(height=h))[1].text
            amount = driver.find_elements_by_css_selector("div[style*='top: {height}px;'] div[class*='Overflowreact']".format(height=h))[2].text
            timetmp = driver.find_element_by_css_selector("div[style*='top: {height}px;'] a.EventTimestamp--link".format(height=h)).text
            timestamp = timetmp.replace(" open_in_new", "")
            
            if "8 days" in timestamp :
                flg = True
                break

            data.append([name, amount, timestamp])
        except :
            pass

        h += 80
    
    H += 640
    
driver.close()

dataTable = pd.DataFrame(data, columns=fields)
dataTable.to_csv("result.csv")

# div[style^='top: 9120px;'] div[class^='Overflowreact']
# div[style^='top: 9120px;'] a.EventTimestamp--link
