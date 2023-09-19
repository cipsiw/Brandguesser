import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from brandguesser_ui import Ui_MainWindow
a = open("levels.txt", "r", encoding="utf-8")
b = a.readline()
c = a.readline()
d = a.readline()
e = a.readline()
f = a.readline()
g = open("mistake.txt", "r", encoding="utf-8")
h = g.read()
i = open("rules.txt", "r", encoding="utf-8")
j = i.read()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(0)

        self.hints1 = 0
        self.hints2 = 0
        self.hints3 = 0
        self.hints4 = 0
        self.hints5 = 0
        self.hints = 0

        self.mistakes1 = 0
        self.mistakes2 = 0
        self.mistakes3 = 0
        self.mistakes4 = 0
        self.mistakes5 = 0
        self.mistakes = 0

        self.player = QMediaPlayer()

        self.ui.label_12.setText(j)

        self.ui.back_1.clicked.connect(self.backtomenu)
        self.ui.back_2.clicked.connect(self.backtomenu)
        self.ui.back_3.clicked.connect(self.backtomenu)
        self.ui.back_4.clicked.connect(self.backtomenu)
        self.ui.back_5.clicked.connect(self.backtomenu)
        self.ui.back_6.clicked.connect(self.backtomenu)
        self.ui.back_7.clicked.connect(self.backtomenu)
        self.ui.back_8.clicked.connect(self.backtomenu)
        self.ui.back_9.clicked.connect(self.backtomenu)
        self.ui.back_10.clicked.connect(self.backtomenu)
        self.ui.back_11.clicked.connect(self.backtomenu)
        self.ui.back_12.clicked.connect(self.backtomenu)
        self.ui.back_13.clicked.connect(self.backtomenu)
        self.ui.back_14.clicked.connect(self.backtomenu)
        self.ui.back_15.clicked.connect(self.backtomenu)
        self.ui.back_16.clicked.connect(self.backtomenu)
        self.ui.back_17.clicked.connect(self.backtomenu)
        self.ui.back_18.clicked.connect(self.backtomenu)
        self.ui.back_19.clicked.connect(self.backtomenu)
        self.ui.back_20.clicked.connect(self.backtomenu)
        self.ui.back_21.clicked.connect(self.backtomenu)
        self.ui.back_22.clicked.connect(self.backtomenu)
        self.ui.back_23.clicked.connect(self.backtomenu)
        self.ui.back_24.clicked.connect(self.backtomenu)
        self.ui.back_25.clicked.connect(self.backtomenu)
        self.ui.back_26.clicked.connect(self.backtomenu)
        self.ui.back_27.clicked.connect(self.backtomenu)

        self.ui.settings.clicked.connect(self.openinfo)

        self.ui.start.clicked.connect(self.levels)

        self.ui.first.clicked.connect(self.lvl1)
        self.ui.second.clicked.connect(self.lvl2)
        self.ui.third.clicked.connect(self.lvl3)
        self.ui.fourth.clicked.connect(self.lvl4)
        self.ui.fifth.clicked.connect(self.lvl5)


        self.ui.check_1.clicked.connect(self.adi)
        self.ui.check_2.clicked.connect(self.nik)
        self.ui.check_3.clicked.connect(self.lac)
        self.ui.check_4.clicked.connect(self.pum)
        self.ui.check_5.clicked.connect(self.jor)
        self.ui.hint_1.clicked.connect(self.hint1)

        self.ui.check_6.clicked.connect(self.reb)
        self.ui.check_7.clicked.connect(self.nb)
        self.ui.check_8.clicked.connect(self.ck)
        self.ui.check_9.clicked.connect(self.dc)
        self.ui.check_10.clicked.connect(self.und)
        self.ui.hint_2.clicked.connect(self.hint2)

        self.ui.check_11.clicked.connect(self.asc)
        self.ui.check_12.clicked.connect(self.vln)
        self.ui.check_13.clicked.connect(self.con)
        self.ui.check_14.clicked.connect(self.dck)
        self.ui.check_15.clicked.connect(self.van)
        self.ui.hint_3.clicked.connect(self.hint3)

        self.ui.check_16.clicked.connect(self.tnf)
        self.ui.check_17.clicked.connect(self.mon)
        self.ui.check_18.clicked.connect(self.hoo)
        self.ui.check_19.clicked.connect(self.tom)
        self.ui.check_20.clicked.connect(self.sto)
        self.ui.hint_4.clicked.connect(self.hint4)

        self.ui.check_21.clicked.connect(self.car)
        self.ui.check_22.clicked.connect(self.ell)
        self.ui.check_23.clicked.connect(self.bap)
        self.ui.check_24.clicked.connect(self.lyl)
        self.ui.check_25.clicked.connect(self.pol)
        self.ui.hint_5.clicked.connect(self.hint5)

        self.ui.next_1.clicked.connect(self.next1)
        self.ui.next_2.clicked.connect(self.next2)
        self.ui.next_3.clicked.connect(self.next3)
        self.ui.next_4.clicked.connect(self.next4)
        self.ui.next_5.clicked.connect(self.next5)

        self.ui.pushButton.clicked.connect(self.mutesound)
        self.ui.plus.clicked.connect(self.volumeup)
        self.ui.minus.clicked.connect(self.volumedown)
        self.ui.play.clicked.connect(self.playsound)


    def backtomenu(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def openinfo(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def levels(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def lvl1(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def lvl2(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def lvl3(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.stackedWidget_4.setCurrentIndex(0)
    def lvl4(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        self.ui.stackedWidget_5.setCurrentIndex(0)
    def lvl5(self):
        self.ui.stackedWidget.setCurrentIndex(10)
        self.ui.stackedWidget_6.setCurrentIndex(0)


    def adi(self):
        if self.ui.lineEdit_1.text() == "Adidas":
            self.ui.stackedWidget_2.setCurrentIndex(1)
            self.ui.lineEdit_1.clear()
        else:
            self.mistake1()
    def nik(self):
        if self.ui.lineEdit_2.text() == "Nike":
            self.ui.stackedWidget_2.setCurrentIndex(2)
            self.ui.lineEdit_2.clear()
        else:
            self.mistake1()
    def lac(self):
        if self.ui.lineEdit_3.text() == "Lacoste":
            self.ui.stackedWidget_2.setCurrentIndex(3)
            self.ui.lineEdit_3.clear()
        else:
            self.mistake1()
    def pum(self):
        if self.ui.lineEdit_4.text() == "Puma":
            self.ui.stackedWidget_2.setCurrentIndex(4)
            self.ui.lineEdit_4.clear()
        else:
            self.mistake1()
    def jor(self):
        if self.ui.lineEdit_5.text() == "Jordan":
            self.ui.stackedWidget.setCurrentIndex(3)
            self.ui.lineEdit_5.clear()
            self.ui.stackedWidget_3.setCurrentIndex(0)
        else:
            self.mistake1()
    def hint1(self):
        hintBox = QMessageBox.information(window, "Подсказка", b)
        self.hints += 1
        self.hints1 += 1
        self.update_states()
        self.update_states1()
    def next1(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    def mistake1(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.mistakes += 1
        self.mistakes1 += 1
        self.update_states()
        self.update_states1()
    def update_states1(self):
        self.ui.hintlabel_1.setText(str(self.hints1))
        self.ui.mistakelabel_1.setText(str(self.mistakes1))


    def reb(self):
        if self.ui.lineEdit_6.text() == "Reebok":
            self.ui.stackedWidget_3.setCurrentIndex(1)
            self.ui.lineEdit_6.clear()
        else:
            self.mistake2()
    def nb(self):
        if self.ui.lineEdit_7.text() == "New Balance":
            self.ui.stackedWidget_3.setCurrentIndex(2)
            self.ui.lineEdit_7.clear()
        else:
            self.mistake2()
    def ck(self):
        if self.ui.lineEdit_8.text() == "Calvin Klein":
            self.ui.stackedWidget_3.setCurrentIndex(3)
            self.ui.lineEdit_8.clear()
        else:
            self.mistake2()
    def dc(self):
        if self.ui.lineEdit_9.text() == "DC Shoes":
            self.ui.stackedWidget_3.setCurrentIndex(4)
            self.ui.lineEdit_9.clear()
        else:
            self.mistake2()
    def und(self):
        if self.ui.lineEdit_10.text() == "Under Armour":
            self.ui.stackedWidget.setCurrentIndex(5)
            self.ui.lineEdit_10.clear()
            self.ui.stackedWidget_4.setCurrentIndex(0)
        else:
            self.mistake2()
    def hint2(self):
        hintBox = QMessageBox.information(window, "Подсказка", c)
        self.hints += 1
        self.hints2 += 1
        self.update_states()
        self.update_states2()
    def next2(self):
        self.ui.stackedWidget.setCurrentIndex(6)
    def mistake2(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.mistakes += 1
        self.mistakes2 += 1
        self.update_states()
        self.update_states2()
    def update_states2(self):
        self.ui.hintlabel_2.setText(str(self.hints2))
        self.ui.mistakelabel_2.setText(str(self.mistakes2))


    def asc(self):
        if self.ui.lineEdit_11.text() == "Asics":
            self.ui.stackedWidget_4.setCurrentIndex(1)
            self.ui.lineEdit_11.clear()
        else:
            self.mistake3()
    def vln(self):
        if self.ui.lineEdit_12.text() == "Vlone":
            self.ui.stackedWidget_4.setCurrentIndex(2)
            self.ui.lineEdit_12.clear()
        else:
            self.mistake3()
    def con(self):
        if self.ui.lineEdit_13.text() == "Converse":
            self.ui.stackedWidget_4.setCurrentIndex(3)
            self.ui.lineEdit_13.clear()
        else:
            self.mistake3()
    def dck(self):
        if self.ui.lineEdit_14.text() == "Dickies":
            self.ui.stackedWidget_4.setCurrentIndex(4)
            self.ui.lineEdit_14.clear()
        else:
            self.mistake3()
    def van(self):
        if self.ui.lineEdit_15.text() == "Vans":
            self.ui.stackedWidget.setCurrentIndex(7)
            self.ui.lineEdit_15.clear()
            self.ui.stackedWidget_5.setCurrentIndex(0)
        else:
            self.mistake3()
    def hint3(self):
        hintBox = QMessageBox.information(window, "Подсказка", d)
        self.hints += 1
        self.hints3 += 1
        self.update_states()
        self.update_states3()
    def next3(self):
        self.ui.stackedWidget.setCurrentIndex(8)
    def mistake3(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.mistakes += 1
        self.mistakes3 += 1
        self.update_states()
        self.update_states3()
    def update_states3(self):
        self.ui.hintlabel_3.setText(str(self.hints3))
        self.ui.mistakelabel_3.setText(str(self.mistakes3))


    def tnf(self):
        if self.ui.lineEdit_16.text() == "The North Face":
            self.ui.stackedWidget_5.setCurrentIndex(1)
            self.ui.lineEdit_16.clear()
        else:
            self.mistake4()
    def mon(self):
        if self.ui.lineEdit_17.text() == "Moncler":
            self.ui.stackedWidget_5.setCurrentIndex(2)
            self.ui.lineEdit_17.clear()
        else:
            self.mistake4()
    def hoo(self):
        if self.ui.lineEdit_18.text() == "Hoka One One":
            self.ui.stackedWidget_5.setCurrentIndex(3)
            self.ui.lineEdit_18.clear()
        else:
            self.mistake4()
    def tom(self):
        if self.ui.lineEdit_19.text() == "Tommy Hilfiger":
            self.ui.stackedWidget_5.setCurrentIndex(4)
            self.ui.lineEdit_19.clear()
        else:
            self.mistake4()
    def sto(self):
        if self.ui.lineEdit_20.text() == "Stone Island":
            self.ui.stackedWidget.setCurrentIndex(9)
            self.ui.lineEdit_20.clear()
            self.ui.stackedWidget_6.setCurrentIndex(0)
        else:
            self.mistake4()
    def hint4(self):
        hintBox = QMessageBox.information(window, "Подсказка", e)
        self.hints += 1
        self.hints4 += 1
        self.update_states()
        self.update_states4()
    def next4(self):
        self.ui.stackedWidget.setCurrentIndex(10)
    def mistake4(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.mistakes += 1
        self.mistakes4 += 1
        self.update_states()
        self.update_states4()
    def update_states4(self):
        self.ui.hintlabel_4.setText(str(self.hints4))
        self.ui.mistakelabel_4.setText(str(self.mistakes4))


    def car(self):
        if self.ui.lineEdit_21.text() == "Carhartt":
            self.ui.stackedWidget_6.setCurrentIndex(1)
            self.ui.lineEdit_21.clear()
        else:
            self.mistake5()
    def ell(self):
        if self.ui.lineEdit_22.text() == "Ellesse":
            self.ui.stackedWidget_6.setCurrentIndex(2)
            self.ui.lineEdit_22.clear()
        else:
            self.mistake5()
    def bap(self):
        if self.ui.lineEdit_23.text() == "A Bathing Ape":
            self.ui.stackedWidget_6.setCurrentIndex(3)
            self.ui.lineEdit_23.clear()
        else:
            self.mistake5()
    def lyl(self):
        if self.ui.lineEdit_24.text() == "Lyle&Scott":
            self.ui.stackedWidget_6.setCurrentIndex(4)
            self.ui.lineEdit_24.clear()
        else:
            self.mistake5()
    def pol(self):
        if self.ui.lineEdit_25.text() == "Polo Ralph Lauren":
            self.ui.stackedWidget.setCurrentIndex(11)
            self.ui.lineEdit_25.clear()
            self.update_states()
        else:
            self.mistake5()
    def hint5(self):
        hintBox = QMessageBox.information(window, "Подсказка", f)
        self.hints += 1
        self.hints5 += 1
        self.update_states()
        self.update_states5()
    def next5(self):
        self.ui.stackedWidget.setCurrentIndex(12)
    def mistake5(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.mistakes += 1
        self.mistakes5 += 1
        self.update_states()
        self.update_states5()
    def update_states5(self):
        self.ui.hintlabel_5.setText(str(self.hints5))
        self.ui.mistakelabel_5.setText(str(self.mistakes5))

    def update_states(self):
        self.ui.hintlabel_6.setText(str(self.hints))
        self.ui.mistakelabel_6.setText(str(self.mistakes))


    def playsound(self):
        soundt = os.path.join(os.getcwd(), "1.mp3")
        url = QUrl.fromLocalFile(soundt)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()

    def mutesound(self):
        self.player.setMuted(not self.player.isMuted())

    def volumeup(self):
        curvolume = self.player.volume()
        self.player.setVolume(curvolume + 5)

    def volumedown(self):
        curvolume = self.player.volume()
        self.player.setVolume(curvolume - 5)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	sys.exit(app.exec_())