from selenium.webdriver.chrome.options import Options
from selenium import webdriver as nopx
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from seleniumwire import webdriver
class ChromeDriver:
    def driver_no_proxy(profile_path,position):
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996")
        options.add_argument("--disable-application-cache")
        options.add_argument('--hide-crash-restore-bubble')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-logging')
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument('--lang=en')
        driver = nopx.Chrome(options=options,executable_path='chromedriver.exe')
        driver.set_window_size(800, 600)
        xy=position
        x=int(position.split('|')[0])
        y=int(position.split('|')[1])
        driver.set_window_position(x, y)
        driver.get('https://www.youtube.com/')
        return driver  
    

    def driver_with_proxy(profile_path,proxy,position):
        print("Proxy in Profile is ",proxy)
        proxy=proxy.replace('\n','')
        hostname = proxy.split(':')[0]
        port = proxy.split(':')[1]
        options = Options()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996")
        options.add_argument("--disable-application-cache")
        options.add_argument('--hide-crash-restore-bubble')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-logging')
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument('--lang=en')
        options.add_argument(position)
        try:
            proxy_username = proxy.split(':')[2]
            proxy_password = proxy.split(':')[3]
            proxy_options = {
                'proxy': {
                    'http': f'http://{proxy_username}:{proxy_password}@{hostname}:{port}',
                    'https': f'https://{proxy_username}:{proxy_password}@{hostname}:{port}',
                    'no_proxy': 'localhost,127.0.0.1',
                    'verify_ssl': False
                }
            }
        except: 
            proxy_username = None
            proxy_password = None
            proxy_options = {
                'proxy': {
                    'http': f'http://{hostname}:{port}',
                    'https': f'https://{hostname}:{port}',
                    'no_proxy': 'localhost,127.0.0.1',
                    'verify_ssl': False
                }
            }
        
        
        driver = webdriver.Chrome(seleniumwire_options=proxy_options, chrome_options=options,executable_path='chromedriver.exe')
        driver.set_window_size(800, 600)
        driver.set_window_position(10, 0)
        driver.get('https://www.youtube.com/')
        time.sleep(1)
        return driver