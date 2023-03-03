
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
		Data.append([video.get_attribute('title'),video.get_attribute('href')])



	df = pd.DataFrame(Data,columns=['Video','Link'])

	print('Successfully scraped trending videos links.')
	driver_trending.quit()

	return df
	



def ScrapComments(url) :
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(options=options)
	driver.get(url)

	comz = []
	comments = driver.find_element(By.ID,"comments")
	coms = comments.find_elements(By.XPATH,"//div[@id='comment-content']//yt-formatted-string[@id='content-text']")
	for a in coms :
		comz.append(a.text)

	return comz 



df = GetTrendingVideos()



