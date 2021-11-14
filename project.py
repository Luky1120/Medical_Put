#PyQt5를 사용하기 위한 import문
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.uiparser import QtWidgets

#아두이노 시리얼 통신에 필요한 import문
import serial

#아두이노의 컴포트 값과 딜레이
arduino = serial.Serial('COM4', 9600)

#PyQt5를 이용하여 제작한 UI파일을 파이썬 코드와 연결
form_class = uic.loadUiType("C:\PyQT\project\project2.ui")[0]

#타이레놀 설명 폼
class cmWindow(QDialog):
    def __init__(self,parent1):
        super(cmWindow, self).__init__(parent1)
        uic.loadUi("C:\PyQT\project\cm.ui",self)
        self.show()
     

#후시딘 설명 폼
class hsWindow(QDialog):
    def __init__(self,parent2):
        super(hsWindow, self).__init__(parent2)
        uic.loadUi("C:\PyQT\project\hs.ui",self)
        self.show()
       

#메인 폼    
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_3.clicked.connect(self.button3_clicked)
        self.pushButton_3.clicked.connect(self.Motermove1)
        self.click_count1 = 0

        self.pushButton_4.clicked.connect(self.button4_clicked)
        self.pushButton_4.clicked.connect(self.Motermove2)
        self.click_count2 = 0
        
        pixmap1 = QPixmap('C:\PyQT\image\cm.png')
        self.label.setPixmap(pixmap1)
        pixmap2 = QPixmap('C:\PyQT\image\hs.jpg')
        self.label_2.setPixmap(pixmap2)

        self.pushButton.clicked.connect(self.cm)
        self.pushButton_2.clicked.connect(self.hs)

        #버튼 활성화 버튼
        self.pushButton_5.clicked.connect(self.buntton3_clear)
        self.pushButton_5.clicked.connect(self.buntton4_clear)
        

    #타이레놀 설명 폼을 열기 위한 함수
    def cm(self):
        cmWindow(self)
    
    #후시딘 설명 폼을 열기 위한 함수
    def hs(self):
        hsWindow(self)
    
    def button3_clicked(self):
        self.click_count1 += 1
        #클릭을 4번하여 다시 모터 동작을 초기화 하고 버튼 비활성화
        if self.click_count1==4:
            self.click_count1=0
            self.pushButton_3.setEnabled(False)

    def button4_clicked(self):
        self.click_count2 += 1
        #클릭을 4번하여 다시 모터 동작을 초기화 하고 버튼 비활성화
        if self.click_count2==4:
            self.click_count2=0
            self.pushButton_4.setEnabled(False)

    #타이레놀 모터 동작 함수
































    
    def Motermove1(self):
        print('1번모터 동작')
        m ='1'
        m = [m.encode('utf-8')]
        arduino.writelines(m)

    #후시딘 모터 동작 함수
    def Motermove2(self):
        print('2번모터 동작')
        m ='2'
        m = [m.encode('utf-8')]
        arduino.writelines(m)

    def buntton3_clear(self):
        self.pushButton_3.setEnabled(True)
    
    def buntton4_clear(self):
        self.pushButton_4.setEnabled(True)

app=QApplication(sys.argv)
mainWindow = WindowClass()
mainWindow.show()
app.exec_()