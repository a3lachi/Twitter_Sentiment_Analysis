
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading
import os 
from selenium.webdriver.common.by import By
import pandas as pd





def GetTrendingVideos() :
	options = Options()
	##options.headless = True
	driver_trending = webdriver.Firefox(options=options)

	driver_trending.get('https://www.youtube.com/feed/trending')

	videos = driver_trending.find_element(By.ID,"contents")

	vidz = videos.find_elements(By.XPATH,"//div[@id='contents']//div[@id='grid-container']//a[@id='video-title']")



	Data = []

	for video in vidz :
		Data.append([video.get_attribute('title'),video.get_attribute('href')])






	df = pd.DataFrame(Data,columns=['Video','Link'])


	print(df.head(10))