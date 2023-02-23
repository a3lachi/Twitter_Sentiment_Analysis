
from selenium import webdriver



dri=webdriver.Firefox()
dri.get('https://trends24.in/united-states/')

try :
    dri.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
except : 
    print('No CONSENT button.')


trends_list = dri.find_element_by_class_name("trend-card__list")

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



