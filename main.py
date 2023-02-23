
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True




dri_trends=webdriver.Firefox(options=options)
dri_trends.get('https://trends24.in/united-states/')

try :
    dri_trends.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
except : 
    print('No CONSENT button.')


trends_list = dri_trends.find_element_by_class_name("trend-card__list")

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

dri_trends.quit()


for a in tw_links :
    print(a)













## not now button on notifications popup 

try :
    dri_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span").click()
except : 
    print('No CONSENT button.')



tweets = dri_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div")

bol = True
i = 3
while (bol) :
    try :
        tweet = tweets.find_element_by_xpath("./div["+str(i)+"]")
        print(tweet.text)
        i+=1
    except : 
        dri_tw.execute_script("window.scrollTo(0,document.body.scrollHeight)")


