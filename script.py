import os
import sys
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *

UI_File, _ = loadUiType(os.path.join(os.path.dirname('__file__'), "Score Board.ui"))


class MainApp(QMainWindow, UI_File):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui()
        self.actions()

    def ui(self):
        self.setFixedSize(800, 514)
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
        self.multi_label.setVisible(False)

    def actions(self):
        self.reset_bt.clicked.connect(self.reset)
        self.clear_bt.clicked.connect(self.clear)
        self.calculate_bt.clicked.connect(self.calculate)
        # self.risk_yes.toggled.connect(self.ui_update)
        self.p1call.toggled.connect(self.ui_update)
        self.p2call.toggled.connect(self.ui_update)
        self.p3call.toggled.connect(self.ui_update)
        self.p4call.toggled.connect(self.ui_update)
        self.p1call.toggled.connect(self.update)
        self.p2call.toggled.connect(self.update)
        self.p3call.toggled.connect(self.update)
        self.p4call.toggled.connect(self.update)
        # self.double_risk.toggled.connect(self.ui_update)
        self.p1edit.textChanged.connect(self.ui_update)
        self.p2edit.textChanged.connect(self.ui_update)
        self.p3edit.textChanged.connect(self.ui_update)
        self.p4edit.textChanged.connect(self.ui_update)
        self.p1result.textChanged.connect(self.ui_update)
        self.p2result.textChanged.connect(self.ui_update)
        self.p3result.textChanged.connect(self.ui_update)
        self.p4result.textChanged.connect(self.ui_update)

    def update(self):
        p1call = self.p1edit.text()
        p2call = self.p2edit.text()
        p3call, p3test = self.p3edit.text(), self.p3edit.text()
        p4call = self.p4edit.text()
        calls = []

        try:
            p1call = int(self.p1edit.text())
            calls.append(p1call)
        except:
            print('1this is dc or not valid')
        try:
            p2call = int(self.p2edit.text())
            calls.append(p2call)
        except:
            print('2this is dc or not valid')
        try:
            p3call = int(self.p3edit.text())
            calls.append(p3call)
        except:
            print(p3test)
            if p3test == 'dc':
                p3test = 0
                calls.append(p3test)
                print(p3test)
            else:
                QMessageBox.warning(self, 'error', 'not valid value')
                return
            print('3this is dc or not valid')
        try:
            p4call = int(self.p4edit.text())
            calls.append(p4call)
        except:
            print('4this is dc or not valid')

        if self.p1call.isChecked():
            if p1call == max(calls):
                if p4call == 'dc':
                    if p3call == 'dc':
                        if p2call == 'dc':
                            print('sbane5')
                        else:
                            # p2 test
                            dif = abs(13 - p1call)
                            print('difff', dif)
                            print(p1call)
                            print(p2call)
                            print(p3call)
                            print(p4call)
                            if abs(dif - p2call == 2) or abs(dif - p2call == 3):
                                print('1Risk')
                            elif abs(dif - p2call == 1) or abs(dif - p2call == 0):
                                print('1not risk')
                            else:
                                print('1D.Risk')
                    else:
                        # p3 test
                        dif = abs(13 - (p1call + p2call))
                        print('difff', dif)
                        print(p1call)
                        print(p2call)
                        print(p3call)
                        print(p4call)
                        if abs(dif - p3call) == 3 or abs(dif - p3call) == 2:
                            print('2Risk')
                        elif abs(dif - p3call) == 1 or abs(dif - p3call) == 0:
                            print('2no risk')
                        else:
                            print('2D.Risk')
                else:
                    # p4 test
                    if type(p3test) == str:
                        dif = abs(13 - (p1call + p3call + p2call))
                    else:
                        dif = abs(13 - (p1call + p3test + p2call))
                    print('difff', dif)
                    print(p1call)
                    print(p2call)
                    print(p3call)
                    print(p4call)
                    if abs(dif - p4call) == 3 or abs(dif - p4call) == 2:
                        print('3Risk')
                    elif abs(dif - p4call) == 1 or abs(dif - p4call) == 0:
                        print('3not risk')
                    else:
                        print('3D.Risk')

    def ui_update(self):
        # risk and double risk
        '''
        if self.double_risk.isChecked():
            self.risk1.setText('D.Risk')
            self.risk1.setGeometry(170, 60, 41, 16)
            self.risk2.setText('D.Risk')
            self.risk2.setGeometry(170, 230, 41, 16)
            self.risk3.setText('D.Risk')
            self.risk3.setGeometry(710, 60, 41, 16)
            self.risk4.setText('D.Risk')
            self.risk4.setGeometry(710, 230, 41, 16)
        else:
            self.risk1.setText('Risk')
            self.risk1.setGeometry(170, 60, 31, 16)
            self.risk2.setText('Risk')
            self.risk2.setGeometry(170, 230, 31, 16)
            self.risk3.setText('Risk')
            self.risk3.setGeometry(710, 60, 31, 16)
            self.risk4.setText('Risk')
            self.risk4.setGeometry(710, 230, 31, 16)

        # risk checked or not
        if self.risk_yes.isChecked() and self.p1risk.isChecked() and self.p1risk.isEnabled():
            self.risk1.setVisible(True)
        else:
            self.risk1.setVisible(False)
        if self.risk_yes.isChecked() and self.p2risk.isChecked() and self.p2risk.isEnabled():
            self.risk2.setVisible(True)
        else:
            self.risk2.setVisible(False)
        if self.risk_yes.isChecked() and self.p3risk.isChecked() and self.p3risk.isEnabled():
            self.risk3.setVisible(True)
        else:
            self.risk3.setVisible(False)
        if self.risk_yes.isChecked() and self.p4risk.isChecked() and self.p4risk.isEnabled():
            self.risk4.setVisible(True)
        else:
            self.risk4.setVisible(False)
            '''

        # with checked or not
        if self.p1call.isChecked() and (not self.p1with.isEnabled()):
            self.p1with.setChecked(False)
        elif self.p2call.isChecked() and (not self.p2with.isEnabled()):
            self.p2with.setChecked(False)
        elif self.p3call.isChecked() and (not self.p3with.isEnabled()):
            self.p3with.setChecked(False)
        elif self.p4call.isChecked() and (not self.p4with.isEnabled()):
            self.p4with.setChecked(False)
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
            self.p1edit.setText('')
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
            self.p2edit.setText('')
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
            self.p3edit.setText('')
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
            self.p4edit.setText('')
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
            self.p1result.setText('')
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
            self.p2result.setText('')
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
            self.p3result.setText('')
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
            self.p4result.setText('')
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
            self.p1result.setText('')
            return
        if not result_dash_call(p2in, p2result):
            QMessageBox.warning(self, 'result 2 error', 'result must be an number not dc')
            self.p2result.setText('')
            return
        if not result_dash_call(p3in, p3result):
            QMessageBox.warning(self, 'result 3 error', 'result must be an number not dc')
            self.p3result.setText('')
            return
        if not result_dash_call(p4in, p4result):
            QMessageBox.warning(self, 'result 4 error', 'result must be an number not dc')
            self.p4result.setText('')
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

        # knowing who in Risk
        '''
        if self.risk_yes.isChecked() and self.risk1.isVisible():
            if self.risk1.text() == 'Risk':
                p1.append('risk')
            else:
                p1.append('D.Risk')
    
        if self.risk_yes.isChecked() and self.risk2.isVisible():
            if self.risk2.text() == 'Risk':
                p2.append('risk')
            else:
                p2.append('D.Risk')
    
        if self.risk_yes.isChecked() and self.risk3.isVisible():
            if self.risk3.text() == 'Risk':
                p3.append('risk')
            else:
                p3.append('D.Risk')
    
        if self.risk_yes.isChecked() and self.risk4.isVisible():
            if self.risk4.text() == 'Risk':
                p4.append('risk')
            else:
                p4.append('D.Risk')
        '''
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
        self.p1edit.setText('')
        self.p2edit.setText('')
        self.p3edit.setText('')
        self.p4edit.setText('')
        self.p1result.setText('')
        self.p2result.setText('')
        self.p3result.setText('')
        self.p4result.setText('')
        self.multi_no.setChecked(False)

    def reset(self):
        self.p1sc.setText('score')
        self.p2sc.setText('Score')
        self.p3sc.setText('score')
        self.p4sc.setText('score')
        self.p1edit.setText('')
        self.p2edit.setText('')
        self.p3edit.setText('')
        self.p4edit.setText('')
        self.p1result.setText('')
        self.p2result.setText('')
        self.p3result.setText('')
        self.p4result.setText('')
        self.multi_no.setChecked(False)


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
