
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time 
import threading
import os 
from selenium.webdriver.common.by import By







options = Options()
##options.headless = True
driver_trending = webdriver.Firefox(options=options)

driver_trending.get('https://www.youtube.com/feed/trending')

videos = driver_trending.find_element(By.ID,"contents")

vidz = videos.find_element(By.XPATH,"//div[@id='contents']")