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

        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.score5 = 0

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
        self.ui.back_38.clicked.connect(self.backtomenu)

        self.ui.settings.clicked.connect(self.openinfo)

        self.ui.start.clicked.connect(self.levels)

        self.ui.first.clicked.connect(self.lvl1)

        self.ui.second.clicked.connect(self.lvl2)
        self.ui.third.clicked.connect(self.lvl3)
        self.ui.fourth.clicked.connect(self.lvl4)
        self.ui.fifth.clicked.connect(self.lvl5)


        self.ui.a_1.clicked.connect(self.adi)
        self.ui.a_2.clicked.connect(self.mistake1)
        self.ui.a_3.clicked.connect(self.mistake1)
        self.ui.a_4.clicked.connect(self.mistake1)
        self.ui.a_5.clicked.connect(self.mistake1)

        self.ui.b_1.clicked.connect(self.nik)
        self.ui.b_2.clicked.connect(self.mistake1)
        self.ui.b_3.clicked.connect(self.mistake1)
        self.ui.b_4.clicked.connect(self.mistake1)
        self.ui.b_5.clicked.connect(self.mistake1)

        self.ui.c_1.clicked.connect(self.lac)
        self.ui.c_2.clicked.connect(self.mistake1)
        self.ui.c_3.clicked.connect(self.mistake1)
        self.ui.c_4.clicked.connect(self.mistake1)
        self.ui.c_5.clicked.connect(self.mistake1)

        self.ui.d_1.clicked.connect(self.pum)
        self.ui.d_2.clicked.connect(self.mistake1)
        self.ui.d_3.clicked.connect(self.mistake1)
        self.ui.d_4.clicked.connect(self.mistake1)
        self.ui.d_5.clicked.connect(self.mistake1)

        self.ui.e_1.clicked.connect(self.jor)
        self.ui.e_2.clicked.connect(self.mistake1)
        self.ui.e_3.clicked.connect(self.mistake1)
        self.ui.e_4.clicked.connect(self.mistake1)
        self.ui.e_5.clicked.connect(self.mistake1)

        self.ui.hint_1.clicked.connect(self.hint1)


        self.ui.f_1.clicked.connect(self.reb)
        self.ui.f_2.clicked.connect(self.mistake2)
        self.ui.f_3.clicked.connect(self.mistake2)
        self.ui.f_4.clicked.connect(self.mistake2)
        self.ui.f_5.clicked.connect(self.mistake2)

        self.ui.g_1.clicked.connect(self.nb)
        self.ui.g_2.clicked.connect(self.mistake2)
        self.ui.g_3.clicked.connect(self.mistake2)
        self.ui.g_4.clicked.connect(self.mistake2)
        self.ui.g_5.clicked.connect(self.mistake2)

        self.ui.h_1.clicked.connect(self.ck)
        self.ui.h_2.clicked.connect(self.mistake2)
        self.ui.h_3.clicked.connect(self.mistake2)
        self.ui.h_4.clicked.connect(self.mistake2)
        self.ui.h_5.clicked.connect(self.mistake2)

        self.ui.i_1.clicked.connect(self.dc)
        self.ui.i_2.clicked.connect(self.mistake2)
        self.ui.i_3.clicked.connect(self.mistake2)
        self.ui.i_4.clicked.connect(self.mistake2)
        self.ui.i_5.clicked.connect(self.mistake2)

        self.ui.j_1.clicked.connect(self.und)
        self.ui.j_2.clicked.connect(self.mistake2)
        self.ui.j_3.clicked.connect(self.mistake2)
        self.ui.j_4.clicked.connect(self.mistake2)
        self.ui.j_5.clicked.connect(self.mistake2)

        self.ui.hint_2.clicked.connect(self.hint2)


        self.ui.k_1.clicked.connect(self.asc)
        self.ui.k_2.clicked.connect(self.mistake3)
        self.ui.k_3.clicked.connect(self.mistake3)
        self.ui.k_4.clicked.connect(self.mistake3)
        self.ui.k_5.clicked.connect(self.mistake3)

        self.ui.l_1.clicked.connect(self.vln)
        self.ui.l_2.clicked.connect(self.mistake3)
        self.ui.l_3.clicked.connect(self.mistake3)
        self.ui.l_4.clicked.connect(self.mistake3)
        self.ui.l_5.clicked.connect(self.mistake3)

        self.ui.m_1.clicked.connect(self.con)
        self.ui.m_2.clicked.connect(self.mistake3)
        self.ui.m_3.clicked.connect(self.mistake3)
        self.ui.m_4.clicked.connect(self.mistake3)
        self.ui.m_5.clicked.connect(self.mistake3)

        self.ui.n_1.clicked.connect(self.dck)
        self.ui.n_2.clicked.connect(self.mistake3)
        self.ui.n_3.clicked.connect(self.mistake3)
        self.ui.n_4.clicked.connect(self.mistake3)
        self.ui.n_5.clicked.connect(self.mistake3)

        self.ui.o_1.clicked.connect(self.van)
        self.ui.o_2.clicked.connect(self.mistake3)
        self.ui.o_3.clicked.connect(self.mistake3)
        self.ui.o_4.clicked.connect(self.mistake3)
        self.ui.o_5.clicked.connect(self.mistake3)

        self.ui.hint_3.clicked.connect(self.hint3)

        self.ui.p_1.clicked.connect(self.tnf)
        self.ui.p_2.clicked.connect(self.mistake4)
        self.ui.p_3.clicked.connect(self.mistake4)
        self.ui.p_4.clicked.connect(self.mistake4)
        self.ui.p_5.clicked.connect(self.mistake4)

        self.ui.q_1.clicked.connect(self.mon)
        self.ui.q_2.clicked.connect(self.mistake4)
        self.ui.q_3.clicked.connect(self.mistake4)
        self.ui.q_4.clicked.connect(self.mistake4)
        self.ui.q_5.clicked.connect(self.mistake4)

        self.ui.r_1.clicked.connect(self.hoo)
        self.ui.r_2.clicked.connect(self.mistake4)
        self.ui.r_3.clicked.connect(self.mistake4)
        self.ui.r_4.clicked.connect(self.mistake4)
        self.ui.r_5.clicked.connect(self.mistake4)

        self.ui.s_1.clicked.connect(self.tom)
        self.ui.s_2.clicked.connect(self.mistake4)
        self.ui.s_3.clicked.connect(self.mistake4)
        self.ui.s_4.clicked.connect(self.mistake4)
        self.ui.s_5.clicked.connect(self.mistake4)

        self.ui.t_1.clicked.connect(self.sto)
        self.ui.t_2.clicked.connect(self.mistake4)
        self.ui.t_3.clicked.connect(self.mistake4)
        self.ui.t_4.clicked.connect(self.mistake4)
        self.ui.t_5.clicked.connect(self.mistake4)

        self.ui.hint_4.clicked.connect(self.hint4)

        self.ui.u_1.clicked.connect(self.car)
        self.ui.u_2.clicked.connect(self.mistake5)
        self.ui.u_3.clicked.connect(self.mistake5)
        self.ui.u_4.clicked.connect(self.mistake5)
        self.ui.u_5.clicked.connect(self.mistake5)

        self.ui.v_1.clicked.connect(self.ell)
        self.ui.v_2.clicked.connect(self.mistake5)
        self.ui.v_3.clicked.connect(self.mistake5)
        self.ui.v_4.clicked.connect(self.mistake5)
        self.ui.v_5.clicked.connect(self.mistake5)

        self.ui.w_1.clicked.connect(self.bap)
        self.ui.w_2.clicked.connect(self.mistake5)
        self.ui.w_3.clicked.connect(self.mistake5)
        self.ui.w_4.clicked.connect(self.mistake5)
        self.ui.w_5.clicked.connect(self.mistake5)

        self.ui.x_1.clicked.connect(self.lyl)
        self.ui.x_2.clicked.connect(self.mistake5)
        self.ui.x_3.clicked.connect(self.mistake5)
        self.ui.x_4.clicked.connect(self.mistake5)
        self.ui.x_5.clicked.connect(self.mistake5)

        self.ui.y_1.clicked.connect(self.pol)
        self.ui.y_2.clicked.connect(self.mistake5)
        self.ui.y_3.clicked.connect(self.mistake5)
        self.ui.y_4.clicked.connect(self.mistake5)
        self.ui.y_5.clicked.connect(self.mistake5)

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
        self.mistakes1 = 0
        self.mistakes2 = 0
        self.mistakes3 = 0
        self.mistakes4 = 0
        self.mistakes5 = 0
        self.ui.stackedWidget.setCurrentIndex(0)

    def openinfo(self):
        self.ui.stackedWidget.setCurrentIndex(13)

    def levels(self):
        self.ui.stackedWidget.setCurrentIndex(1)


    def lvl1(self):
        self.healths = 5
        self.ui.healths_1.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.stackedWidget_2.setCurrentIndex(0)
    def lvl2(self):
        self.healths = 5
        self.ui.healths_2.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def lvl3(self):
        self.healths = 5
        self.ui.healths_3.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.stackedWidget_4.setCurrentIndex(0)
    def lvl4(self):
        self.healths = 5
        self.ui.healths_4.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(8)
        self.ui.stackedWidget_5.setCurrentIndex(0)
    def lvl5(self):
        self.healths = 5
        self.ui.healths_5.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(10)
        self.ui.stackedWidget_6.setCurrentIndex(0)


    def adi(self):
        self.scorec1()
        self.ui.stackedWidget_2.setCurrentIndex(1)
    def nik(self):
        self.scorec1()
        self.ui.stackedWidget_2.setCurrentIndex(2)
    def lac(self):
        self.scorec1()
        self.ui.stackedWidget_2.setCurrentIndex(3)
    def pum(self):
        self.scorec1()
        self.ui.stackedWidget_2.setCurrentIndex(4)
    def jor(self):
        self.scorec1()
        self.ui.stackedWidget.setCurrentIndex(3)
    def hint1(self):
        if self.healths<=3:
            hintBox = QMessageBox.information(window, "Подсказка", b)
            self.hints += 1
            self.hints1 += 1
            self.update_states()
            self.update_states1()
        else:
            hintBox = QMessageBox.information(window, "Подсказка не доступна", "У Вас ещё больше 3 попыток")
    def next1(self):
        self.healths = 5
        self.mistakes1 = 0
        self.ui.healths_2.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_3.setCurrentIndex(0)
    def mistake1(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.healths -= 1
        self.ui.healths_1.setText(str(self.healths))
        self.gameover()
        self.mistakes += 1
        self.mistakes1 += 1
        self.update_states()
        self.update_states1()
    def update_states1(self):
        self.ui.hintlabel_1.setText(str(self.hints1))
        self.ui.mistakelabel_1.setText(str(self.mistakes1))


    def reb(self):
        self.scorec2()
        self.ui.stackedWidget_3.setCurrentIndex(1)
    def nb(self):
        self.scorec2()
        self.ui.stackedWidget_3.setCurrentIndex(2)
    def ck(self):
        self.scorec2()
        self.ui.stackedWidget_3.setCurrentIndex(3)
    def dc(self):
        self.scorec2()
        self.ui.stackedWidget_3.setCurrentIndex(4)
    def und(self):
        self.scorec2()
        self.ui.stackedWidget.setCurrentIndex(5)
    def hint2(self):
        if self.healths <= 3:
            hintBox = QMessageBox.information(window, "Подсказка", c)
            self.hints += 1
            self.hints1 += 1
            self.update_states()
            self.update_states2()
        else:
            hintBox = QMessageBox.information(window, "Подсказка не доступна", "У Вас ещё больше 3 попыток")
    def next2(self):
        self.healths = 5
        self.mistakes2 = 0
        self.ui.healths_3.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(6)
        self.ui.stackedWidget_4.setCurrentIndex(0)
    def mistake2(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.healths -= 1
        self.ui.healths_2.setText(str(self.healths))
        self.gameover()
        self.mistakes += 1
        self.mistakes2 += 1
        self.update_states()
        self.update_states2()
    def update_states2(self):
        self.ui.hintlabel_2.setText(str(self.hints2))
        self.ui.mistakelabel_2.setText(str(self.mistakes2))


    def asc(self):
        self.scorec3()
        self.ui.stackedWidget_4.setCurrentIndex(1)
    def vln(self):
        self.scorec3()
        self.ui.stackedWidget_4.setCurrentIndex(2)
    def con(self):
        self.scorec3()
        self.ui.stackedWidget_4.setCurrentIndex(3)
    def dck(self):
        self.scorec3()
        self.ui.stackedWidget_4.setCurrentIndex(4)
    def van(self):
        self.scorec3()
        self.ui.stackedWidget.setCurrentIndex(7)
    def hint3(self):
        if self.healths <= 3:
            hintBox = QMessageBox.information(window, "Подсказка", d)
            self.hints += 1
            self.hints1 += 1
            self.update_states()
            self.update_states3()
        else:
            hintBox = QMessageBox.information(window, "Подсказка не доступна", "У Вас ещё больше 3 попыток")
    def next3(self):
        self.healths = 5
        self.mistakes3 = 0
        self.ui.healths_4.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(8)
        self.ui.stackedWidget_5.setCurrentIndex(0)
    def mistake3(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.healths -= 1
        self.ui.healths_3.setText(str(self.healths))
        self.gameover()
        self.mistakes += 1
        self.mistakes3 += 1
        self.update_states()
        self.update_states3()
    def update_states3(self):
        self.ui.hintlabel_3.setText(str(self.hints3))
        self.ui.mistakelabel_3.setText(str(self.mistakes3))


    def tnf(self):
        self.scorec4()
        self.ui.stackedWidget_5.setCurrentIndex(1)
    def mon(self):
        self.scorec4()
        self.ui.stackedWidget_5.setCurrentIndex(2)
    def hoo(self):
        self.scorec4()
        self.ui.stackedWidget_5.setCurrentIndex(3)
    def tom(self):
        self.scorec4()
        self.ui.stackedWidget_5.setCurrentIndex(4)
    def sto(self):
        self.scorec4()
        self.ui.stackedWidget.setCurrentIndex(9)
    def hint4(self):
        if self.healths <= 3:
            hintBox = QMessageBox.information(window, "Подсказка", e)
            self.hints += 1
            self.hints1 += 1
            self.update_states()
            self.update_states4()
        else:
            hintBox = QMessageBox.information(window, "Подсказка не доступна", "У Вас ещё больше 3 попыток")
    def next4(self):
        self.healths = 5
        self.mistakes4 = 0
        self.ui.healths_5.setText(str(self.healths))
        self.ui.stackedWidget.setCurrentIndex(10)
        self.ui.stackedWidget_6.setCurrentIndex(0)
    def mistake4(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.healths -= 1
        self.ui.healths_4.setText(str(self.healths))
        self.gameover()
        self.mistakes += 1
        self.mistakes4 += 1
        self.update_states()
        self.update_states4()
    def update_states4(self):
        self.ui.hintlabel_4.setText(str(self.hints4))
        self.ui.mistakelabel_4.setText(str(self.mistakes4))


    def car(self):
        self.scorec5()
        self.ui.stackedWidget_6.setCurrentIndex(1)

    def ell(self):
        self.scorec5()
        self.ui.stackedWidget_6.setCurrentIndex(2)

    def bap(self):
        self.scorec5()
        self.ui.stackedWidget_6.setCurrentIndex(3)

    def lyl(self):
        self.scorec5()
        self.ui.stackedWidget_6.setCurrentIndex(4)

    def pol(self):
        self.scorec5()
        self.ui.stackedWidget.setCurrentIndex(11)


    def hint5(self):
        if self.healths <= 3:
            hintBox = QMessageBox.information(window, "Подсказка", f)
            self.hints += 1
            self.hints1 += 1
            self.update_states()
            self.update_states5()
        else:
            hintBox = QMessageBox.information(window, "Подсказка не доступна", "У Вас ещё больше 3 попыток")
    def next5(self):
        self.scorec()
        self.mistakes5 = 0
        self.ui.stackedWidget.setCurrentIndex(12)
    def mistake5(self):
        msgBox = QMessageBox().warning(window, "Предупреждение", h)
        self.healths -= 1
        self.ui.healths_5.setText(str(self.healths))
        self.gameover()
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

    def gameover(self):
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.score4 = 0
        self.score5 = 0
        if self.healths <= 0:
            self.ui.stackedWidget.setCurrentIndex(14)

    def scorec1(self):
        if self.score1 >= 500:
            self.score1 = 0
        if self.mistakes1 == 0:
            self.score1 += 100
            self.ui.score_1.setText(str(self.score1))
        elif self.mistakes1 == 1:
            self.score1 += 80
            self.ui.score_1.setText(str(self.score1))
        elif self.mistakes1 >= 2:
            self.score1 += 50
            self.ui.score_1.setText(str(self.score1))
    def scorec2(self):
        if self.score2 >= 500:
            self.score2 = 0
        if self.mistakes2 == 0:
            self.score2 += 100
            self.ui.score_2.setText(str(self.score2))
        elif self.mistakes2 == 1:
            self.score2 += 80
            self.ui.score_2.setText(str(self.score2))
        elif self.mistakes2 >= 2:
            self.score2 += 50
            self.ui.score_2.setText(str(self.score2))
    def scorec3(self):
        if self.score3 >= 500:
            self.score3 = 0
        if self.mistakes3 == 0:
            self.score3 += 100
            self.ui.score_3.setText(str(self.score3))
        elif self.mistakes3 == 1:
            self.score3 += 80
            self.ui.score_3.setText(str(self.score3))
        elif self.mistakes3 >= 2:
            self.score3 += 50
            self.ui.score_3.setText(str(self.score3))
    def scorec4(self):
        if self.score4 >= 500:
            self.score4 = 0
        if self.mistakes4 == 0:
            self.score4 += 100
            self.ui.score_4.setText(str(self.score4))
        elif self.mistakes4 == 1:
            self.score4 += 80
            self.ui.score_4.setText(str(self.score4))
        elif self.mistakes4 >= 2:
            self.score4 += 50
            self.ui.score_4.setText(str(self.score4))
    def scorec5(self):
        if self.score5 >= 500:
            self.score5 = 0
        if self.mistakes5 == 0:
            self.score5 += 100
            self.ui.score_5.setText(str(self.score5))
        elif self.mistakes5 == 1:
            self.score5 += 80
            self.ui.score_5.setText(str(self.score5))
        elif self.mistakes5 >= 2:
            self.score5 += 50
            self.ui.score_5.setText(str(self.score5))
    def scorec(self):
        x = self.score1 + self.score2 + self.score3 + self.score4 + self.score5
        self.ui.score_6.setText(str(x))

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