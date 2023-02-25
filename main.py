
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading


def Get_Tw_Links() :
	options = Options()
	options.headless = True
	driver_trends = webdriver.Firefox(options=options)
	driver_trends.get('https://trends24.in/united-states/')

	try :
		driver_trends.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]").click()
	except : 
		pass


	trends_list = driver_trends.find_element_by_class_name("trend-card__list")

	tw_links = []


	bol = True
	i = 1
	while (bol) :
		try :
			trend = trends_list.find_element_by_xpath("./li["+str(i)+"]")
			tw_links.append([str(trend.find_element_by_xpath("./a").get_attribute('href')) , trend.get_attribute('title')])
			i+=1
		except : 
			bol = False 

	driver_trends.quit()

	print('Twitter links sample :')
	for a in tw_links[10:15] :
		print(a)

	return tw_links



def Consent_Button(driver) :
    try :
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div/span/span").click()
    except : 
        pass

    try :
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]").click()
    except : 
        pass

def Handle() :
	global tw_links
	try :
		trend = tw_links[0]
		tw_links = tw_links[1:]
	except :
		trend = []
	return trend 



def Scrap_Trend() :
	trend = Handle()
	if len(trend)>0 : 
		options = Options()
		options.headless = True
		driver_tw = webdriver.Firefox(options=options)

		driver_tw.get(trend[0])
		time.sleep(2)

		tweets = driver_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div")

		tws_list = ""
		i = 1
		j=1
		while (j<100) :
		    Consent_Button(driver_tw)
		    try :
		        tweet = tweets.find_element_by_xpath("./div["+str(i)+"]")
		        tws_list += tweet.text + "\n------------------------------\n"
		        print(trend[1] + " __ " + str(j))
		        j+=1
		        i+=1
		    except : 
		        driver_tw.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		        time.sleep(2)
		        i=1

		driver_tw.close()

		f = open("trend_"+trend[1]+".txt","a+")
		f.write(tws_list)
		f.close()








tw_links = Get_Tw_Links() 

# Create a list to hold the threads
threads = []

# Create 5 threads, each one running the open_firefox function
for i in range(5):
    t = threading.Thread(target=Scrap_Trend)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()



