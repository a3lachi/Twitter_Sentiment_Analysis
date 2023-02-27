
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading
import os 


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

    twlinks = []


    bol = True
    i = 1
    while (bol) :
        try :
            trend = trends_list.find_element_by_xpath("./li["+str(i)+"]")
            twlinks.append([str(trend.find_element_by_xpath("./a").get_attribute('href')) , trend.get_attribute('title')])
            i+=1
        except : 
            bol = False 

    driver_trends.quit()

    print('Trending tweets urls scraped with success.')
    return twlinks



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

def Write_Data(Folder, Data , trend) :
    Dir = os.listdir('data')
    if Folder not in Dir :
        os.mkdir('./data/'+Folder)
    f = open("./data/"+Folder+"/trend_"+trend[1]+".txt","a+")
    f.write(Data)
    f.close()


def Scrap_Trend() :
    trend = Handle()
    global Swipe 
    options = Options()
    global Headless
    global Folder 
    if Headless == True :
        options.headless = True
    driver_tw = webdriver.Firefox(options=options)
    while len(trend)>0 : 
        driver_tw.get(trend[0])
        time.sleep(3)
        Consent_Button(driver_tw)

        tweets = driver_tw.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div")

        tws_list = ""
        i = 1
        j=1
        while (j<Swipe) :
            Consent_Button(driver_tw)
            
            try :
                tweetat = tweets.find_elements_by_xpath("./div")
                for tweet in tweetat : 
                    tws_list += tweet.text + "\n------------------------------\n"
                driver_tw.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                time.sleep(3)
                j+=1
            except :
                pass
                
        
        Write_Data(Folder, tws_list , trend)

        print("Finished scraping trend : " + trend[1] )

        trend = Handle()
    
    driver_tw.close()


def Start_Threads(numb,Hdls,Swp,Fldr,NumbTrends) :
    global Headless
    Headless = Hdls

    global Swipe 
    Swipe = Swp 

    global Folder 
    Folder = Fldr

    threads = []
    global tw_links
    tw_links = Get_Tw_Links() 
    tw_links = tw_links[:NumbTrends]
    for i in range(numb):
        t = threading.Thread(target=Scrap_Trend)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(' Tweets scraped with success.')



