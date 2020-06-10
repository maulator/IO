from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from Modules import  baza as baza

class Ui_MainWindow(object):
    cnt_ch = 0
    cnt_m = 0
    temp_cnt = 20
    StopStartFlag = 0
    isMaszynaOn = 0
    current_timer = None
    rozruch_timer = None
    time_timer = None
    dropping_timer = None
    In_flag = 0
    rozruch_cnt = 0
    rozruch_click_cnt = 0
    time_cnt = 0
    time_display = '00:00:00'
    zm_baza_pra, zm_baza_chlo = 0,0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1016, 851)
        
       

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1016, 851))
        self.stackedWidget.setObjectName("stackedWidget") 


        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")

        self.logowanie_text = QtWidgets.QLabel(self.login_page)
        self.logowanie_text.setGeometry(QtCore.QRect(410, 90, 240, 50))
        self.logowanie_text.setText("Logowanie")
        self.logowanie_text.setStyleSheet(""" 
                    QWidget{
                    font-size:40px;
                    text-align: center;
                    }
            """)


        self.login_label = QtWidgets.QLineEdit(self.login_page)
        self.login_label.setGeometry(QtCore.QRect(388, 160, 240, 31))
        self.login_label.setObjectName("login_label")
        self.login_label.setPlaceholderText("login")

        self.haslo_label = QtWidgets.QLineEdit(self.login_page)
        self.haslo_label.setGeometry(QtCore.QRect(388, 200, 240, 31))
        self.haslo_label.setObjectName("haslo_label")
        self.haslo_label.setPlaceholderText("haslo")
        self.haslo_label.setEchoMode(2)

        self.potwierdz_button = QtWidgets.QPushButton(self.login_page)
        self.potwierdz_button.setGeometry(QtCore.QRect(418, 240, 181, 40))
        self.potwierdz_button.setObjectName("potwierdz_button")
        self.potwierdz_button.setText('Potwierdź')

        self.stackedWidget.addWidget(self.login_page)
        


        self.control_page = QtWidgets.QWidget()
        self.control_page.setObjectName("control_page")

       

        self.MenuBg = QtWidgets.QLabel(self.control_page)
        self.MenuBg.setGeometry(QtCore.QRect(0, 0, 1016, 851))
        self.MenuBg.setText("")
        self.MenuBg.setPixmap(QtGui.QPixmap("to2.png"))

        self.go_to_baza = QtWidgets.QPushButton(self.control_page)
        self.go_to_baza.setGeometry(QtCore.QRect(28, 731, 181, 60))
        self.go_to_baza.setObjectName("go_to_baza")
        self.go_to_baza.setText('Baza danych')


        self.chlodzenie_button = QtWidgets.QPushButton(self.control_page)
        self.chlodzenie_button.setGeometry(QtCore.QRect(28, 19, 184, 183))
        self.chlodzenie_button.setObjectName("chlodzenie_button")
        self.chlodzenie_button.setText("Chłodzenie ręczne off")
        self.chlodzenie_button.setStyleSheet(""" 
            QPushButton{
                color:black;
                background-color: light grey;
            }
            """)
        self.maszyny_button_on = QtWidgets.QPushButton(self.control_page)
        self.maszyny_button_on.setGeometry(QtCore.QRect(28, 289, 184, 184))
        self.maszyny_button_on.setObjectName("maszyny_button_on")
        self.maszyny_button_on.setText("Maszyny on")
        self.maszyny_button_on.setStyleSheet(""" 
            QPushButton{
                color:black;
                background-color: green;
            }
            """)
        self.maszyny_button_off = QtWidgets.QPushButton(self.control_page)
        self.maszyny_button_off.setGeometry(QtCore.QRect(28, 289, 184, 184))
        self.maszyny_button_off.setObjectName("maszyny_button_on")
        self.maszyny_button_off.setText("Maszyny off")
        self.maszyny_button_off.setStyleSheet(""" 
            QPushButton{
                color:black;
                background-color: light grey;
            }
            """)
        self.temp_lcd = QtWidgets.QLCDNumber(self.control_page)
        self.temp_lcd.setGeometry(QtCore.QRect(383, 351, 100, 75))
        self.temp_lcd.setObjectName("temp_lcd")

        self.czas_lcd = QtWidgets.QLCDNumber(self.control_page)
        self.czas_lcd.setGeometry(QtCore.QRect(808, 48, 150, 80))
        self.czas_lcd.setObjectName("czas_lcd")
        self.rozruch_button = QtWidgets.QPushButton(self.control_page)
        self.rozruch_button.setGeometry(QtCore.QRect(227, 328, 145, 105))
        self.rozruch_button.setObjectName("rozruch_button")
        self.rozruch_button.setText("Rozruch")
        self.maszyny_moc_bar = QtWidgets.QProgressBar(self.control_page)
        self.maszyny_moc_bar.setGeometry(QtCore.QRect(230, 450, 141, 21))
        self.maszyny_moc_bar.setProperty("value", 24)
        self.maszyny_moc_bar.setObjectName("maszyny_moc_bar")
        self.maszyny_moc_bar.setStyleSheet("""
            QProgressBar::chunk { background: grey; }
            QWidget {
                      text-align: center;
                }
            """)
        self.stop_button = QtWidgets.QPushButton(self.control_page)
        self.stop_button.setGeometry(QtCore.QRect(809, 600, 181, 181))
        self.stop_button.setObjectName("stop_button")
        self.start_button = QtWidgets.QPushButton(self.control_page)
        self.start_button.setGeometry(QtCore.QRect(809, 410, 181, 181))
        self.start_button.setObjectName("start_button")
        self.temp_text = QtWidgets.QLabel(self.control_page)
        self.temp_text.setGeometry(QtCore.QRect(380, 315, 101, 41))
        self.temp_text.setObjectName("temp_text")
        self.czas_dzialania_text = QtWidgets.QLabel(self.control_page)
        self.czas_dzialania_text.setGeometry(QtCore.QRect(840, 20, 151, 31))
        self.czas_dzialania_text.setObjectName("czas_dzialania_text")
        self.info_frame = QtWidgets.QFrame(self.control_page)
        self.info_frame.setGeometry(QtCore.QRect(390, 70, 301, 101))
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.info_frame.setStyleSheet('background-image:url("warning.jpg")')
        self.info_text = QtWidgets.QLabel(self.info_frame)
        self.info_text.setGeometry(QtCore.QRect(0, 0, 301, 101))
        self.info_text.setText("")
        self.info_text.setObjectName("info_text")
        self.info_text.setStyleSheet(""" 
                    QWidget{
                    font-size:15px;
                    text-align: center;
                    padding:10px;
                    }
            """)

        self.stackedWidget.addWidget(self.control_page) 

        self.baza_page = QtWidgets.QWidget()
        self.baza_page.setObjectName("baza_page")

        self.baza_display = QtWidgets.QTextEdit(self.baza_page)
        self.baza_display.setGeometry(QtCore.QRect(140, 150, 731, 261))
        self.baza_display.setObjectName("baza_display")
        self.baza_display.setReadOnly(True)
        self.baza_display.setOverwriteMode(True)
        self.baza_pracownikow_button = QtWidgets.QPushButton(self.baza_page)
        self.baza_pracownikow_button.setGeometry(QtCore.QRect(210, 30, 171, 71))
        self.baza_pracownikow_button.setObjectName("baza_pracownikow_button")
        self.baza_danych_chlo = QtWidgets.QPushButton(self.baza_page)
        self.baza_danych_chlo.setGeometry(QtCore.QRect(410, 30, 171, 71))
        self.baza_danych_chlo.setObjectName("baza_danych_chlo")
        self.baza_danych_mag = QtWidgets.QPushButton(self.baza_page)
        self.baza_danych_mag.setGeometry(QtCore.QRect(610, 30, 171, 71))
        self.baza_danych_mag.setObjectName("baza_danych_mag")
        self.dodaj_button = QtWidgets.QPushButton(self.baza_page)
        self.dodaj_button.setGeometry(QtCore.QRect(140, 430, 101, 51))
        self.dodaj_button.setObjectName("dodaj_button")
        self.usun_button = QtWidgets.QPushButton(self.baza_page)
        self.usun_button.setGeometry(QtCore.QRect(770, 430, 101, 51))
        self.usun_button.setObjectName("usun_button")

        self.frame = QtWidgets.QFrame(self.baza_page)
        self.frame.setGeometry(QtCore.QRect(330, 500, 351, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.id_input = QtWidgets.QLineEdit(self.frame)
        self.id_input.setGeometry(QtCore.QRect(210, 0, 141, 31))
        self.id_input.setObjectName("id_input")
        self.id_prac_text = QtWidgets.QLabel(self.frame)
        self.id_prac_text.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.id_prac_text.setObjectName("id_prac_text")
        self.imie_prac_text = QtWidgets.QLabel(self.frame)
        self.imie_prac_text.setGeometry(QtCore.QRect(0, 40, 131, 31))
        self.imie_prac_text.setObjectName("imie_prac_text")
        self.imie_input = QtWidgets.QLineEdit(self.frame)
        self.imie_input.setGeometry(QtCore.QRect(210, 40, 141, 31))
        self.imie_input.setObjectName("imie_input")
        self.nazw_prac_text = QtWidgets.QLabel(self.frame)
        self.nazw_prac_text.setGeometry(QtCore.QRect(0, 80, 131, 31))
        self.nazw_prac_text.setObjectName("nazw_prac_text")
        self.nazwisko_input = QtWidgets.QLineEdit(self.frame)
        self.nazwisko_input.setGeometry(QtCore.QRect(210, 80, 141, 31))
        self.nazwisko_input.setObjectName("nazwisko_input")
        self.sta_prac_text = QtWidgets.QLabel(self.frame)
        self.sta_prac_text.setGeometry(QtCore.QRect(0, 120, 131, 31))
        self.sta_prac_text.setObjectName("sta_prac_text")
        self.stanowisko_input = QtWidgets.QLineEdit(self.frame)
        self.stanowisko_input.setGeometry(QtCore.QRect(210, 120, 141, 31))
        self.stanowisko_input.setObjectName("stanowisko_input")
        self.zatwierdz_button = QtWidgets.QPushButton(self.frame)
        self.zatwierdz_button.setGeometry(QtCore.QRect(110, 160, 121, 41))
        self.zatwierdz_button.setObjectName("zatwierdz_button")

        self.usun_frame = QtWidgets.QFrame(self.baza_page)
        self.usun_frame.setGeometry(QtCore.QRect(330, 500, 351, 201))
        self.usun_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usun_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.id_input2 = QtWidgets.QLineEdit(self.usun_frame)
        self.id_input2.setGeometry(QtCore.QRect(210, 0, 141, 31))
        self.id_input2.setObjectName("id_input")
        self.id_prac_text2 = QtWidgets.QLabel(self.usun_frame)
        self.id_prac_text2.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.id_prac_text2.setObjectName("id_prac_text2")
       
        self.zatwierdz_button2 = QtWidgets.QPushButton(self.usun_frame)
        self.zatwierdz_button2.setGeometry(QtCore.QRect(110, 160, 121, 41))
        self.zatwierdz_button2.setObjectName("zatwierdz_button")

        self.go_to_control = QtWidgets.QPushButton(self.baza_page)
        self.go_to_control.setGeometry(QtCore.QRect(28, 731, 181, 60))
        self.go_to_control.setObjectName("go_to_control")
        self.go_to_control.setText('Panel kontrolny')

        self.stackedWidget.addWidget(self.baza_page) 


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

########################### MY CODE #################################################################################
        self.czas_lcd.setDigitCount(8)
        self.frame.setVisible(0)
        self.usun_frame.setVisible(0)
        self.temp_lcd.display(self.temp_cnt)
        self.czas_lcd.display(self.time_display)
        self.info_frame.setVisible(0)
        self.maszyny_button_on.setVisible(0)
        self.chlodzenie_button.setEnabled(False)
        self.maszyny_button_on.setEnabled(False)
        self.maszyny_button_off.setEnabled(False)
        self.rozruch_button.setEnabled(False)
        self.maszyny_moc_bar.setMaximum(100)
        self.maszyny_moc_bar.setProperty("value", 0)
########################## BUTTONS EVENTS #######################################
        self.chlodzenie_button.clicked.connect(self.chlodzenie_on)
        self.maszyny_button_on.clicked.connect(self.maszyny_off)
        self.maszyny_button_off.clicked.connect(self.maszyny_on)
        self.start_button.clicked.connect(self.start_fun)
        self.stop_button.clicked.connect(self.stop_fun)
        self.rozruch_button.clicked.connect(self.rozruch_timer_fun)
        self.go_to_baza.clicked.connect(self.go_to_baza_fun)
        self.potwierdz_button.clicked.connect(self.potwierdz_fun)
        self.baza_pracownikow_button.clicked.connect(self.pokaz_pracownikow)
        self.baza_danych_chlo.clicked.connect(self.pokaz_chlodzenie)
        self.baza_danych_mag.clicked.connect(self.pokaz_magazyn)
        self.dodaj_button.clicked.connect(self.pokaz_dodaj)
        self.zatwierdz_button.clicked.connect(self.dodaj_do_bazy)
        self.zatwierdz_button2.clicked.connect(self.usun_z_bazy)
        self.usun_button.clicked.connect(self.pokaz_usun)
        self.go_to_control.clicked.connect(self.go_to_control_fun)
########################## FUNCTIONS ###############################################


    def go_to_control_fun(self):
        self.stackedWidget.setCurrentIndex(1)

    def chlodzenie_on(self):
        self.chlodzenie_button.setText("Chłodzenie ręczne on")
        self.chlodzenie_button.setStyleSheet(""" 
            QPushButton{
                background-color: green;
            }
            """)
        self.cnt_ch += 1
        self.dropping_timer.stop()
        self.dropping_timer.timeout.connect(self.temperature_dropping_reczny)
        self.dropping_timer.start(500)
        if self.cnt_ch%2 == 0:
            self.chlodzenie_button.setText("Chłodzenie ręczne off")
            self.chlodzenie_button.setStyleSheet(""" 
            QPushButton{
                background-color: light grey;
            }
            """)
            self.dropping_timer.stop()




    def maszyny_off(self):
        self.maszyny_button_on.setVisible(0)
        self.maszyny_button_off.setVisible(1)
        self.cnt_m = 0
        self.maszyny_button_on.setText("Maszyny on")
        self.maszyny_button_on.setStyleSheet(""" 
        QPushButton{
            background-color: green;
        }
        """)
        self.current_timer.stop()

    def maszyny_on(self):

        self.maszyny_button_on.setVisible(1)
        self.maszyny_button_off.setVisible(0)
        self.cnt_m = 1
        self.maszyny_button_off.setText("Maszyny off")
        self.maszyny_button_off.setStyleSheet(""" 
        QPushButton{
            background-color: light grey;
        }
        """)
        self.dropping_timer.stop()
        self.current_timer.timeout.connect(self.temperature_rising)
        self.current_timer.start(25)

    def stop_timer(self):

       self.current_timer.stop()

    def temperature_rising(self):
        self.dropping_timer.stop()
        if self.temp_cnt >=1220:
            self.current_timer.stop()
        else:
            self.temp_cnt += 1
            self.temp_lcd.display(self.temp_cnt)
            if self.temp_cnt == 700:
                self.current_timer.setInterval(50)
            elif self.temp_cnt == 800:
                self.current_timer.setInterval(100)
            elif self.temp_cnt == 1100:
                self.current_timer.setInterval(250)
            elif self.temp_cnt == 1200:
                self.current_timer.setInterval(500)
            elif self.temp_cnt == 1200:
                self.info_text.setText("Włączam chłodzenie!")
                self.info_frame.setVisible(1)
            elif self.temp_cnt== 1215:
                self.info_frame.setVisible(0)
            elif self.temp_cnt == 1220:
                self.info_text.setText("Temperatura krytyczna!")
                self.info_frame.setVisible(1)
                self.current_timer.stop()
                self.dropping_timer.timeout.connect(self.temperature_drooping)
                self.dropping_timer.start(500)


    def temperature_drooping(self):
        self.temp_cnt = self.temp_cnt -1
        self.temp_lcd.display(self.temp_cnt)
        if self.temp_cnt == 1150:
            self.info_frame.setVisible(0)
            self.dropping_timer.stop()

    def temperature_dropping_reczny(self):
        self.current_timer.stop()
        self.temp_cnt = self.temp_cnt -1
        self.temp_lcd.display(self.temp_cnt)
        if self.temp_cnt == 1150:
            self.info_frame.setVisible(0)
            self.dropping_timer.stop()

   
    def start_fun(self):
        self.chlodzenie_button.setEnabled(True)
        self.rozruch_button.setEnabled(True)
        self.current_timer = QtCore.QTimer()
        self.dropping_timer = QtCore.QTimer()
        self.rozruch_timer = QtCore.QTimer()
        self.time_timer = QtCore.QTimer()
        self.time_cnt_fun()

    def stop_fun(self):
        if self.current_timer.isActive() == True:
             self.stop_timer()
        else:
            pass
        if self.rozruch_timer.isActive() == True:
             self.rozruch_timer.stop()
        else:
            pass
        self.chlodzenie_button.setEnabled(False)
        self.maszyny_button_on.setEnabled(False)
        self.maszyny_button_off.setEnabled(False)
        self.chlodzenie_button.setStyleSheet("background-color:none;")
        self.chlodzenie_button.setText("Chłodzenie ręczne off")
        self.maszyny_button_on.setStyleSheet("background-color:none;")
        self.maszyny_button_on.setText("Maszyny off")
        self.cnt_ch = 0
        self.cnt_m = 0
        self.temp_cnt = 20
        self.rozruch_cnt = 0
        self.temp_lcd.display(self.temp_cnt)
        self.rozruch_timer = 0
        self.maszyny_moc_bar.setProperty("value", 0)
        self.time_timer.stop()
        self.time_display = '00:00:00'
        self.time_cnt = 0
        self.czas_lcd.display(self.time_display)

    def rozruch_timer_fun(self):
        self.rozruch_timer.timeout.connect(self.rozruch_fun)
        self.rozruch_timer.start(250)

    def rozruch_fun(self):
        self.rozruch_button.setEnabled(False)

        if self.rozruch_cnt == 100:
            self.rozruch_timer.stop()
            self.maszyny_moc_bar.setStyleSheet("""
            QProgressBar::chunk { background: green; }
            QWidget {
                      text-align: center;
                }
            """)
            self.maszyny_button_on.setEnabled(True)
            self.maszyny_button_off.setEnabled(True)
        self.maszyny_moc_bar.setProperty("value", int(self.rozruch_cnt))
        self.rozruch_cnt += 1
        self.temp_cnt += 2
        self.temp_lcd.display(self.temp_cnt)

    def time_counter(self,s):
      min, s = divmod(s, 60)
      h, min = divmod(min, 60)
      d, h = divmod(h, 24)
      return h, min, s

    def time_cnt_fun(self):
        self.time_timer.timeout.connect(self.lcd_time_fun)
        self.time_timer.start(1000)

    def lcd_time_fun(self):
        self.time_cnt += 1
        h,m,s = self.time_counter(self.time_cnt) 
        sw0 = "0{}".format(s)
        mw0 = "0{}".format(m)
        hw0 = "0{}".format(h)
        tmps,tmpm,tmph = s,m,h
        if s < 10:
            s = sw0
        else:
            s = tmps
        if m < 10:
            m = mw0
        else:
            m = tmpm
        if h < 10:
            h = hw0
        else:
            h = tmph
        self.time_display = "{}:{}:{}".format(h,m,s)
        self.czas_lcd.display(self.time_display)

    def chlodzenie_reczne_fun(self):
        self.dropping_timer.stop()
        self.current_timer.stop()
        self.dropping_timer.timeout.connect(self.temperature_dropping_reczny)
        self.dropping_timer.start(500)

################################ BAZA DANYCH FUNKCJE ######################################
    def go_to_baza_fun(self):
        self.stackedWidget.setCurrentIndex(2)

    def potwierdz_fun(self):
        login = baza.wyswietl(baza.wypisz('login','logowanie'))[0][0]
        haslo = baza.wyswietl(baza.wypisz('haslo','logowanie'))[0][0]
        if login == self.login_label.text() and haslo == self.haslo_label.text():
            self.stackedWidget.setCurrentIndex(1)
        else:
            self.login_label.setStyleSheet("border:2px solid red")
            self.haslo_label.setStyleSheet("border:2px solid red")

    def pokaz_pracownikow(self):
        self.baza_display.clear()
        first_col ='ID           Imie                 Nazwisko              Stanowisko\n'
        self.baza_display.setText(first_col)
        pracownikID = baza.wyswietl(baza.wypisz('pracownikID','pracownik'))
        pracownikImie = baza.wyswietl(baza.wypisz('pracownikImie','pracownik'))
        pracownikNazwisko = baza.wyswietl(baza.wypisz('pracownikNazwisko','pracownik'))
        stanowisko = baza.wyswietl(baza.wypisz('stanowisko','pracownik'))
        all_res = baza.wyswietl(baza.wypisz_all('pracownik'))
        for i in range(len(all_res)):
            res = '{}           {}                 {}              {}\n'.format(pracownikID[i][0],pracownikImie[i][0],pracownikNazwisko[i][0],stanowisko[i][0])
            self.baza_display.append(res)
       
    def pokaz_chlodzenie(self):
        self.baza_display.clear()
        first_col ='ID             Data                     Godzina            Temperatura\n'
        self.baza_display.setText(first_col)
        chlodzenieID = baza.wyswietl(baza.wypisz('chlodzenieID','chlodzenie'))
        dataChlodzenia = baza.wyswietl(baza.wypisz('dataChlodzenia','chlodzenie'))
        godzinaChlodzenia = baza.wyswietl(baza.wypisz('godzinaChlodzenia','chlodzenie'))
        temp = baza.wyswietl(baza.wypisz('temp','chlodzenie'))
        all_res = baza.wyswietl(baza.wypisz_all('chlodzenie'))
        for i in range(len(all_res)):
            res = '{}           {}          {}          {}\n'.format(chlodzenieID[i][0],dataChlodzenia[i][0],godzinaChlodzenia[i][0],temp[i][0])
            self.baza_display.append(res)

    def pokaz_magazyn(self):
        self.baza_display.clear()
        first_col ='ID              Nazwa produktu          cena          Data zamowienia          ilosc\n'
        self.baza_display.setText(first_col)
        materialID = baza.wyswietl(baza.wypisz('materialID','magazyn'))
        produktNazwa = baza.wyswietl(baza.wypisz('produktNazwa','magazyn'))
        cena = baza.wyswietl(baza.wypisz('cena','magazyn'))
        dataZamowienia = baza.wyswietl(baza.wypisz('dataZamowienia','magazyn'))
        ilosc = baza.wyswietl(baza.wypisz('ilosc','magazyn'))
        all_res = baza.wyswietl(baza.wypisz_all('magazyn'))
        for i in range(len(all_res)):
            res = '{}           {}                         {}            {}               {}\n'.format(materialID[i][0],produktNazwa[i][0],cena[i][0],dataZamowienia[i][0],ilosc[i][0])
            self.baza_display.append(res)

    def pokaz_dodaj(self):
        self.frame.setVisible(1)
        self.usun_frame.setVisible(0)
        self.id_input2.clear()

    def dodaj_do_bazy(self):
        
        id_pracownika = self.id_input.text()
        imie_pracownika = self.imie_input.text()
        nazwisko_pracownika = self.nazwisko_input.text()
        stanowisko_pracownika = self.stanowisko_input.text()
        if id_pracownika == "" or imie_pracownika == "" or nazwisko_pracownika == "" or stanowisko_pracownika == "":
            print('Nie można dodać pracownika')
        else:
            baza.dodaj_pracownika(id_pracownika,imie_pracownika,nazwisko_pracownika,stanowisko_pracownika)
            self.frame.setVisible(0)
            self.id_input.clear()
            self.imie_input.clear()
            self.nazwisko_input.clear()
            self.stanowisko_input.clear()

    def pokaz_usun(self):
        self.usun_frame.setVisible(1)
        self.frame.setVisible(0)
        self.id_input.clear()
        self.imie_input.clear()
        self.nazwisko_input.clear()
        self.stanowisko_input.clear()

    def usun_z_bazy(self):
        id_pracownika = self.id_input2.text()
        baza.usun_pracownika(id_pracownika)
        self.usun_frame.setVisible(0)
        self.id_input2.clear()
        

########################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chlodzenie_button.setText(_translate("MainWindow", "Chłodzenie ręczne off"))
        self.maszyny_button_on.setText(_translate("MainWindow", "Maszyny on"))
        self.maszyny_button_off.setText(_translate("MainWindow", "Maszyny off"))
        self.stop_button.setText(_translate("MainWindow", "Stop systemu"))
        self.start_button.setText(_translate("MainWindow", "Start Systemu"))
        self.temp_text.setText(_translate("MainWindow", "Temperatura"))
        self.baza_pracownikow_button.setText(_translate("MainWindow", "Baza danych pracowników"))
        self.baza_danych_chlo.setText(_translate("MainWindow", "Baza danych chłodzenia"))
        self.baza_danych_mag.setText(_translate("MainWindow", "Baza danych magazynu"))
        self.dodaj_button.setText(_translate("MainWindow", "Dodaj"))
        self.usun_button.setText(_translate("MainWindow", "Usuń"))
        self.id_prac_text.setText(_translate("MainWindow", "ID pracownika"))
        self.imie_prac_text.setText(_translate("MainWindow", "Imie pracownika"))
        self.nazw_prac_text.setText(_translate("MainWindow", "Nazwisko pracownika"))
        self.sta_prac_text.setText(_translate("MainWindow", "Stanowisko"))
        self.zatwierdz_button.setText(_translate("MainWindow", "Zatwierdź"))
        self.id_prac_text2.setText(_translate("MainWindow", "ID pracownika"))
        self.zatwierdz_button2.setText(_translate("MainWindow", "Zatwierdź"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
