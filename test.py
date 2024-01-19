from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
chrome_options.add_argument("--window-position=2000,0")
driver = webdriver.Chrome(executable_path="chromedriver_c.exe",chrome_options=chrome_options)