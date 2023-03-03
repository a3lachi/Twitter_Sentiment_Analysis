
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading
import os 
from selenium.webdriver.common.by import By
import pandas as pd





def GetTrendingVideos() :

	options = Options()
	options.headless = True
	driver_trending = webdriver.Firefox(options=options)

	driver_trending.get('https://www.youtube.com/feed/trending')

	videos = driver_trending.find_element(By.ID,"contents")

	vidz = videos.find_elements(By.XPATH,"//div[@id='contents']//div[@id='grid-container']//a[@id='video-title']")


	Data = []

	for video in vidz :
		Data.append([video.get_attribute('title'),video.get_attribute('href'),''])



	df = pd.DataFrame(Data,columns=['Video','Link','Comments'])

	print('Successfully scraped trending videos links.')
	driver_trending.quit()

	return df
	
def Handle() :
    global Yt_data
    try :
        video = Yt_data[0]
        Yt_data = Yt_data[1:]
    except :
        video = []
    return video 


def ScrapComments() :
	global Yt_data
	video = Handle()
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)

	while (video) :
		driver.get(video)

		comz = []
		comments = driver.find_element(By.ID,"comments")
		coms = comments.find_elements(By.XPATH,"//div[@id='comment-content']//yt-formatted-string[@id='content-text']")
		for a in coms :
			comz.append(a.text)

		## insert comz in df 

		video = Handle()





def ThreadYoutube(NumbVidz)
	threads = []
    global Yt_data 
    try :
        Yt_data = GetTrendingVideos()
        Yt_data = Yt_data[:NumbVidz]
        for i in range(numb):
            t = threading.Thread(target=Scrap_Trend)
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        print('Comments scraped with success.')
    except Exception as e :
        print('An error occured launching th threads.')
        print('The error says : ',e)



