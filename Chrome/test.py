from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# add all URLs you want to visit here
urls = []
 
options = Options()
options.add_argument('--disable-notifications')
options.add_argument('--headless')
chrome = webdriver.Chrome(executable_path='Selenium/Chrome/chromedriver', chrome_options=options)

startTime = time.time()
for i in range(10):
  chrome.get(urls[i])
  try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(chrome, 3).until(element_present)
  except TimeoutException:
    continue
endTime = time.time()
print (endTime-startTime)
