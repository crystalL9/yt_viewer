from os import path
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
import watch_video
import threading
from module_tool import get_folder_profile_path,delete_profile
from queue import Queue
import random
import shutil
from ChromeDriver import ChromeDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
    
url_login='https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=en&ifkv=ASKXGp1CQs07hBbsyRMnV2oIiVHDcda6UtL7QSmncDc6WMVqW2oUs4VY8bsy1MKCtG06x54yXX8Lig&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1476421625%3A1705496782910721&theme=glif'
queue_mail = Queue()
queue_profile = Queue()
queue_keyword = Queue()
lock = threading.Lock()
queue_proxy= Queue()
flag=1

def read_file_to_queue(file_path, queue):
    unique_values = set()

    with open(file_path, 'r') as file:
        for line in file:
            value = line.strip()
            if value not in unique_values:
                queue.put(value)
                unique_values.add(value)

    return queue.qsize()

def get_all_profile(folder_path,queue):
    subdirectories = next(os.walk(folder_path))[1]
    for i in subdirectories:
        queue.put(i)

def read_file_to_array(file_path):
    lines = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines

def create_profile_from_file(queue,use_proxy,queue_position):
        
        with lock:
            account = queue.get()
            proxy = queue_proxy.get()
            position=queue_position.get()
        username = account.split('|')[0]
        password = account.split('|')[1]
        recover_mail = account.split('|')[2]
        profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{str(username)}'
        if path.exists(profile_path):
            print(f"Profile {username} Exist !")
            time.sleep(3)
            pass
        else: 
            if use_proxy==1:
                
                driver = ChromeDriver.driver_with_proxy(profile_path=profile_path,proxy=proxy,position=position)
            else:
                driver = ChromeDriver.driver_no_proxy(profile_path=profile_path,position=position)
                proxy=None
            try:
                try:
                    login_=login(driver=driver,username=username,password=password)
                except:
                    with open('logs.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\nLỗi mail\n')
                        file.write("-------------------\n")
                        file.close
                    with open('mail_error.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\n')
                        file.close
                    driver.quit()
                    return 0
                time.sleep(5)
                current_url = driver.current_url
                if '//accounts.google.com/v3/signin/challenge/selection?' in current_url:
                        confirm_mail(driver=driver,recovery_mail=recover_mail) 
                time.sleep(10)
                current_url2 = driver.current_url
                if '//accounts.google.com' in current_url2:
                    with open('logs.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\nLỗi mail\n')
                        file.write("-------------------\n")
                        file.close
                    with open('mail_error.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\n')
                        file.close
                    driver.quit()
                else:
                    time.sleep(3)
                    driver.quit()
                    mail(profile_path,username,password,proxy)
            except Exception as e:
                    with open('logs.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\nLỗi mail\n')
                        file.write("-------------------\n")
                        file.close
                    with open('mail_error.txt', 'a',encoding='utf-8') as file:
                        file.write(f'{account}\n')
                        file.close
                    driver.quit()
            if not path.exists(profile_path):
                print(f"Create Profile Fail: {username}")

def mail(path,username,password,proxy):
    if proxy!=None:
        duong_dan1 = os.path.join(path, "proxy.txt")
        with open(duong_dan1, "w") as file:
            file.write(f"{proxy}\n")
            file.close()
    duong_dan = os.path.join(path, "login.txt")
    with open(duong_dan, "w") as file:
        file.write(f"{username}|{password}\n")
        file.close()

def check_live_profile(path):
    for thu_muc in os.listdir(path):
        duong_dan_thu_muc = os.path.join(path, thu_muc)
        if os.path.isdir(duong_dan_thu_muc):
            duong_dan_tep_tin = os.path.join(duong_dan_thu_muc, "login.txt")
            if not os.path.exists(duong_dan_tep_tin):
                try:
                    shutil.rmtree(duong_dan_tep_tin)
                    print(f"Đã xóa thư mục: {duong_dan_thu_muc}")
                except OSError as e:
                    print(f"Lỗi xóa thư mục: {e}")

def confirm_mail(driver,recovery_mail):
    # Wait for the li element to be present in the DOM
        li_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(@class, 'JDAKTe') and contains(@class, 'cd29Sd') and contains(@class, 'zpCp3') and contains(@class, 'SmR8')][2]")
            )
        )
        li_elements.click()

        # Wait for the input element to be present in the DOM
        input_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'input[type="email"]')
            )
        )
        input_elements.send_keys(recovery_mail)

        # Wait for the button element to be present in the DOM
        button_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button')
            )
        )
        button_elements.click()

        # Add additional wait or actions if needed
        time.sleep(random.uniform(1, 5))

def login(driver,username,password):
        driver.get(url_login)
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
        )
        username_field.send_keys(username)
        username_next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button'))
        )
        username_next_button.click()
        time.sleep(5)
        
        password_field = None
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                password_field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'))
                )
                break
            except TimeoutException:
                attempts += 1
                print(" Không tìm thấy trường mật khẩu. Refresh lại trang...")
                driver.refresh()
        
        if password_field:
            time.sleep(5)
            password_field.send_keys(password)
            password_next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="passwordNext"]/div/button'))
            )
            password_next_button.click()
            time.sleep(5)
        else:
            print(" Cố gắng đăng nhập thất bại")
        return driver.current_url
        

def manager_profiles_watch_search(queue,keywords,start_time,end_time,queue_position):
    with lock:
            profile_name = queue.get()
            proxy=queue_proxy.get()
            position=queue_position.get()
    link_keywords=keywords
    random.shuffle(link_keywords)
    proxy=check_proxy_in_profile(profile_path)
    if proxy!=None:
        use_proxy=1
    else:
        use_proxy=0
    while len(link_keywords) > 0:
        if start_time>end_time:
            print ("Lỗi thời gian xem")
            break
        else:
            
            profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
            if path.exists(profile_path):
                if use_proxy==1:
                
                    driver = ChromeDriver.driver_with_proxy(profile_path=profile_path,proxy=proxy,position=position)
                else:
                    driver = ChromeDriver.driver_no_proxy(profile_path=profile_path,position=position)
                random_link= random.sample(link_keywords, random.randint(min(6,len(link_keywords)), min(8, len(link_keywords))))
                watch_video.watch_random(driver=driver,quantity=1)
                for _ in random_link :
                    try:
                        watch_video.watch_first(driver=driver,keywords=[_],start_time=start_time,end_time=end_time)
                        
                    except Exception as e:
                        print(e)
                        pass
                    link_keywords.remove(_)    
                driver.quit()
def check_proxy_in_profile(folder_path):
    proxy=None
    file_path = os.path.join(folder_path, "proxy.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            proxy = file.read()
    return proxy
def check_delete_in_profile(folder_path):
    file_path = os.path.join(folder_path, "delete.txt")
    if os.path.exists(file_path):
        return True
    else:
         return False
def manager_profiles_watch_link(queue,links,start_time,end_time,queue_position):
    with lock:
            profile_name = queue.get()
            position = queue_position.get()
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    proxy=check_proxy_in_profile(profile_path)
    if proxy!=None:
        use_proxy=1
    else:
        use_proxy=0
    link_keywords=links
    random.shuffle(link_keywords)
    while len(link_keywords) > 0:
        if start_time>end_time:
            print ("Lỗi thời gian xem")
            break
        else:
            random_link= random.sample(link_keywords, random.randint(min(6,len(link_keywords)), min(8, len(link_keywords))))
            if path.exists(profile_path):
                if use_proxy==1:
                
                    driver = ChromeDriver.driver_with_proxy(profile_path=profile_path,proxy=proxy,position=position)
                else:
                    driver = ChromeDriver.driver_no_proxy(profile_path=profile_path,position=position)
                watch_video.watch_random(driver=driver,quantity=1)
                for i in random_link:
                    try:
                        watch_video.watch_with_duration(driver=driver,video_url=i,start_time=start_time,end_time=end_time)   
                    except Exception as e:
                        print(e)
                        pass
                    link_keywords.remove(i)
                driver.quit()
def manager_profiles_watch_short(queue,queue_position):
    try:
        with lock:
                profile_name = queue.get()
                position = queue_position.get()
        profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
        proxy=check_proxy_in_profile(profile_path)
        if proxy!=None:
            use_proxy=1
        else:
            use_proxy=0
        if path.exists(profile_path):
            if use_proxy==1:
            
                driver = ChromeDriver.driver_with_proxy(profile_path=profile_path,proxy=proxy,position=position)
            else:
                driver = ChromeDriver.driver_no_proxy(profile_path=profile_path,position=position)
            watch_video.watch_random(driver=driver,quantity=1)
            driver.quit()
    except:
        pass

def manager_profiles_delete_history(queue):
    with lock:
            profile_name = queue.get()
    profile_path = get_folder_profile_path() + '\\' + f'Profiles\\{profile_name}'
    proxy=check_proxy_in_profile(profile_path)
    check= check_delete_in_profile(profile_path)
    if proxy!=None:
        useproxy=1
    else:
        useproxy=0
    if path.exists(profile_path):
        if useproxy==1:
                driver= ChromeDriver.driver_with_proxy(profile_path=profile_path,proxy=proxy)
        else:
                driver = ChromeDriver.driver_no_proxy(profile_path=profile_path)
        delete_history(driver,check,profile_path)
        driver.quit()
def list_subdirectories(directory):
    subdirectories = next(os.walk(directory))[1]
    return subdirectories

def delete_history(driver,check,profile_path):
    driver.get('chrome://settings/clearBrowserData')
    perform_actions(driver, Keys.TAB * 5)
    perform_actions(driver, Keys.ENTER)
    perform_actions(driver, Keys.DOWN * 4)
    perform_actions(driver, Keys.TAB * 3)
    if check==True:
        perform_actions(driver, Keys.ENTER)
    else:
         pass
    perform_actions(driver, Keys.TAB * 5)
    perform_actions(driver, Keys.ENTER)
    duong_dan1 = os.path.join(profile_path, "delete.txt")
    with open(duong_dan1, "w") as file:
            file.write("deleted")
            file.close()
    time.sleep(2)
   # Keys.TAB * 2 + Keys.ENTER+ Keys.TAB * 6 + Keys.ENTER)
    driver.close() 
def perform_actions(driver, keys):
    actions = ActionChains(driver)
    actions.send_keys(keys)
    time.sleep(2)
    print('Performing Actions!')
    actions.perform()

def process_mail(queue, use_proxy, num_threads):
    threads = []
    queue_position = Queue()
    x=2000
    for i in range(num_threads):
         queue_position.put(f'--window-position={x},0"')
         x=x+100
    for _ in range(num_threads):
        thread = threading.Thread(target=create_profile_from_file, args=(queue,use_proxy,queue_position))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def all_profiles_action(path_profile,queue,mode,links,keywords,start_time,end_time,num_threads):
    get_all_profile(path_profile,queue)
    len_profile = queue.qsize()
    queue_position = Queue()
    x=2000
    for i in range(len_profile):
         queue_position.put(f'--window-position={x},0"')
         x=x+10
    
    while not queue.empty():
        flag=read_flag()
        if flag == 0 :
            break
        else:
            if num_threads > 0 :
                len_profile=min(queue.qsize(),num_threads)
            else:
                len_profile = queue.qsize()
            if mode==1:
                threads = []
                for _ in range(len_profile):
                    thread = threading.Thread(target=manager_profiles_watch_short, args=(queue,queue_position))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            if mode==2:
                threads = []
                for _ in range(len_profile):
                    thread = threading.Thread(target=manager_profiles_watch_search, args=(queue,keywords,start_time,end_time,queue_position))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            if mode==3:
                threads = []
                for _ in range(len_profile):
                    thread = threading.Thread(target=manager_profiles_watch_link, args=(queue,links,start_time,end_time,queue_position))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
            if mode==4:
                threads = []
                for _ in range(len_profile):
                    thread = threading.Thread(target=manager_profiles_delete_history, args=(queue,))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()
        
def open_file_with_notepad(file_path):
    try:
        # Sử dụng subprocess để mở tệp tin bằng Notepad
        subprocess.Popen(['notepad.exe', file_path], shell=True)
        pass
    except FileNotFoundError:
        print(f"Tệp tin '{file_path}' không tìm thấy.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}") 

def read_flag():
    try:
        with open('flag', 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        return f"không tìm thấy."
    except Exception as e:
        return f"Có lỗi xảy ra: {e}" 
def write_flag(txt):
    try:
        with open('flag', 'w') as file:
            file.write(txt)
            file.close()
    except FileNotFoundError:
        return f" không tìm thấy."
    except Exception as e:
        return f"Có lỗi xảy ra: {e}" 

def action_create(use_proxy,numthread):
    write_flag('1')
    path_mail='gmail.txt'
    path_profile="Profiles"
    path_proxy="proxy.txt"
    len_proxy=read_file_to_queue(file_path=path_proxy,queue=queue_proxy)
    len_mail=read_file_to_queue(file_path=path_mail,queue=queue_mail)
    min_value = min(queue_mail.qsize(),int(numthread))
    min_value2 = min(queue_mail.qsize(),int(numthread))
    while min_value>0:
        
        if use_proxy==0:
            process_mail(queue=queue_mail,use_proxy= use_proxy, num_threads=min_value)
            delete_profile(path_profile)
        if use_proxy==1:
                min2=min(len_proxy,min_value2)
                while min2>0:
                    
                    process_mail(queue=queue_mail,use_proxy= use_proxy, num_threads=min2)
                    read_file_to_queue(file_path=path_proxy,queue=queue_proxy)
                    min2=min2-min_value2
        min_value = min(queue_mail.qsize(), numthread)
        delete_profile(path_profile)
    delete_profile(path_profile)
    

def action_create_forerror(use_proxy,numthread):
    write_flag('1')
    path_mail='mail_error.txt'
    path_profile="Profiles"
    path_proxy="proxy.txt"
    len_proxy=read_file_to_queue(file_path=path_proxy,queue=queue_proxy)
    len_mail=read_file_to_queue(file_path=path_mail,queue=queue_mail)
    min_value = min(queue_mail.qsize(),int(numthread))
    min_value2 = min(queue_mail.qsize(),int(numthread))
    while min_value>0:
        
        if use_proxy==0:
            process_mail(queue=queue_mail,use_proxy= use_proxy, num_threads=min_value)
            delete_profile(path_profile)
        if use_proxy==1:
                min2=min(len_proxy,min_value2)
                while min2>0:
                    
                    process_mail(queue=queue_mail,use_proxy= use_proxy, num_threads=min2)
                    read_file_to_queue(file_path=path_proxy,queue=queue_proxy)
                    min2=min2-min_value2
        min_value = min(queue_mail.qsize(), numthread)
        delete_profile(path_profile)
    delete_profile(path_profile)

def action_watch_or_del(mode,start_time,end_time,num_threads):
    write_flag('1')
    path_mail='gmail.txt'
    path_profile="Profiles"
    path_proxy="proxy.txt"
    path_keyword="keyword.txt"
    path_link="link-video.txt"
    links = read_file_to_array(file_path=path_keyword)
    keywords = read_file_to_array(file_path=path_link)
    all_profiles_action(path_profile,queue_profile,mode=mode,links=links,keywords=keywords,start_time=start_time,end_time=end_time,num_threads=num_threads)
if __name__ == "__main__":
    action_create_forerror(numthread=2,use_proxy=1)