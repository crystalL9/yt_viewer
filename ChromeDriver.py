from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from seleniumwire import webdriver
class ChromeDriver:
    def driver_no_proxy(profile_path,position):
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument(f"--user-data-dir={profile_path}")
        options.add_argument('--lang=en')
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument('--hide-crash-restore-bubble')
        options.add_argument(position)
        driver = webdriver.Chrome(options=options,executable_path='chromedriver_c.exe')
        driver.get('https://www.youtube.com/')
        return driver  
    

    def driver_with_proxy(profile_path,proxy,position):
        print("Proxy in Profile is ",proxy)
        proxy=proxy.replace('\n','')
        hostname = proxy.split(':')[0]
        port = proxy.split(':')[1]
        options = Options()
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-application-cache")
        options.add_argument('--hide-crash-restore-bubble')
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
        
        
        driver = webdriver.Chrome('chromedriver_c.exe',seleniumwire_options=proxy_options, chrome_options=options)
        driver.get('https://www.youtube.com/')
        time.sleep(1)
        return driver