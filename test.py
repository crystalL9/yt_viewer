from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996")

browser = webdriver.Chrome(executable_path='chromedriver.exe',options=chrome_options)

url = 'https://www.youtube.com/shorts/baw78sli9Q0'

browser.get(url)
time.sleep(1)
search_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//div[@class="mobile-topbar-header-content non-search-mode cbox"]/button[@aria-label="Search YouTube"]/c3-icon')))
search_button.click()
time.sleep(1)
search_field = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,'//input[@name="search"]')))
search_field.send_keys('programming is hard')
time.sleep(1)
#results = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,'//ul[@role="listbox"]/li[@role="presentation"]')))
time.sleep(1)
print('and now we perform the search, by sending Enter key')
search_field.send_keys(Keys.ENTER) 
thumbnail_img = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, '//img[contains(@class, "cover video-thumbnail-img yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded")]'))
)
thumbnail_img.click()
