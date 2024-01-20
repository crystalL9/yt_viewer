from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtCore import QResource
from datetime import datetime, timedelta
from PyQt6.QtCore import QResource, QThread, pyqtSignal
import pytz
from src.activate import *
from dateutil import parser
import requests
import json
from src import profiles
import subprocess
import sys
import threading
import os
import ctypes 
timezone = pytz.timezone('Asia/Ho_Chi_Minh')
time_activate = datetime(year=2024, month=1, day=21, hour=21, minute=45, tzinfo=timezone)

class WorkerThread(QThread):
    finished = pyqtSignal()  # Tín hiệu được phát khi luồng hoàn thành

    def __init__(self, target=None, args=()):
        super(WorkerThread, self).__init__()
        self.target = target
        self.args = args

    def run(self):
        # Thực hiện công việc trong luồng
        if self.target:
            self.target(*self.args)

        # Khi công việc hoàn thành, phát tín hiệu finished
        self.finished.emit()
def get_time_now():
    # if response.status_code == 200:
    #     data = json.loads(response.text)
    #     date_time = data['datetime']
    #     time_now  = datetime.fromisoformat(date_time)
    #     return date_time_with_timezone
    try:
        response = requests.get("https://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh")
        if response.status_code == 200:
            data = json.loads(response.text)
            date_time = data['datetime']
            time_now  = datetime.fromisoformat(date_time)
            return time_now
        else:
            response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Ho_Chi_Minh")
            if response.status_code == 200:
                data = json.loads(response.text)
                date_time = data['dateTime']
                time_now  = parser.isoparse(date_time)
                date_time_with_timezone = timezone.localize(time_now)
                return date_time_with_timezone
            else:
                return datetime.now(timezone)
    except Exception as e:
        print(e)
        try:
            response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Asia/Ho_Chi_Minh")
            if response.status_code == 200:
                data = json.loads(response.text)
                date_time = data['dateTime']
                time_now  = parser.isoparse(date_time)
                date_time_with_timezone = timezone.localize(time_now)
                return date_time_with_timezone
            else:
                return datetime.now(timezone)
        except Exception as e:
            print(e)    
            return datetime.now(timezone)

class Login_w(QMainWindow):
    def __init__(self):
        super(Login_w, self).__init__()
        loadUi('UI/login.ui', self)
        self.bt_login.clicked.connect(self.login)
    def login(self):
        user = self.username.text()
        psw = self.password.text()
        print(user, psw)
        if user == "1" and psw == "1":
            QMessageBox.information(self, "Login", "Login succsess")
            widget.setCurrentIndex(1)
            widget.setFixedHeight(600)
            widget.setFixedWidth(800)
        else:
            QMessageBox.information(self, "Login", "Login fail")
class YTB_main(QMainWindow):
    def __init__(self):
        super(YTB_main, self).__init__()
        loadUi('UI/UI_YTB.ui', self)
        self.bt_pause.clicked.connect(self.stop)
        self.bt_import_proxy.clicked.connect(self.input_proxy)
        self.bt_open_profiles.clicked.connect(self.open_folder)
        self.bt_import_mail.clicked.connect(self.input_mail)
        self.bt_login_mail.clicked.connect(self.create_profile)
        self.bt_mail_error.clicked.connect(self.mail_error)
        self.bt_remove_history.clicked.connect(self.delete_history)
        self.bt_mail_error.clicked.connect(self.mail_error)
        self.bt_import_link.clicked.connect(self.input_link)
        self.bt_import_key.clicked.connect(self.input_keyword)
        self.bt_running.clicked.connect(self.watch_video)
        self.bt_exit.clicked.connect(self.exit)
        self.bt_login_mail_error.clicked.connect(self.create_profile_error)
    def open_folder(self):
        try:
            if sys.platform == 'win32':
                subprocess.Popen(['explorer', 'Profiles'], shell=True)
            else:
                subprocess.Popen(['xdg-open', 'Profiles'])
        except Exception as e:
         print(f"Error: {e}")
    def stop(self):
        try:
            profiles.write_flag('0')
        except:
            pass
    def input_proxy(self):
        try:
            profiles.open_file_with_notepad('data/proxy.txt')
        except:
            pass
    def input_keyword(self):
        try:
            profiles.open_file_with_notepad('data/keyword.txt')
        except:
            pass
    def input_link(self):
        try:
            profiles.open_file_with_notepad('data/link-video.txt')
        except:
            pass
    def input_mail(self):
        try:
            profiles.open_file_with_notepad('data/gmail.txt')
        except:
            pass
    def mail_error(self):
        try:
            profiles.open_file_with_notepad('data\mail_error.txt')
        except:
            pass
    def delete_history(self):
        try:
            numthreads = self.spb_num_thread.value()
            # t= threading.Thread(target=profiles.action_watch_or_del, args=(4,10,20,numthreads))
            # t.setDaemon(True)
            # t.start()
            self.word_thread_delete = WorkerThread(target=profiles.action_watch_or_del, args=(4,10,20,numthreads))
            self.word_thread_delete.finished.connect(self.handle_thread_finished_delete)  # Kết nối tín hiệu finished với phương thức handle_thread_finished
            self.word_thread_delete.start()
            self.word_thread_view.wait()
        except:
            pass
    def exit(self):
        #sys.exit()
        profiles.stop_driver()
        QtCore.QCoreApplication.quit()
    def watch_video(self):
        numthreads = self.spb_num_thread.value()
        timedelay = self.spb_time_delay.value()
        startime= self.spb_time_view.value() - timedelay
        endtime= self.spb_time_view.value() + timedelay
        if self.rd_random_view_video.isChecked():
            if self.rd_search_video.isChecked():
                t= threading.Thread(target=profiles.action_watch_or_del, args=(2,startime,endtime,numthreads))
                t.setDaemon(True)
                t.start()
            if self.rd_direct_video.isChecked():
                t= threading.Thread(target=profiles.action_watch_or_del, args=(3,startime,endtime,numthreads))
                t.setDaemon(True)
                t.start()
            else:
                t= threading.Thread(target=profiles.action_watch_or_del, args=(1,startime,endtime,numthreads))
                t.setDaemon(True)
                t.start()
        else:
            if self.rd_search_video.isChecked():
                t= threading.Thread(target=profiles.action_watch_or_del, args=(5,startime,endtime,numthreads))
                t.setDaemon(True)
                t.start()
            if self.rd_direct_video.isChecked():
                t= threading.Thread(target=profiles.action_watch_or_del, args=(6,startime,endtime,numthreads))
                t.setDaemon(True)
                t.start()
        
    def create_profile(self):
        try:
            numthreads = self.spb_num_thread.value()
            useproxy=1
            if self.rd_yes_proxy.isChecked():
                useproxy=1
            else:
                useproxy=0
            # t= threading.Thread(target=profiles.action_create, args=(useproxy,numthreads))
            # t.setDaemon(True)
            # t.start()
            self.word_thread = WorkerThread(target=profiles.action_create, args=(useproxy, numthreads))
            self.word_thread.finished.connect(self.handle_thread_finished)  # Kết nối tín hiệu finished với phương thức handle_thread_finished
            self.word_thread.start()
            self.word_thread_view.wait()
        except:
            pass
    def create_profile_error(self):
        try:
            numthreads = self.spb_num_thread.value()
            useproxy=1
            if self.rd_yes_proxy.isChecked():
                useproxy=1
            else:
                useproxy=0
            # t= threading.Thread(target=profiles.action_create_forerror, args=(useproxy,numthreads))
            # t.setDaemon(True)
            # t.start()
            self.word_thread_err = WorkerThread(target=profiles.action_create_forerror, args=(useproxy, numthreads))
            self.word_thread_err.finished.connect(self.handle_thread_finished)  # Kết nối tín hiệu finished với phương thức handle_thread_finished
            self.word_thread_err.start()
            self.word_thread_view.wait()
        except:
            pass
    def handle_thread_finished(self):
        self.show_message_box()

    def show_message_box(self):
        QMessageBox.information(self, "Profiles", "Đã tạo profile và login xong.")
    def handle_thread_finished_delete(self):
        QMessageBox.information(self, "Profiles", "Đã xóa lịch sử web.")
    def handle_thread_finished_view(self):
        self.show_message_box_view()
    def show_message_box_view(self):
        QMessageBox.information(self, "View YTB", "Đã xem hết video.")
if __name__ == "__main__":
    folder_path = "Profiles"
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        print("Thư mục Profiles đã tồn tại.")
    else:
        os.makedirs(folder_path)
        print("Thư mục Profiles đã được tạo.")
    curren_time = get_time_now()
    print(curren_time)
    if curren_time > time_activate:
        print("Please activate")
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.setFixedHeight(600)
        MainWindow.setFixedWidth(550)
        MainWindow.show()
        sys.exit(app.exec())
    else:
        print("Time activate")
        app=QApplication(sys.argv)
        widget=QtWidgets.QStackedWidget()
        login_form = Login_w()
        ytb_form = YTB_main()
        widget.addWidget(login_form)
        widget.addWidget(ytb_form)
        widget.setCurrentIndex(0)
        widget.setFixedHeight(500)
        widget.setFixedWidth(400)
        widget.show()
        app.exec()