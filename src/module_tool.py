from os import makedirs , path , listdir , system
from shutil import rmtree
from pathlib import Path
import os

def create_profiles_folder(name_folder="Profiles"):
    if not path.exists(name_folder):
        makedirs(name_folder)

def delete_profile(folder_path):
    for folder_name in os.listdir(folder_path):
        current_folder = os.path.join(folder_path, folder_name)
        
        # Kiểm tra xem là thư mục không
        if os.path.isdir(current_folder):
            login_file_path = os.path.join(current_folder, 'login.txt')
            
            # Nếu không có file 'login.txt' trong thư mục, xóa thư mục đó
            if not os.path.exists(login_file_path):
                try:
                    rmtree(current_folder)
                except:
                    pass
def get_folder_profile_path():
    return str(Path.cwd())

def get_profiles():
    profiles = []
    profiles =  [profile_name for  profile_name  in listdir("Profiles") if not profile_name.endswith('.txt')]
    profile_count = len(profiles)
    print(f"Profiles:  {profile_count}")
    for x in profiles:
        profile_index = profiles.index(x)
        print(f"{profile_index + 1}: {x}")
    return profiles
def clear_chrome_process():
    try:
        system('taskkill /im chrome.exe')
    except:
        pass
    system('cls')
    

if __name__ == "__main__":
    get_profiles()

    