from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

# add all URLs you want to visit here
urls = []
 
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless')
firefox = webdriver.Firefox(options=options, executable_path='Selenium/Firefox/geckodriver')

startTime = time.time()
for i in range urls:
  firefox.get(urls[i])
endTime = time.time()
print (endTime-startTime)
