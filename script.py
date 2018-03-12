import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
from PyQt5.QtGui import *

UI_File, _ = loadUiType(os.path.join(os.path.dirname('__file__'), "Score Board.ui"))


def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QEvent.MouseButtonPress:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class MainApp(QMainWindow, UI_File):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui()
        self.actions()

    def ui(self):
        self.setFixedSize(800, 514)
        self.call1.setVisible(False)
        self.call2.setVisible(False)
        self.call3.setVisible(False)
        self.call4.setVisible(False)
        self.with1.setVisible(False)
        self.with2.setVisible(False)
        self.with3.setVisible(False)
        self.with4.setVisible(False)
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        self.p1edit.setFocus(True)
        self.multi_label.setVisible(False)

    def actions(self):
        self.reset_bt.clicked.connect(self.reset)
        self.clear_bt.clicked.connect(self.clear)
        self.calculate_bt.clicked.connect(self.calculate)

        #self.p1call.toggled.connect(self.update)
        #self.p2call.toggled.connect(self.update)
        #self.p3call.toggled.connect(self.update)
        #self.p4call.toggled.connect(self.update)

        #self.p1call.toggled.connect(self.with_update)
        #self.p2call.toggled.connect(self.with_update)
        #self.p3call.toggled.connect(self.with_update)
        #self.p4call.toggled.connect(self.with_update)

        self.p1edit.textChanged.connect(self.ui_update)
        self.p2edit.textChanged.connect(self.ui_update)
        self.p3edit.textChanged.connect(self.ui_update)
        self.p4edit.textChanged.connect(self.ui_update)

        self.p1result.textChanged.connect(self.ui_update)
        self.p2result.textChanged.connect(self.ui_update)
        self.p3result.textChanged.connect(self.ui_update)
        self.p4result.textChanged.connect(self.ui_update)

    def with_update2(self):
        if self.p1call.isEnabled():
            # self.p1with.setEnabled(True)
            # self.p1with.setChecked(True)
            if self.p1call.isChecked():
                self.p1with.setEnabled(False)
                self.p1with.setChecked(False)
                # p4 risk test
                dif = abs(13 - (p1c + p2c + p3c))
                if abs(dif - p4c) == 3 or abs(dif - p4c) == 2:
                    print('Risk')
                    self.risk4.setVisible(True)
                    self.risk4.setText('Risk')
                    self.risk4.setGeometry(710, 230, 31, 16)
                elif abs(dif - p4c) == 1 or abs(dif - p4c) == 0:
                    print('not risk')
                else:
                    print('D.Risk')
                    self.risk4.setVisible(True)
                    self.risk4.setText('D.Risk')
                    self.risk4.setGeometry(710, 230, 41, 16)
                print('difff', dif)
            else:
                self.p1with.setEnabled(True)
                self.p1with.setChecked(True)
                self.risk4.setVisible(False)

        if self.p2call.isEnabled():
            # self.p2with.setEnabled(True)
            # self.p2with.setChecked(True)
            if self.p2call.isChecked():
                self.p2with.setEnabled(False)
                self.p2with.setChecked(False)
                # p1 risk test
                dif = abs(13 - (p2c + p4c + p3c))
                if abs(dif - p1c) == 3 or abs(dif - p1c) == 2:
                    print('Risk')
                    self.risk1.setVisible(True)
                    self.risk1.setText('Risk')
                    self.risk1.setGeometry(170, 60, 31, 16)
                elif abs(dif - p1c) == 1 or abs(dif - p1c) == 0:
                    print('not risk')
                else:
                    print('D.Risk')
                    self.risk1.setVisible(True)
                    self.risk1.setText('D.Risk')
                    self.risk1.setGeometry(170, 60, 41, 16)
                print('difff', dif)
            else:
                self.p2with.setEnabled(True)
                self.p2with.setChecked(True)
                self.risk1.setVisible(False)

        if self.p3call.isEnabled():
            # self.p3with.setEnabled(True)
            # self.p3with.setChecked(True)
            if self.p3call.isChecked():
                self.p3with.setEnabled(False)
                self.p3with.setChecked(False)
                # p2 risk test
                dif = abs(13 - (p1c + p4c + p3c))
                if abs(dif - p2c) == 3 or abs(dif - p2c) == 2:
                    print('Risk')
                    self.risk2.setVisible(True)
                    self.risk2.setText('Risk')
                    self.risk2.setGeometry(170, 230, 31, 16)
                elif abs(dif - p2c) == 1 or abs(dif - p2c) == 0:
                    print('not risk')
                else:
                    print('D.Risk')
                    self.risk2.setVisible(True)
                    self.risk2.setText('D.Risk')
                    self.risk2.setGeometry(170, 230, 41, 16)
                print('difff', dif)
            else:
                self.p3with.setEnabled(True)
                self.p3with.setChecked(True)
                self.risk2.setVisible(False)

        if self.p4call.isEnabled():
            # self.p4with.setEnabled(True)
            # self.p4with.setChecked(True)
            if self.p4call.isChecked():
                self.p4with.setEnabled(False)
                self.p4with.setChecked(False)
                # p3 risk test
                dif = abs(13 - (p4c + p2c + p1c))
                if abs(dif - p3c) == 3 or abs(dif - p3c) == 2:
                    print('Risk')
                    self.risk3.setVisible(True)
                    self.risk3.setText('Risk')
                    self.risk3.setGeometry(710, 60, 31, 16)
                elif abs(dif - p3c) == 1 or abs(dif - p3c) == 0:
                    print('not risk')
                else:
                    print('D.Risk')
                    self.risk3.setVisible(True)
                    self.risk3.setText('D.Risk')
                    self.risk3.setGeometry(710, 60, 41, 16)
                print('difff', dif)
            else:
                self.p4with.setEnabled(True)
                self.p4with.setChecked(True)
                self.risk3.setVisible(False)

    def with_update(self):
        '''
        # with checked or not (toggle event)
        if self.p1call.isChecked() and (self.p1with.isEnabled() or self.p1with.isChecked()):
            self.p1with.setChecked(False)
            self.p1with.setEnabled(False)
        if self.p2call.isChecked() and (self.p2with.isEnabled() or self.p2with.isChecked()):
            self.p2with.setChecked(False)
            self.p2with.setEnabled(False)
        if self.p3call.isChecked() and (self.p3with.isEnabled() or self.p3with.isChecked()):
            self.p3with.setChecked(False)
            self.p3with.setEnabled(False)
        if self.p4call.isChecked() and (self.p4with.isEnabled() or self.p4with.isChecked()):
            self.p4with.setChecked(False)
            self.p4with.setEnabled(False)
        '''
        pass

    def update(self):
        global p1c, p2c, p3c, p4c
        p1c = self.p1edit.text()
        p2c = self.p2edit.text()
        p3c = self.p3edit.text()
        p4c = self.p4edit.text()
        calls=[]
        ls_players=['p1','p2','p3','p4']
        caller=[]
        dc=[]
        if check_int(p1c):
            p1c = int(p1c)
            calls.append(p1c)
        else:
            if self.p1edit.text() == 'd':
                p1c=0
                calls.append(0)
            else:
                self.p1edit.clear()
                QMessageBox.warning(self,'error','input must be number or d only')
                self.p1edit.setFocus(True)
                return
        if check_int(p2c):
            p2c=int(p2c)
            calls.append(p2c)
        else:
            if self.p2edit.text() == 'd':
                    p2c=0
                    calls.append(0)
            else:
                self.p2edit.clear()
                QMessageBox.warning(self,'error','input must be number or d only')
                self.p2edit.setFocus(True)
                return

        if check_int(p3c):
            p3c=int(p3c)
            calls.append(p3c)
        else:
            if self.p3edit.text() == 'd':
                p3c=0
                calls.append(0)
            else:
                self.p3edit.clear()
                QMessageBox.warning(self,'error','input must be number or d only')
                self.p3edit.setFocus(True)
                return

        if check_int(p4c):
            p4c=int(p4c)
            calls.append(p4c)
        else:
            if self.p4edit.text() == 'd':
                    p4c=0
                    calls.append(0)
            else:
                self.p4edit.clear()
                QMessageBox.warning(self,'error','input must be number or d only')
                self.p4edit.setFocus(True)
                return

        for i in calls:
            if i == 0:
                dc.append(i)
        print('dc', dc)
        if len(dc) > 2:
            QMessageBox.warning(self, 'error', 'no more two dash calls allowed')
            self.p1edit.clear()
            self.p2edit.clear()
            self.p3edit.clear()
            self.p4edit.clear()
            self.p1edit.setFocus(True)
            return

        call = max(calls)
        if sum(calls) == 13:
            QMessageBox.warning(self, 'Call error', 'total calls must be lower or greater than 13')
            calls.clear()
            self.p1edit.clear()
            self.p2edit.clear()
            self.p3edit.clear()
            self.p4edit.clear()
            self.p1edit.setFocus(True)
            return

        for x, y in zip(calls, ls_players):
            if x == call:
                caller.append(y)

        if len(caller)==1:
            self.p1edit.setEnabled(False)
            self.p2edit.setEnabled(False)
            self.p3edit.setEnabled(False)
            self.p4edit.setEnabled(False)
            self.p1result.setFocus(True)
            if ls_players[0] in caller:
                self.p1call.setChecked(True)
                self.p1call.setEnabled(True)
                self.p2call.setEnabled(False)
                self.p3call.setEnabled(False)
                self.p4call.setEnabled(False)
                self.p2call.setChecked(False)
                self.p3call.setChecked(False)
                self.p4call.setChecked(False)
            elif ls_players[1] in caller:
                self.p1call.setEnabled(False)
                self.p2call.setChecked(True)
                self.p2call.setEnabled(True)
                self.p3call.setEnabled(False)
                self.p4call.setEnabled(False)
                self.p1call.setChecked(False)
                self.p3call.setChecked(False)
                self.p4call.setChecked(False)
            elif ls_players[2] in caller:
                self.p1call.setEnabled(False)
                self.p2call.setEnabled(False)
                self.p3call.setChecked(True)
                self.p3call.setEnabled(True)
                self.p4call.setEnabled(False)
            elif ls_players[3] in caller:
                self.p1call.setEnabled(False)
                self.p2call.setEnabled(False)
                self.p3call.setEnabled(False)
                self.p4call.setChecked(True)
                self.p4call.setEnabled(True)
                self.p1call.setChecked(False)
                self.p2call.setChecked(False)
                self.p3call.setChecked(False)

        elif len(caller) == 2 or len(caller) == 3 or len(caller) == 4:
            self.p1edit.setEnabled(False)
            self.p2edit.setEnabled(False)
            self.p3edit.setEnabled(False)
            self.p4edit.setEnabled(False)
            self.p1result.setFocus(True)

            if ls_players[0] not in caller:
                self.p1call.setEnabled(False)
            else:
                self.p1call.setEnabled(True)
                self.p1call.setChecked(True)
                self.p1with.setChecked(False)
                self.p1with.setEnabled(False)

            if ls_players[1] not in caller:
                self.p2call.setEnabled(False)
            else:
                self.p2call.setEnabled(True)
                self.p2call.setChecked(True)
                self.p2with.setChecked(False)
                self.p2with.setEnabled(False)

            if ls_players[2] not in caller:
                self.p3call.setEnabled(False)
            else:
                self.p3call.setEnabled(True)
                self.p3call.setChecked(True)
                self.p3with.setChecked(False)
                self.p3with.setEnabled(False)

            if ls_players[3] not in caller:
                self.p4call.setEnabled(False)
            else:
                self.p4call.setEnabled(True)
                self.p4call.setChecked(True)
                self.p4with.setChecked(False)
                self.p4with.setEnabled(False)

            if 'p1' in caller:
                self.p1call.toggled.connect(self.with_update2)
                if self.p1call.isChecked():
                    self.p1with.setEnabled(False)
                else:
                    self.p1with.setEnabled(True)
                    self.p1with.setChecked(True)

            if 'p2' in caller:
                self.p2call.toggled.connect(self.with_update2)
                if self.p2call.isChecked():
                    self.p2with.setEnabled(False)
                else:
                    self.p2with.setEnabled(True)
                    self.p2with.setChecked(True)

            if 'p3' in caller:
                self.p3call.toggled.connect(self.with_update2)
                if self.p3call.isChecked():
                    self.p3with.setEnabled(False)
                else:
                    self.p3with.setEnabled(True)
                    self.p3with.setChecked(True)

            if 'p4' in caller:
                self.p4call.toggled.connect(self.with_update2)
                if self.p4call.isChecked():
                    self.p4with.setEnabled(False)
                else:
                    self.p4with.setEnabled(True)
                    self.p4with.setChecked(True)

        print(caller)
        print('calls list',calls)
        print(p1c, p2c, p3c, p4c)

        if self.call1.isVisible() and self.p4edit.text() != 'd':
            # p4 risk logic
            dif = abs(13 - (p1c + p2c + p3c))
            if abs(dif - p4c) == 3 or abs(dif - p4c) == 2:
                print('Risk')
                self.risk4.setVisible(True)
                self.risk4.setText('Risk')
                self.risk4.setGeometry(710, 230, 31, 16)
            elif abs(dif - p4c) == 1 or abs(dif - p4c) == 0:
                print('not risk')
            else:
                print('D.Risk')
                self.risk4.setVisible(True)
                self.risk4.setText('D.Risk')
                self.risk4.setGeometry(710,230,41,16)
            print('difff', dif)
            print('test 1')

        if self.call2.isVisible() and self.p1edit.text() != 'd':
            # p1 risk logic
            dif = abs(13 - (p2c + p4c + p3c))
            if abs(dif - p1c) == 3 or abs(dif - p1c) == 2:
                print('Risk')
                self.risk1.setVisible(True)
                self.risk1.setText('Risk')
                self.risk1.setGeometry(170, 60, 31, 16)
            elif abs(dif - p1c) == 1 or abs(dif - p1c) == 0:
                print('not risk')
            else:
                print('D.Risk')
                self.risk1.setVisible(True)
                self.risk1.setText('D.Risk')
                self.risk1.setGeometry(170, 60, 41, 16)
            print('difff', dif)
            print('test 2')

        if self.call3.isVisible() and self.p2edit.text() != 'd':
            # p2 risk logic
            dif = abs(13 - (p1c + p4c + p3c))
            if abs(dif - p2c) == 3 or abs(dif - p2c) == 2:
                print('Risk')
                self.risk2.setVisible(True)
                self.risk2.setText('Risk')
                self.risk2.setGeometry(170, 230, 31, 16)
            elif abs(dif - p2c) == 1 or abs(dif - p2c) == 0:
                print('not risk')
            else:
                print('D.Risk')
                self.risk2.setVisible(True)
                self.risk2.setText('D.Risk')
                self.risk2.setGeometry(170, 230, 41, 16)
            print('difff', dif)
            print('test 3')

        if self.call4.isVisible() and self.p3edit.text() != 'd':
            # p3 risk logic
            dif = abs(13 - (p4c + p2c + p1c))
            if abs(dif - p3c) == 3 or abs(dif - p3c) == 2:
                print('Risk')
                self.risk3.setVisible(True)
                self.risk3.setText('Risk')
                self.risk3.setGeometry(710, 60, 31, 16)
            elif abs(dif - p3c) == 1 or abs(dif - p3c) == 0:
                print('not risk')
            else:
                print('D.Risk')
                self.risk3.setVisible(True)
                self.risk3.setText('D.Risk')
                self.risk3.setGeometry(710, 60, 41, 16)
            print('difff', dif)
            print('test 4')

    def clear_1(self):
        if self.p1edit.text() != '' and self.p1edit.isEnabled():
            self.p1edit.clear()

    def clear_2(self):
        if self.p2edit.text() != '' and self.p2edit.isEnabled():
            self.p2edit.clear()

    def clear_3(self):
        if self.p3edit.text() != '' and self.p3edit.isEnabled():
            self.p3edit.clear()

    def clear_4(self):
        if self.p4edit.text() != '' and self.p4edit.isEnabled():
            self.p4edit.clear()

    def clear_11(self):
        if self.p1result.text() != '':
            self.p1result.clear()

    def clear_12(self):
        if self.p2result.text() != '':
            self.p2result.clear()

    def clear_13(self):
        if self.p3result.text() != '':
            self.p3result.clear()

    def clear_14(self):
        if self.p4result.text() != '':
            self.p4result.clear()

    def ui_update(self):
        if self.p1result.text() != '':
            clickable(self.p1result).connect(self.clear_11)

        if self.p2result.text() != '':
            clickable(self.p2result).connect(self.clear_12)

        if self.p3result.text() != '':
            clickable(self.p3result).connect(self.clear_13)

        if self.p4result.text() != '':
            clickable(self.p4result).connect(self.clear_14)

        if self.p1edit.text() != '':
            self.p2edit.setEnabled(True)
            clickable(self.p1edit).connect(self.clear_1)
        else:
            self.p2edit.setEnabled(False)

        if self.p2edit.text() != '' and self.p2edit.isEnabled():
            self.p3edit.setEnabled(True)
            clickable(self.p2edit).connect(self.clear_2)
        else:
            self.p3edit.setEnabled(False)

        if self.p3edit.text() != '' and self.p3edit.isEnabled():
            self.p4edit.setEnabled(True)
            clickable(self.p3edit).connect(self.clear_3)
        else:
            self.p4edit.setEnabled(False)

        if self.p4edit.text() != '':
            clickable(self.p4edit).connect(self.clear_4)

            if self.p1call.isChecked() and self.p4edit.isEnabled():
                self.call1.setVisible(True)
                if self.call1.isVisible():
                    print('test 111')
                    self.update()

            if self.p2call.isChecked()and self.p4edit.isEnabled():
                self.call2.setVisible(True)
                if self.call2.isVisible():
                    print('test 222')
                    self.update()

            if self.p3call.isChecked()and self.p4edit.isEnabled():
                self.call3.setVisible(True)
                if self.call3.isVisible():
                    print('test 333')
                    self.update()

            if self.p4call.isChecked()and self.p4edit.isEnabled():
                self.call4.setVisible(True)
                if self.call4.isVisible():
                    print('test 444')
                    self.update()
        else:
            self.call1.setVisible(False)
            self.call2.setVisible(False)
            self.call3.setVisible(False)
            self.call4.setVisible(False)

        # calculate button control
        if self.p1edit.text() == '' or self.p2edit.text() == '' or self.p3edit.text() == '' or \
                self.p4edit.text() == '' or self.p1result.text() == '' or self.p2result.text() == '' or \
                self.p3result.text() == '' or self.p4result.text() == '':
            self.calculate_bt.setEnabled(False)
        else:
            self.calculate_bt.setEnabled(True)

        if self.p1edit.text() == '' or self.p2edit.text() == '' or self.p3edit.text() == '' or \
                self.p4edit.text() == '':
            self.call_group.setEnabled(False)
        else:
            self.call_group.setEnabled(True)

    def calculate(self):
        p1in = self.p1edit.text()
        p2in = self.p2edit.text()
        p3in = self.p3edit.text()
        p4in = self.p4edit.text()
        p1result = self.p1result.text()
        p2result = self.p2result.text()
        p3result = self.p3result.text()
        p4result = self.p4result.text()
        ls_sum_in = []
        caller = []
        ls_players = ['p1', 'p2', 'p3', 'p4']
        p1, p2, p3, p4 = [], [], [], []
        winners, losers = [], []
        # checking if input and result values are valid or not
        if not error_input(p1in):
            QMessageBox.warning(self, 'player1 error', 'input must be positive number or dc only')
            p1in = ''
            self.p1edit.clear()
            return
        else:
            if not p1in == 'dc':
                p1in = int(p1in)
                ls_sum_in.append(p1in)
            else:
                ls_sum_in.append(0)

        if not error_input(p2in):
            QMessageBox.warning(self, 'player2 error', 'input must be positive number or dc only')
            p2in = ''
            self.p2edit.clear()
            return
        else:
            if not p2in == 'dc':
                p2in = int(p2in)
                ls_sum_in.append(p2in)
            else:
                ls_sum_in.append(0)

        if not error_input(p3in):
            QMessageBox.warning(self, 'player3 error', 'input must be positive number or dc only')
            p3in = ''
            self.p3edit.clear()
            return
        else:
            if not p3in == 'dc':
                p3in = int(p3in)
                ls_sum_in.append(p3in)
            else:
                ls_sum_in.append(0)

        if not error_input(p4in):
            QMessageBox.warning(self, 'player4 error', 'input must be positive number or dc only')
            p4in = ''
            self.p4edit.clear()
            return
        else:
            if not p4in == 'dc':
                p4in = int(p4in)
                ls_sum_in.append(p4in)
            else:
                ls_sum_in.append(0)

        if not error_input(p1result):
            QMessageBox.warning(self, 'result1 error', 'result must be positive number or dc only')
            p1result = ''
            self.p1result.clear()
            return
        else:
            if not p1result == 'dc':
                p1result = int(p1result)
                p1.append(p1result)
            else:
                p1.append(p1result)

        if not error_input(p2result):
            QMessageBox.warning(self, 'result2 error', 'result must be positive number or dc only')
            p2result = ''
            self.p2result.clear()
            return
        else:
            if not p2result == 'dc':
                p2result = int(p2result)
                p2.append(p2result)
            else:
                p2.append(p2result)

        if not error_input(p3result):
            QMessageBox.warning(self, 'result3 error', 'result must be positive number or dc only')
            p3result = ''
            self.p3result.clear()
            return
        else:
            if not p3result == 'dc':
                p3result = int(p3result)
                p3.append(p3result)
            else:
                p3.append(p3result)

        if not error_input(p4result):
            QMessageBox.warning(self, 'result4 error', 'result must be positive number or dc only')
            p4result = ''
            self.p4result.clear()
            return
        else:
            if not p4result == 'dc':
                p4result = int(p4result)
                p4.append(p4result)
            else:
                p4.append(p4result)

        # No more two Dash calls
        if p1in == 'dc' and p2in == 'dc' and p3in == 'dc':
            QMessageBox.warning(self, 'error', 'no more two dash calls are allowed')
            return
        elif p1in == 'dc' and p2in == 'dc' and p4in == 'dc':
            QMessageBox.warning(self, 'error', 'no more two dash calls are allowed')
            return
        elif p1in == 'dc' and p3in == 'dc' and p4in == 'dc':
            QMessageBox.warning(self, 'error', 'no more two dash calls are allowed')
            return
        elif p2in == 'dc' and p3in == 'dc' and p4in == 'dc':
            QMessageBox.warning(self, 'error', 'no more two dash calls are allowed')
            return
        # doesn't accept dc in result if input not dc
        if not result_dash_call(p1in, p1result):
            QMessageBox.warning(self, 'result 1 error', 'result must be an number not dc')
            self.p1result.clear()
            return
        if not result_dash_call(p2in, p2result):
            QMessageBox.warning(self, 'result 2 error', 'result must be an number not dc')
            self.p2result.clear()
            return
        if not result_dash_call(p3in, p3result):
            QMessageBox.warning(self, 'result 3 error', 'result must be an number not dc')
            self.p3result.clear()
            return
        if not result_dash_call(p4in, p4result):
            QMessageBox.warning(self, 'result 4 error', 'result must be an number not dc')
            self.p4result.clear()
            return

        # make sure that total calls aren't = 13
        if sum(ls_sum_in) == 13:
            QMessageBox.warning(self, 'Call error', 'total calls must be lower or greater than 13')
            return
        else:  # determining game is over or under
            if sum(ls_sum_in) > 13:
                over = True
                under = False
            else:
                over = False
                under = True

        # to determine the right caller
        call = max(ls_sum_in)
        for x, y in zip(ls_sum_in, ls_players):
            if x == call:
                caller.append(y)

        if self.p1call.isChecked() and 'p1' in caller:
            p1.append('call')
        elif self.p1call.isChecked():
            QMessageBox.warning(self, 'call error', 'this player is not allowed to get call')
            return

        if self.p2call.isChecked() and 'p2' in caller:
            p2.append('call')
        elif self.p2call.isChecked():
            QMessageBox.warning(self, 'call error', 'this player is not allowed to get call')
            return

        if self.p3call.isChecked() and 'p3' in caller:
            p3.append('call')
        elif self.p3call.isChecked():
            QMessageBox.warning(self, 'call error', 'this player is not allowed to get call')
            return

        if self.p4call.isChecked() and 'p4' in caller:
            p4.append('call')
        elif self.p4call.isChecked():
            QMessageBox.warning(self, 'call error', 'this player is not allowed to get call')
            return

        # determining who are winners and losers
        if win_lose(p1in, p1result):
            winners.append('p1')
        else:
            losers.append('p1')
        if win_lose(p2in, p2result):
            winners.append('p2')
        else:
            losers.append('p2')
        if win_lose(p3in, p3result):
            winners.append('p3')
        else:
            losers.append('p3')
        if win_lose(p4in, p4result):
            winners.append('p4')
        else:
            losers.append('p4')

        # only win or only lose
        if only_win_lose(winners, losers) or len(winners) == 2:
            if len(winners) < 2 and 'p1' in winners:
                p1.append('only win')
            elif len(winners) < 2 and 'p2' in winners:
                p2.append('only win')
            elif len(winners) < 2 and 'p3' in winners:
                p3.append('only win')
            elif len(winners) < 2 and 'p4' in winners:
                p4.append('only win')
            elif len(losers) < 2 and 'p1' in losers:
                p1.append('only lose')
            elif len(losers) < 2 and 'p2' in losers:
                p2.append('only lose')
            elif len(losers) < 2 and 'p3' in losers:
                p3.append('only lose')
            elif len(losers) < 2 and 'p4' in losers:
                p4.append('only lose')
        elif len(winners) == 4:
            QMessageBox.warning(self, 'error', "all players couldn't win in row")
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No winners, multiplication needed, "
                        "do you want to enable multiplication in the next round?")
            msg.setWindowTitle("error")
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            retrieval = msg.exec_()
            if retrieval == QMessageBox.Yes:
                self.Yes_bt()
            else:
                self.No_bt()
            return

        if self.p1with.isChecked():
            if p1in == call:
                p1.append('with')
            else:
                QMessageBox.warning(self, 'error', "this player can't attempt with")
                self.p1with.setChecked(False)
                return

        if self.p2with.isChecked():
            if p2in == call:
                p2.append('with')
            else:
                QMessageBox.warning(self, 'error', "this player can't attempt with")
                self.p2with.setChecked(False)
                return

        if self.p3with.isChecked():
            if p3in == call:
                p3.append('with')
            else:
                QMessageBox.warning(self, 'error', "this player can't attempt with")
                self.p3with.setChecked(False)
                return

        if self.p4with.isChecked():
            if p4in == call:
                p4.append('with')
            else:
                QMessageBox.warning(self, 'error', "this player can't attempt with")
                self.p4with.setChecked(False)
                return

        # calculation logic starts here

        print(p1, p2, p3, p4)
        self.multi_no.setChecked(False)  # final step

    def Yes_bt(self):
        self.multi_yes.setChecked(True)

    def No_bt(self):
        self.multi_no.setChecked(True)

    def clear(self):
        self.p1edit.setEnabled(True)
        self.p1edit.setFocus(True)
        self.p1edit.clear()
        self.p2edit.clear()
        self.p3edit.clear()
        self.p4edit.clear()
        self.p1result.clear()
        self.p2result.clear()
        self.p3result.clear()
        self.p4result.clear()
        self.p1with.setEnabled(False)
        self.p2with.setEnabled(False)
        self.p3with.setEnabled(False)
        self.p4with.setEnabled(False)
        self.p1with.setChecked(False)
        self.p2with.setChecked(False)
        self.p3with.setChecked(False)
        self.p4with.setChecked(False)
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        self.multi_no.setChecked(False)

    def reset(self):
        self.p1sc.setText('score')
        self.p2sc.setText('Score')
        self.p3sc.setText('score')
        self.p4sc.setText('score')
        self.p1edit.clear()
        self.p2edit.clear()
        self.p3edit.clear()
        self.p4edit.clear()
        self.p1result.clear()
        self.p2result.clear()
        self.p3result.clear()
        self.p4result.clear()
        self.p1with.setEnabled(False)
        self.p2with.setEnabled(False)
        self.p3with.setEnabled(False)
        self.p4with.setEnabled(False)
        self.p1with.setChecked(False)
        self.p2with.setChecked(False)
        self.p3with.setChecked(False)
        self.p4with.setChecked(False)
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        self.multi_no.setChecked(False)


def check_int(num):
    try:
        num=int(num)
        return True
    except:
        return False

def only_win_lose(winners, losers):
    if len(winners) == 1:
        return True
    elif len(losers) == 1:
        return True
    else:
        return False


def win_lose(inp, result):
    if inp == result:
        return True
    else:
        return False


def result_dash_call(inp, result):
    if inp != 'dc' and result == 'dc':
        return False
    else:
        return True


def error_input(variable):
    try:
        variable = int(variable)
        if variable < 0:
            return False
        else:
            return True
    except:
        if variable == 'dc':
            return True
        else:
            variable = ''
            return False


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
