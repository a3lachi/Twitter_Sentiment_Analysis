
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 



options = Options()
options.headless = True

driver_trends = webdriver.Firefox(options=options)
driver_trends.get('https://trends24.in/united-states/')

try :
    driver_trends.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
except : 
    print('No CONSENT button.')


trends_list = driver_trends.find_element_by_class_name("trend-card__list")

tw_links = []

## iterate over trends
bol = True
i = 1
while (bol) :
    try :
        trend = trends_list.find_element_by_xpath("./li["+str(i)+"]")
        tw_links.append(str(trend.find_element_by_xpath("./a").get_attribute('href')))
        i+=1
    except : 
        bol = False 

driver_trends.quit()

print('Twitter links sample :')
for a in tw_links[:5] :
    print(a)








driver_tw = webdriver.Firefox()

driver_tw.get(a)

time.sleep(2)
## not now button on notifications popup 

def Consent_Button() :
    try :
        driver_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span").click()
    except : 
        print('No CONSENT button.')



tweets = driver_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div")

tws_list = []
i = 1
j=1
while (j<100) :
    Consent_Button()
    try :
        tweet = tweets.find_element_by_xpath("./div["+str(i)+"]")
        tws_list.append(tweet.text)
        j+=1
        i+=1
    except : 
        driver_tw.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        i=1
        
driver_tw.close()

        




