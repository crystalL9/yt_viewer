from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import random

# Xem video với thời gian đặt trước
def watch_with_duration(driver,video_url,start_time, end_time):
    try:
        driver.get(video_url)
        time.sleep(random.uniform(1, 3))
        video_element = driver.find_element(By.TAG_NAME,'video')
        is_video_playing = not video_element.get_attribute('paused')
        if is_video_playing:
            pass
        else:
            play_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ytp-play-button"))
        )
            play_button.click()
        time_watch=random.uniform(start_time, end_time)
        time.sleep(time_watch/2)
        scroll_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
        random_scroll_value = random.uniform(scroll_height/2, scroll_height)
        driver.execute_script(f"window.scrollTo(0, {random_scroll_value});")
        time.sleep(random.uniform(1, 10))
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(time_watch/2)
    except:
             pass
    
# xem video short random
def watch_random(driver,quantity):
    driver.get('https://www.youtube.com/shorts/')
    if quantity !=None:
        if quantity > 0 :
            for i in range(quantity):
                xpath = '//*[@id="shorts-player"]/div[5]/button'
                try:
                    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
                    element.click()
                except:
                     pass
                time.sleep(random.uniform(50, 60))
        

def excute_link(link):
        if '&' in link:
            link = link.split('&')[0]
        return link
# tìm kiếm video đầu tiên 
def watch_first(driver,keywords,start_time,end_time):
    for keyword in keywords:
        link_search=f"https://www.youtube.com/results?search_query={keyword}"
        driver.get(link_search)
        video_title_elements = driver.find_elements(By.XPATH, '//a[@id="video-title"]')
        for element in video_title_elements:
                    link = excute_link(element.get_attribute("href"))
                    watch_with_duration(driver,link,start_time,end_time)
                    break



if __name__ == "__main__":
    video_url = "https://youtu.be/0QePKDsizWk"
    watch_duration = 20 
    # watch_with_duration(video_url, watch_duration)
    #watch_random(3)
    start_time = 5
    end_time = 10

    watch_first("https://youtu.be/0QePKDsizWk",start_time=5,end_time=10)
