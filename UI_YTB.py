# Form implementation generated from reading ui file 'UI_YTB.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import profiles
import subprocess
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_mail = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gb_mail.setEnabled(True)
        self.gb_mail.setGeometry(QtCore.QRect(10, 10, 781, 271))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gb_mail.setFont(font)
        self.gb_mail.setStyleSheet("color: rgb(67, 0, 0);")
        self.gb_mail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_mail.setFlat(True)
        self.gb_mail.setCheckable(False)
        self.gb_mail.setObjectName("gb_mail")
        self.gb_profiles = QtWidgets.QGroupBox(parent=self.gb_mail)
        self.gb_profiles.setGeometry(QtCore.QRect(60, 40, 191, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_profiles.setFont(font)
        self.gb_profiles.setTabletTracking(False)
        self.gb_profiles.setStyleSheet("background-color: rgb(0, 217, 217);")
        self.gb_profiles.setObjectName("gb_profiles")
        self.rd_chrome = QtWidgets.QRadioButton(parent=self.gb_profiles)
        self.rd_chrome.setGeometry(QtCore.QRect(40, 40, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_chrome.setFont(font)
        self.rd_chrome.setCheckable(True)
        self.rd_chrome.setChecked(False)
        self.rd_chrome.setAutoRepeat(False)
        self.rd_chrome.setAutoExclusive(True)
        self.rd_chrome.setObjectName("rd_chrome")
        self.rd_gpm = QtWidgets.QRadioButton(parent=self.gb_profiles)
        self.rd_gpm.setGeometry(QtCore.QRect(40, 80, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_gpm.setFont(font)
        self.rd_gpm.setObjectName("rd_gpm")
        self.bt_open_profiles = QtWidgets.QPushButton(parent=self.gb_profiles)
        self.bt_open_profiles.setGeometry(QtCore.QRect(40, 140, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_open_profiles.setFont(font)
        self.bt_open_profiles.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_open_profiles.setObjectName("bt_open_profiles")
        self.gb_proxy = QtWidgets.QGroupBox(parent=self.gb_mail)
        self.gb_proxy.setGeometry(QtCore.QRect(330, 40, 191, 211))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_proxy.setFont(font)
        self.gb_proxy.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gb_proxy.setObjectName("gb_proxy")
        self.rd_no_proxy = QtWidgets.QRadioButton(parent=self.gb_proxy)
        self.rd_no_proxy.setGeometry(QtCore.QRect(60, 50, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_no_proxy.setFont(font)
        self.rd_no_proxy.setObjectName("rd_no_proxy")
        self.rd_yes_proxy = QtWidgets.QRadioButton(parent=self.gb_proxy)
        self.rd_yes_proxy.setGeometry(QtCore.QRect(60, 90, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_yes_proxy.setFont(font)
        self.rd_yes_proxy.setObjectName("rd_yes_proxy")
        self.bt_import_proxy = QtWidgets.QPushButton(parent=self.gb_proxy)
        self.bt_import_proxy.setGeometry(QtCore.QRect(50, 140, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.bt_import_proxy.setFont(font)
        self.bt_import_proxy.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_import_proxy.setObjectName("bt_import_proxy")
        self.gb_bt_mail = QtWidgets.QGroupBox(parent=self.gb_mail)
        self.gb_bt_mail.setGeometry(QtCore.QRect(590, 40, 120, 211))
        self.gb_bt_mail.setMaximumSize(QtCore.QSize(120, 220))
        self.gb_bt_mail.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.gb_bt_mail.setStyleSheet("border-color: rgb(85, 170, 255);\n"
"background-color: rgb(164, 255, 157);")
        self.gb_bt_mail.setTitle("")
        self.gb_bt_mail.setFlat(False)
        self.gb_bt_mail.setObjectName("gb_bt_mail")
        self.bt_import_mail = QtWidgets.QPushButton(parent=self.gb_bt_mail)
        self.bt_import_mail.setGeometry(QtCore.QRect(20, 15, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_import_mail.setFont(font)
        self.bt_import_mail.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_import_mail.setObjectName("bt_import_mail")
        self.bt_login_mail = QtWidgets.QPushButton(parent=self.gb_bt_mail)
        self.bt_login_mail.setGeometry(QtCore.QRect(20, 55, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_login_mail.setFont(font)
        self.bt_login_mail.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.bt_login_mail.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_login_mail.setObjectName("bt_login_mail")
        self.bt_mail_error = QtWidgets.QPushButton(parent=self.gb_bt_mail)
        self.bt_mail_error.setGeometry(QtCore.QRect(20, 95, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_mail_error.setFont(font)
        self.bt_mail_error.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.bt_mail_error.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_mail_error.setObjectName("bt_mail_error")
        self.bt_login_mail_error = QtWidgets.QPushButton(parent=self.gb_bt_mail)
        self.bt_login_mail_error.setGeometry(QtCore.QRect(20, 135, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_login_mail_error.setFont(font)
        self.bt_login_mail_error.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_login_mail_error.setObjectName("bt_login_mail_error")
        self.bt_remove_history = QtWidgets.QPushButton(parent=self.gb_bt_mail)
        self.bt_remove_history.setGeometry(QtCore.QRect(20, 175, 80, 25))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_remove_history.setFont(font)
        self.bt_remove_history.setAutoFillBackground(False)
        self.bt_remove_history.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_remove_history.setAutoDefault(False)
        self.bt_remove_history.setDefault(False)
        self.bt_remove_history.setFlat(False)
        self.bt_remove_history.setObjectName("bt_remove_history")
        self.gb_view_ytb = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.gb_view_ytb.setGeometry(QtCore.QRect(10, 299, 781, 271))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gb_view_ytb.setFont(font)
        self.gb_view_ytb.setStyleSheet("color: rgb(66, 0, 0);")
        self.gb_view_ytb.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.gb_view_ytb.setFlat(True)
        self.gb_view_ytb.setObjectName("gb_view_ytb")
        self.gb_type_view = QtWidgets.QGroupBox(parent=self.gb_view_ytb)
        self.gb_type_view.setGeometry(QtCore.QRect(59, 30, 401, 171))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gb_type_view.setFont(font)
        self.gb_type_view.setStyleSheet("background-color: rgb(149, 176, 200);")
        self.gb_type_view.setObjectName("gb_type_view")
        self.rd_random_view_video = QtWidgets.QRadioButton(parent=self.gb_type_view)
        self.rd_random_view_video.setGeometry(QtCore.QRect(40, 30, 201, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_random_view_video.setFont(font)
        self.rd_random_view_video.setAutoExclusive(False)
        self.rd_random_view_video.setObjectName("rd_random_view_video")
        self.rd_search_video = QtWidgets.QRadioButton(parent=self.gb_type_view)
        self.rd_search_video.setGeometry(QtCore.QRect(40, 75, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_search_video.setFont(font)
        self.rd_search_video.setObjectName("rd_search_video")
        self.rd_direct_video = QtWidgets.QRadioButton(parent=self.gb_type_view)
        self.rd_direct_video.setGeometry(QtCore.QRect(40, 120, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.rd_direct_video.setFont(font)
        self.rd_direct_video.setObjectName("rd_direct_video")
        self.bt_import_key = QtWidgets.QPushButton(parent=self.gb_type_view)
        self.bt_import_key.setGeometry(QtCore.QRect(200, 75, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_import_key.setFont(font)
        self.bt_import_key.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_import_key.setObjectName("bt_import_key")
        self.bt_import_link = QtWidgets.QPushButton(parent=self.gb_type_view)
        self.bt_import_link.setGeometry(QtCore.QRect(200, 120, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_import_link.setFont(font)
        self.bt_import_link.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_import_link.setObjectName("bt_import_link")
        self.gb_bt_view_ytb = QtWidgets.QGroupBox(parent=self.gb_view_ytb)
        self.gb_bt_view_ytb.setGeometry(QtCore.QRect(490, 30, 251, 231))
        self.gb_bt_view_ytb.setStyleSheet("background-color: rgb(146, 153, 255);")
        self.gb_bt_view_ytb.setTitle("")
        self.gb_bt_view_ytb.setObjectName("gb_bt_view_ytb")
        self.label = QtWidgets.QLabel(parent=self.gb_bt_view_ytb)
        self.label.setGeometry(QtCore.QRect(30, 30, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.gb_bt_view_ytb)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.gb_bt_view_ytb)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.bt_exit = QtWidgets.QPushButton(parent=self.gb_bt_view_ytb)
        self.bt_exit.setGeometry(QtCore.QRect(80, 190, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_exit.setFont(font)
        self.bt_exit.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_exit.setObjectName("bt_exit")
        self.spb_num_thread = QtWidgets.QSpinBox(parent=self.gb_bt_view_ytb)
        self.spb_num_thread.setGeometry(QtCore.QRect(150, 30, 45, 30))
        self.spb_num_thread.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spb_num_thread.setObjectName("spb_num_thread")
        self.spb_time_view = QtWidgets.QSpinBox(parent=self.gb_bt_view_ytb)
        self.spb_time_view.setGeometry(QtCore.QRect(150, 80, 45, 30))
        self.spb_time_view.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spb_time_view.setObjectName("spb_time_view")
        self.spb_time_delay = QtWidgets.QSpinBox(parent=self.gb_bt_view_ytb)
        self.spb_time_delay.setGeometry(QtCore.QRect(150, 130, 45, 30))
        self.spb_time_delay.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.spb_time_delay.setObjectName("spb_time_delay")
        self.bt_running = QtWidgets.QPushButton(parent=self.gb_view_ytb)
        self.bt_running.setGeometry(QtCore.QRect(100, 220, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_running.setFont(font)
        self.bt_running.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_running.setObjectName("bt_running")
        self.bt_pause = QtWidgets.QPushButton(parent=self.gb_view_ytb)
        self.bt_pause.setGeometry(QtCore.QRect(320, 220, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.bt_pause.setFont(font)
        self.bt_pause.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.bt_pause.setObjectName("bt_pause")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
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
        profiles.write_flag('0')
    def input_proxy(self):
        profiles.open_file_with_notepad('proxy.txt')
    def input_keyword(self):
        profiles.open_file_with_notepad('keyword.txt')
    def input_link(self):
        profiles.open_file_with_notepad('link-video.txt')
    def input_mail(self):
        profiles.open_file_with_notepad('gmail.txt')
    def mail_error(self):
        profiles.open_file_with_notepad('mail_error.txt')
    def delete_history(self):
        profiles.action_watch_or_del(mode=4,end_time=10,start_time=20,num_threads=0)
    def exit(self):
        sys.exit()
    def watch_video(self):
        numthreads = self.spb_num_thread.value()
        timedelay = self.spb_time_delay.value()
        startime= self.spb_time_view.value() - timedelay
        endtime= self.spb_time_view.value() + timedelay
        if self.rd_random_view_video.isChecked():
            profiles.action_watch_or_del(mode=1,end_time=endtime,start_time=startime,num_threads=numthreads)
        if self.rd_search_video.isChecked():
            profiles.action_watch_or_del(mode=2,end_time=endtime,start_time=startime,num_threads=numthreads)
        if self.rd_direct_video.isChecked():
            profiles.action_watch_or_del(mode=3,end_time=endtime,start_time=startime,num_threads=numthreads)
    def create_profile(self):
        numthreads = self.spb_num_thread.value()
        if self.rd_yes_proxy.isChecked():
            useproxy=1
        else:
            useproxy=0
        profiles.action_create(use_proxy=useproxy,numthread=numthreads)
    def create_profile_error(self):
        numthreads = self.spb_num_thread.value()
        if self.rd_yes_proxy.isChecked():
            useproxy=1
        else:
            useproxy=0
        profiles.action_create_forerror(use_proxy=useproxy,numthread=numthreads)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTB VIEWER"))
        self.gb_mail.setTitle(_translate("MainWindow", "MAIL"))
        self.gb_profiles.setTitle(_translate("MainWindow", "PROFILES"))
        self.rd_chrome.setText(_translate("MainWindow", "Chrome"))
        self.rd_gpm.setText(_translate("MainWindow", "GPM"))
        self.bt_open_profiles.setText(_translate("MainWindow", "Mở thư mục"))
        self.gb_proxy.setTitle(_translate("MainWindow", "PROXY"))
        self.rd_no_proxy.setText(_translate("MainWindow", "NO"))
        self.rd_yes_proxy.setText(_translate("MainWindow", "YES"))
        self.bt_import_proxy.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.bt_import_proxy.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.bt_import_proxy.setText(_translate("MainWindow", "Nhập proxy"))
        self.gb_bt_mail.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><br/></p></body></html>"))
        self.gb_bt_mail.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt;\"><br/></span></p></body></html>"))
        self.bt_import_mail.setText(_translate("MainWindow", "Nhập Mail"))
        self.bt_login_mail.setText(_translate("MainWindow", "Login Mail"))
        self.bt_mail_error.setText(_translate("MainWindow", "Mail Lỗi"))
        self.bt_login_mail_error.setText(_translate("MainWindow", "Login Mail Lỗi"))
        self.bt_remove_history.setText(_translate("MainWindow", "Xóa Lịch Sử"))
        self.gb_view_ytb.setTitle(_translate("MainWindow", "View YTB"))
        self.gb_type_view.setTitle(_translate("MainWindow", "Loại View"))
        self.rd_random_view_video.setText(_translate("MainWindow", "Xem video ngẫu nhiên"))
        self.rd_search_video.setText(_translate("MainWindow", "Tìm kiếm"))
        self.rd_direct_video.setText(_translate("MainWindow", "Trực tiếp"))
        self.bt_import_key.setText(_translate("MainWindow", "Nhập từ khóa"))
        self.bt_import_link.setText(_translate("MainWindow", "Nhập link"))
        self.label.setText(_translate("MainWindow", "Số Luồng"))
        self.label_2.setText(_translate("MainWindow", "Thời gian xem"))
        self.label_3.setText(_translate("MainWindow", "Thời gian delay"))
        self.bt_exit.setText(_translate("MainWindow", "Thoát"))
        self.bt_running.setText(_translate("MainWindow", "Chạy"))
        self.bt_pause.setText(_translate("MainWindow", "Dừng"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
