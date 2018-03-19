import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *

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

        self.dc1.toggled.connect(self.dash_call1)
        self.dc2.toggled.connect(self.dash_call2)
        self.dc3.toggled.connect(self.dash_call3)
        self.dc4.toggled.connect(self.dash_call4)

        self.dc11.toggled.connect(self.ui_update)
        self.dc12.toggled.connect(self.ui_update)
        self.dc13.toggled.connect(self.ui_update)
        self.dc14.toggled.connect(self.ui_update)

        self.p1edit.textChanged.connect(self.edit1)
        self.p2edit.textChanged.connect(self.edit2)
        self.p3edit.textChanged.connect(self.edit3)
        self.p4edit.textChanged.connect(self.edit4)

        self.p1result.textChanged.connect(self.result1)
        self.p2result.textChanged.connect(self.result2)
        self.p3result.textChanged.connect(self.result3)
        self.p4result.textChanged.connect(self.result4)

    def dash_call(self):
        if (self.dc1.isChecked() or self.p1edit.text() == '0') and (self.dc2.isChecked() or self.p2edit.text() == '0'):
            self.dc3.setEnabled(False)
            self.dc4.setEnabled(False)
            #self.p1edit.setEnabled(False)
            #self.p2edit.setEnabled(False)
            return True
        else:
            print('here')
            if self.p3edit.text() == '':
                self.dc3.setEnabled(True)
            if self.p4edit.text() == '':
                self.dc4.setEnabled(True)
            #self.p1edit.setEnabled(True)
            #self.p2edit.setEnabled(True)

            if (self.dc1.isChecked() or self.p1edit.text() == '0') and \
                    (self.dc3.isChecked() or self.p3edit.text() == '0'):
                self.dc2.setEnabled(False)
                self.dc4.setEnabled(False)
                #self.p1edit.setEnabled(False)
                #self.p3edit.setEnabled(False)
                return True
            else:
                if self.p2edit.text() == '':
                    self.dc2.setEnabled(True)
                if self.p4edit.text() == '':
                    self.dc4.setEnabled(True)
                print('here1')
                #self.p1edit.setEnabled(True)
                #self.p3edit.setEnabled(True)

                if (self.dc1.isChecked() or self.p1edit.text() == '0') and \
                        (self.dc4.isChecked() or self.p4edit.text() == '0'):
                    self.dc2.setEnabled(False)
                    self.dc3.setEnabled(False)
                    #self.p1edit.setEnabled(False)
                    #self.p4edit.setEnabled(False)
                    return True
                else:
                    print('here2')
                    if self.p2edit.text() == '':
                        self.dc2.setEnabled(True)
                    if self.p3edit.text() == '':
                        self.dc3.setEnabled(True)
                    #self.p1edit.setEnabled(True)
                    #self.p4edit.setEnabled(True)

                    if (self.dc2.isChecked() or self.p2edit.text() == '0') and \
                            (self.dc3.isChecked() or self.p3edit.text() == '0'):
                        self.dc1.setEnabled(False)
                        self.dc4.setEnabled(False)
                        #self.p2edit.setEnabled(False)
                        #self.p3edit.setEnabled(False)
                        return True
                    else:
                        print('here3')
                        if self.p1edit.text()=='':
                            self.dc1.setEnabled(True)
                        if self.p4edit.text() == '':
                            self.dc4.setEnabled(True)
                        #self.p2edit.setEnabled(True)
                        #self.p3edit.setEnabled(True)

                        if (self.dc2.isChecked() or self.p2edit.text() == '0') and \
                                (self.dc4.isChecked() or self.p4edit.text() == '0'):
                            self.dc1.setEnabled(False)
                            self.dc3.setEnabled(False)
                            #self.p2edit.setEnabled(False)
                            #self.p4edit.setEnabled(False)
                            return True
                        else:
                            print('here4')
                            if self.p1edit.text() == '':
                                self.dc1.setEnabled(True)
                            if self.p3edit.text() == '':
                                self.dc3.setEnabled(True)
                            #self.p2edit.setEnabled(True)
                            #self.p4edit.setEnabled(True)

                            if (self.dc3.isChecked() or self.p3edit.text() == '0') and \
                                    (self.dc4.isChecked() or self.p4edit.text() == '0'):
                                self.dc1.setEnabled(False)
                                self.dc2.setEnabled(False)
                                #self.p3edit.setEnabled(False)
                                #self.p4edit.setEnabled(False)
                                return True
                            else:
                                print('here5')
                                if self.p1edit.text() == '':
                                    self.dc1.setEnabled(True)
                                if self.p2edit.text() == '':
                                    self.dc2.setEnabled(True)
                                #self.p3edit.setEnabled(True)
                                #self.p4edit.setEnabled(True)
                                return False

    def dash_call1(self):
        self.dash_call()
        if self.dc1.isChecked():
            if self.p1result.text()=='0':
                self.p1result.clear()
            self.p1edit.setEnabled(False)
            self.p1edit.clear()
            self.p2edit.setFocus(True)
        else:
            self.p1edit.setEnabled(True)
            self.p1edit.setFocus(True)
            if self.dc11.isChecked():
                self.dc11.setChecked(False)
        self.ui_update()

    def dash_call2(self):
        self.dash_call()
        if self.dc2.isChecked():
            if self.p2result.text()=='0':
                self.p2result.clear()
            self.p2edit.setEnabled(False)
            self.p2edit.clear()
            self.p3edit.setFocus(True)
        else:
            self.p2edit.setEnabled(True)
            self.p2edit.setFocus(True)
            if self.dc12.isChecked():
                self.dc12.setChecked(False)
        self.ui_update()

    def dash_call3(self):
        self.dash_call()
        if self.dc3.isChecked():
            if self.p3result.text()=='0':
                self.p3result.clear()
            self.p3edit.setEnabled(False)
            self.p3edit.clear()
            self.p4edit.setFocus(True)
        else:
            self.p3edit.setEnabled(True)
            self.p3edit.setFocus(True)
            if self.dc13.isChecked():
                self.dc13.setChecked(False)
        self.ui_update()

    def dash_call4(self):
        self.dash_call()
        if self.dc4.isChecked():
            if self.p4result.text()=='0':
                self.p4result.clear()
            self.p4edit.setEnabled(False)
            self.p4edit.clear()
            self.p1result.setFocus(True)
        else:
            self.p4edit.setEnabled(True)
            self.p4edit.setFocus(True)
            if self.dc14.isChecked():
                self.dc14.setChecked(False)
        self.ui_update()

    def risk_update1(self):
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        # p4 risk logic by default
        if self.dc4.isChecked():
            if self.dc3.isChecked():
                # p2 risk logic
                if risk(p2c, p1c, p3c, p4c) == 1:
                    self.risk2.setVisible(True)
                    self.risk2.setText('Risk')
                    self.risk2.setGeometry(170, 230, 31, 16)
                elif risk(p2c, p1c, p3c, p4c) == 2:
                    self.risk2.setVisible(True)
                    self.risk2.setText('D.Risk')
                    self.risk2.setGeometry(170, 230, 41, 16)
            else:
                # p3 risk logic
                if risk(p3c, p1c, p2c, p4c) == 1:
                    self.risk3.setVisible(True)
                    self.risk3.setText('Risk')
                    self.risk3.setGeometry(710, 60, 31, 16)
                elif risk(p3c, p1c, p2c, p4c) == 2:
                    self.risk3.setVisible(True)
                    self.risk3.setText('D.Risk')
                    self.risk3.setGeometry(710, 60, 41, 16)
        else:
            # p4 risk logic
            if risk(p4c, p3c, p2c, p1c) == 1:
                self.risk4.setVisible(True)
                self.risk4.setText('Risk')
                self.risk4.setGeometry(710, 230, 31, 16)
            elif risk(p4c, p3c, p2c, p1c) == 2:
                self.risk4.setVisible(True)
                self.risk4.setText('D.Risk')
                self.risk4.setGeometry(710, 230, 41, 16)

    def risk_update2(self):
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        # p1 risk logic by default
        if self.dc1.isChecked():
            if self.dc4.isChecked():
                # p3 risk logic
                if risk(p3c, p1c, p2c, p4c) == 1:
                    self.risk3.setVisible(True)
                    self.risk3.setText('Risk')
                    self.risk3.setGeometry(710, 60, 31, 16)
                elif risk(p3c, p1c, p2c, p4c) == 2:
                    self.risk3.setVisible(True)
                    self.risk3.setText('D.Risk')
                    self.risk3.setGeometry(710, 60, 41, 16)
            else:
                # p4 risk logic
                if risk(p4c, p3c, p2c, p1c) == 1:
                    self.risk4.setVisible(True)
                    self.risk4.setText('Risk')
                    self.risk4.setGeometry(710, 230, 31, 16)
                elif risk(p4c, p3c, p2c, p1c) == 2:
                    self.risk4.setVisible(True)
                    self.risk4.setText('D.Risk')
                    self.risk4.setGeometry(710, 230, 41, 16)
        else:
            # p1 risk logic
            if risk(p1c, p2c, p3c, p4c) == 1:
                self.risk1.setVisible(True)
                self.risk1.setText('Risk')
                self.risk1.setGeometry(170, 60, 31, 16)
            elif risk(p1c, p2c, p3c, p4c) == 2:
                self.risk1.setVisible(True)
                self.risk1.setText('D.Risk')
                self.risk1.setGeometry(170, 60, 41, 16)

    def risk_update3(self):
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        # p2 risk logic by default
        if self.dc2.isChecked():
            if self.dc1.isChecked():
                # p4 risk logic
                if risk(p4c, p3c, p2c, p1c) == 1:
                    self.risk4.setVisible(True)
                    self.risk4.setText('Risk')
                    self.risk4.setGeometry(710, 230, 31, 16)
                elif risk(p4c, p3c, p2c, p1c) == 2:
                    self.risk4.setVisible(True)
                    self.risk4.setText('D.Risk')
                    self.risk4.setGeometry(710, 230, 41, 16)
            else:
                # p1 risk logic
                if risk(p1c, p2c, p3c, p4c) == 1:
                    self.risk1.setVisible(True)
                    self.risk1.setText('Risk')
                    self.risk1.setGeometry(170, 60, 31, 16)
                elif risk(p1c, p2c, p3c, p4c) == 2:
                    self.risk1.setVisible(True)
                    self.risk1.setText('D.Risk')
                    self.risk1.setGeometry(170, 60, 41, 16)
        else:
            # p2 risk logic
            if risk(p2c, p1c, p3c, p4c) == 1:
                self.risk2.setVisible(True)
                self.risk2.setText('Risk')
                self.risk2.setGeometry(170, 230, 31, 16)
            elif risk(p2c, p1c, p3c, p4c) == 2:
                self.risk2.setVisible(True)
                self.risk2.setText('D.Risk')
                self.risk2.setGeometry(170, 230, 41, 16)

    def risk_update4(self):
        self.risk1.setVisible(False)
        self.risk2.setVisible(False)
        self.risk3.setVisible(False)
        self.risk4.setVisible(False)
        # p3 risk logic by default
        if self.dc3.isChecked():
            if self.dc2.isChecked():
                # p1 risk logic
                if risk(p1c, p2c, p3c, p4c) == 1:
                    self.risk1.setVisible(True)
                    self.risk1.setText('Risk')
                    self.risk1.setGeometry(170, 60, 31, 16)
                elif risk(p1c, p2c, p3c, p4c) == 2:
                    self.risk1.setVisible(True)
                    self.risk1.setText('D.Risk')
                    self.risk1.setGeometry(170, 60, 41, 16)
            else:
                # p2 risk logic
                if risk(p2c, p1c, p3c, p4c) == 1:
                    self.risk2.setVisible(True)
                    self.risk2.setText('Risk')
                    self.risk2.setGeometry(170, 230, 31, 16)
                elif risk(p2c, p1c, p3c, p4c) == 2:
                    self.risk2.setVisible(True)
                    self.risk2.setText('D.Risk')
                    self.risk2.setGeometry(170, 230, 41, 16)
        else:
            # p3 risk logic
            if risk(p3c, p1c, p2c, p4c) == 1:
                self.risk3.setVisible(True)
                self.risk3.setText('Risk')
                self.risk3.setGeometry(710, 60, 31, 16)
            elif risk(p3c, p1c, p2c, p4c) == 2:
                self.risk3.setVisible(True)
                self.risk3.setText('D.Risk')
                self.risk3.setGeometry(710, 60, 41, 16)

    def with_update(self):
        if self.p1call.isEnabled():
            # self.p1with.setEnabled(True)
            # self.p1with.setChecked(True)
            if self.p1call.isChecked():
                self.p1with.setEnabled(False)
                self.p1with.setChecked(False)
                self.p1call.toggled.connect(self.risk_update1)
            else:
                self.p1with.setEnabled(True)
                self.p1with.setChecked(True)

        if self.p2call.isEnabled():
            # self.p2with.setEnabled(True)
            # self.p2with.setChecked(True)
            if self.p2call.isChecked():
                self.p2with.setEnabled(False)
                self.p2with.setChecked(False)
                self.p2call.toggled.connect(self.risk_update2)
            else:
                self.p2with.setEnabled(True)
                self.p2with.setChecked(True)

        if self.p3call.isEnabled():
            # self.p3with.setEnabled(True)
            # self.p3with.setChecked(True)
            if self.p3call.isChecked():
                self.p3with.setEnabled(False)
                self.p3with.setChecked(False)
                self.p3call.toggled.connect(self.risk_update3)
            else:
                self.p3with.setEnabled(True)
                self.p3with.setChecked(True)

        if self.p4call.isEnabled():
            # self.p4with.setEnabled(True)
            # self.p4with.setChecked(True)
            if self.p4call.isChecked():
                self.p4with.setEnabled(False)
                self.p4with.setChecked(False)
                self.p4call.toggled.connect(self.risk_update4)
            else:
                self.p4with.setEnabled(True)
                self.p4with.setChecked(True)

    def update(self):
        global p1c, p2c, p3c, p4c
        p1c = self.p1edit.text()
        p2c = self.p2edit.text()
        p3c = self.p3edit.text()
        p4c = self.p4edit.text()
        calls = []
        ls_players = ['p1','p2','p3','p4']
        caller = []

        if self.dc1.isChecked():
            p1c=0
            calls.append(0)
        else:
            p1c=int(p1c)
            calls.append(p1c)

        if self.dc2.isChecked():
            p2c=0
            calls.append(p2c)
        else:
            p2c = int(p2c)
            calls.append(p2c)

        if self.dc3.isChecked():
            p3c=0
            calls.append(p3c)
        else:
            p3c = int(p3c)
            calls.append(p3c)

        if self.dc4.isChecked():
            p4c=0
            calls.append(p4c)
        else:
            p4c = int(p4c)
            calls.append(p4c)

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
            #self.p1edit.setEnabled(False)
            #self.p2edit.setEnabled(False)
            #self.p3edit.setEnabled(False)
            #self.p4edit.setEnabled(False)

            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)

            #self.p1result.setFocus(True)
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
                self.p1call.setChecked(False)
                self.p2call.setChecked(False)
                self.p4call.setChecked(False)
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
            #self.p1edit.setEnabled(False)
            #self.p2edit.setEnabled(False)
            #self.p3edit.setEnabled(False)
            #self.p4edit.setEnabled(False)

            #self.p1result.setFocus(True)

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
                self.p1call.toggled.connect(self.with_update)
                if self.p1call.isChecked():
                    self.p1with.setEnabled(False)
                    self.risk1.setVisible(False)
                else:
                    self.p1with.setEnabled(True)
                    self.p1with.setChecked(True)

            if 'p2' in caller:
                self.p2call.toggled.connect(self.with_update)
                if self.p2call.isChecked():
                    self.p2with.setEnabled(False)
                    self.risk2.setVisible(False)
                else:
                    self.p2with.setEnabled(True)
                    self.p2with.setChecked(True)

            if 'p3' in caller:
                self.p3call.toggled.connect(self.with_update)
                if self.p3call.isChecked():
                    self.p3with.setEnabled(False)
                    self.risk3.setVisible(False)
                else:
                    self.p3with.setEnabled(True)
                    self.p3with.setChecked(True)

            if 'p4' in caller:
                self.p4call.toggled.connect(self.with_update)
                if self.p4call.isChecked():
                    self.p4with.setEnabled(False)
                    self.risk4.setVisible(False)
                else:
                    self.p4with.setEnabled(True)
                    self.p4with.setChecked(True)

        print(caller)
        print('calls list',calls)
        print(p1c, p2c, p3c, p4c)

        if self.call1.isVisible():
            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)
            # p4 risk logic by default
            if self.dc4.isChecked():
                if self.dc3.isChecked():
                    # p2 risk logic
                    if risk(p2c, p1c, p3c, p4c) == 1:
                        self.risk2.setVisible(True)
                        self.risk2.setText('Risk')
                        self.risk2.setGeometry(170, 230, 31, 16)
                    elif risk(p2c, p1c, p3c, p4c) == 2:
                        self.risk2.setVisible(True)
                        self.risk2.setText('D.Risk')
                        self.risk2.setGeometry(170, 230, 41, 16)
                else:
                    # p3 risk logic
                    if risk(p3c, p1c, p2c, p4c) == 1:
                        self.risk3.setVisible(True)
                        self.risk3.setText('Risk')
                        self.risk3.setGeometry(710, 60, 31, 16)
                    elif risk(p3c, p1c, p2c, p4c) == 2:
                        self.risk3.setVisible(True)
                        self.risk3.setText('D.Risk')
                        self.risk3.setGeometry(710, 60, 41, 16)
            else:
                # p4 risk logic
                if risk(p4c,p3c,p2c,p1c) == 1:
                    self.risk4.setVisible(True)
                    self.risk4.setText('Risk')
                    self.risk4.setGeometry(710, 230, 31, 16)
                elif risk(p4c,p3c,p2c,p1c) == 2:
                    self.risk4.setVisible(True)
                    self.risk4.setText('D.Risk')
                    self.risk4.setGeometry(710, 230, 41, 16)
            print('test 1')

        if self.call2.isVisible():
            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)
            # p1 risk logic by default
            if self.dc1.isChecked():
                if self.dc4.isChecked():
                    # p3 risk logic
                    if risk(p3c, p1c, p2c, p4c) == 1:
                        self.risk3.setVisible(True)
                        self.risk3.setText('Risk')
                        self.risk3.setGeometry(710, 60, 31, 16)
                    elif risk(p3c, p1c, p2c, p4c) == 2:
                        self.risk3.setVisible(True)
                        self.risk3.setText('D.Risk')
                        self.risk3.setGeometry(710, 60, 41, 16)
                else:
                    # p4 risk logic
                    if risk(p4c, p3c, p2c, p1c) == 1:
                        self.risk4.setVisible(True)
                        self.risk4.setText('Risk')
                        self.risk4.setGeometry(710, 230, 31, 16)
                    elif risk(p4c, p3c, p2c, p1c) == 2:
                        self.risk4.setVisible(True)
                        self.risk4.setText('D.Risk')
                        self.risk4.setGeometry(710, 230, 41, 16)
            else:
                # p1 risk logic
                if risk(p1c,p2c,p3c,p4c) == 1:
                    self.risk1.setVisible(True)
                    self.risk1.setText('Risk')
                    self.risk1.setGeometry(170, 60, 31, 16)
                elif risk(p1c,p2c,p3c,p4c) == 2:
                    self.risk1.setVisible(True)
                    self.risk1.setText('D.Risk')
                    self.risk1.setGeometry(170, 60, 41, 16)
            print('test 2')

        if self.call3.isVisible():
            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)
            # p2 risk logic by default
            if self.dc2.isChecked():
                if self.dc1.isChecked():
                    # p4 risk logic
                    if risk(p4c, p3c, p2c, p1c) == 1:
                        self.risk4.setVisible(True)
                        self.risk4.setText('Risk')
                        self.risk4.setGeometry(710, 230, 31, 16)
                    elif risk(p4c, p3c, p2c, p1c) == 2:
                        self.risk4.setVisible(True)
                        self.risk4.setText('D.Risk')
                        self.risk4.setGeometry(710, 230, 41, 16)
                else:
                    # p1 risk logic
                    if risk(p1c, p2c, p3c, p4c) == 1:
                        self.risk1.setVisible(True)
                        self.risk1.setText('Risk')
                        self.risk1.setGeometry(170, 60, 31, 16)
                    elif risk(p1c, p2c, p3c, p4c) == 2:
                        self.risk1.setVisible(True)
                        self.risk1.setText('D.Risk')
                        self.risk1.setGeometry(170, 60, 41, 16)
            else:
                # p2 risk logic
                if risk(p2c,p1c,p3c,p4c) == 1:
                    self.risk2.setVisible(True)
                    self.risk2.setText('Risk')
                    self.risk2.setGeometry(170, 230, 31, 16)
                elif risk(p2c,p1c,p3c,p4c) == 2:
                    self.risk2.setVisible(True)
                    self.risk2.setText('D.Risk')
                    self.risk2.setGeometry(170, 230, 41, 16)
            print('test 3')

        if self.call4.isVisible():
            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)
            # p3 risk logic by default
            if self.dc3.isChecked():
                if self.dc2.isChecked():
                    # p1 risk logic
                    if risk(p1c, p2c, p3c, p4c) == 1:
                        self.risk1.setVisible(True)
                        self.risk1.setText('Risk')
                        self.risk1.setGeometry(170, 60, 31, 16)
                    elif risk(p1c, p2c, p3c, p4c) == 2:
                        self.risk1.setVisible(True)
                        self.risk1.setText('D.Risk')
                        self.risk1.setGeometry(170, 60, 41, 16)
                else:
                    # p2 risk logic
                    if risk(p2c, p1c, p3c, p4c) == 1:
                        self.risk2.setVisible(True)
                        self.risk2.setText('Risk')
                        self.risk2.setGeometry(170, 230, 31, 16)
                    elif risk(p2c, p1c, p3c, p4c) == 2:
                        self.risk2.setVisible(True)
                        self.risk2.setText('D.Risk')
                        self.risk2.setGeometry(170, 230, 41, 16)
            else:
                # p3 risk logic
                if risk(p3c,p1c,p2c,p4c) == 1:
                    self.risk3.setVisible(True)
                    self.risk3.setText('Risk')
                    self.risk3.setGeometry(710, 60, 31, 16)
                elif risk(p3c,p1c,p2c,p4c) == 2:
                    self.risk3.setVisible(True)
                    self.risk3.setText('D.Risk')
                    self.risk3.setGeometry(710, 60, 41, 16)
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
        if self.p1result.text() != '' and self.p1result.isEnabled():
            self.p1result.clear()

    def clear_12(self):
        if self.p2result.text() != '' and self.p2result.isEnabled():
            self.p2result.clear()

    def clear_13(self):
        if self.p3result.text() != '' and self.p3result.isEnabled():
            self.p3result.clear()

    def clear_14(self):
        if self.p4result.text() != '' and self.p4result.isEnabled():
            self.p4result.clear()

    def edit1(self):
        self.dash_call()
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p1edit.text() not in prob:
            self.p1edit.clear()

        if self.p1edit.text() != '':
            self.dc1.setEnabled(False)
            clickable(self.p1edit).connect(self.clear_1)
        else:
            if self.dash_call():
                self.dc1.setEnabled(False)
            else:
                self.dc1.setEnabled(True)
        self.ui_update()

    def edit2(self):
        self.dash_call()
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p2edit.text() not in prob:
            self.p2edit.clear()

        if self.p2edit.text() != '':
            self.dc2.setEnabled(False)
            clickable(self.p2edit).connect(self.clear_2)
        else:
            if self.dash_call():
                self.dc2.setEnabled(False)
            else:
                self.dc2.setEnabled(True)
        self.ui_update()

    def edit3(self):
        self.dash_call()
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p3edit.text() not in prob:
            self.p3edit.clear()

        if self.p3edit.text() != '':
            self.dc3.setEnabled(False)
            clickable(self.p3edit).connect(self.clear_3)
        else:
            if self.dash_call():
                self.dc3.setEnabled(False)
            else:
                self.dc3.setEnabled(True)
        self.ui_update()

    def edit4(self):
        self.dash_call()
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p4edit.text() not in prob:
            self.p4edit.clear()

        if self.p4edit.text() != '':
            self.dc4.setEnabled(False)
            clickable(self.p4edit).connect(self.clear_4)
        else:
            if self.dash_call():
                self.dc4.setEnabled(False)
            else:
                self.dc4.setEnabled(True)
        self.ui_update()

    def result1(self):
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p1result.text() == '0' and self.dc1.isChecked():
            self.p1result.clear()

        if self.p1result.text() not in prob:
            self.p1result.clear()

        if self.p1result.text()!='':
            clickable(self.p1result).connect(self.clear_11)
        self.ui_update()

    def result2(self):
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p2result.text() == '0' and self.dc2.isChecked():
            self.p2result.clear()

        if self.p2result.text() not in prob:
            self.p2result.clear()

        if self.p2result.text()!='':
            clickable(self.p2result).connect(self.clear_12)
        self.ui_update()

    def result3(self):
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p3result.text() == '0' and self.dc3.isChecked():
            self.p3result.clear()

        if self.p3result.text() not in prob:
            self.p3result.clear()

        if self.p3result.text()!='':
            clickable(self.p3result).connect(self.clear_13)
        self.ui_update()

    def result4(self):
        prob = []
        for i in range(13):
            prob.append(str(i))

        if self.p4result.text() == '0' and self.dc4.isChecked():
            self.p4result.clear()

        if self.p4result.text() not in prob:
            self.p4result.clear()

        if self.p4result.text()!='':
            clickable(self.p4result).connect(self.clear_14)
        self.ui_update()

    def ui_update(self):
        if (self.p1edit.text() != '' or self.dc1.isChecked()) and (self.p2edit.text() != '' or self.dc2.isChecked())\
                and (self.p3edit.text() != '' or self.dc3.isChecked()) and \
                (self.p4edit.text() != '' or self.dc4.isChecked()):
            print('True')
            self.call_group.setEnabled(True)
            if self.p1call.isChecked():
                self.call1.setVisible(True)
                if self.call1.isVisible():
                    print('test 111')
                    self.update()

            if self.p2call.isChecked():
                self.call2.setVisible(True)
                if self.call2.isVisible():
                    print('test 222')
                    self.update()

            if self.p3call.isChecked():
                self.call3.setVisible(True)
                if self.call3.isVisible():
                    print('test 333')
                    self.update()

            if self.p4call.isChecked():
                self.call4.setVisible(True)
                if self.call4.isVisible():
                    print('test 444')
                    self.update()
        else:
            print('false')
            self.call1.setVisible(False)
            self.call2.setVisible(False)
            self.call3.setVisible(False)
            self.call4.setVisible(False)

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

            self.call_group.setEnabled(False)
            return

        # calculate button control
        if (self.p1edit.text()!='' or self.dc1.isChecked()) and (self.p2edit.text()!='' or self.dc2.isChecked())\
                and (self.p3edit.text()!='' or self.dc3.isChecked()) and \
                (self.p4edit.text()!='' or self.dc4.isChecked())\
                and (self.p1result.text() != '' or self.dc11.isChecked()) and \
                (self.p2result.text() != '' or self.dc12.isChecked())\
                and (self.p3result.text() != '' or self.dc13.isChecked()) and \
                (self.p4result.text() != '' or self.dc14.isChecked()):

            self.calculate_bt.setEnabled(True)
        else:
            self.calculate_bt.setEnabled(False)

    def calculate(self):
        p1in = self.p1edit.text()
        p2in = self.p2edit.text()
        p3in = self.p3edit.text()
        p4in = self.p4edit.text()
        p1result = self.p1result.text()
        p2result = self.p2result.text()
        p3result = self.p3result.text()
        p4result = self.p4result.text()
        p1sc = self.p1sc.text()
        p2sc = self.p2sc.text()
        p3sc = self.p3sc.text()
        p4sc = self.p4sc.text()
        p1round = p2round = p3round = p4round = 0
        ls_sum_in = []
        p1, p2, p3, p4 = [], [], [], []
        winners, losers = [], []

        if not self.dc11.isChecked():
            p1result = int(p1result)
            p1.append(p1result)

        if not self.dc12.isChecked():
            p2result=int(p2result)
            p2.append(p2result)

        if not self.dc13.isChecked():
            p3result = int(p3result)
            p3.append(p3result)

        if not self.dc14.isChecked():
            p4result = int(p4result)
            p4.append(p4result)

        if self.dc1.isChecked():
            p1.append('dash call')
            if self.dc11.isChecked():
                winners.append('p1')
            else:
                losers.append('p1')
            p1in=0
        else:
            p1in = int(p1in)
            if win_lose(p1in, p1result):
                winners.append('p1')
            else:
                losers.append('p1')

        if self.dc2.isChecked():
            p2.append('dash call')
            if self.dc12.isChecked():
                winners.append('p2')
            else:
                losers.append('p2')
            p2in=0
        else:
            p2in = int(p2in)
            if win_lose(p2in, p2result):
                winners.append('p2')
            else:
                losers.append('p2')

        if self.dc3.isChecked():
            p3.append('dash call')
            if self.dc13.isChecked():
                winners.append('p3')
            else:
                losers.append('p3')
            p3in=0
        else:
            p3in = int(p3in)
            if win_lose(p3in, p3result):
                winners.append('p3')
            else:
                losers.append('p3')

        if self.dc4.isChecked():
            p4.append('dash call')
            if self.dc14.isChecked():
                winners.append('p4')
            else:
                losers.append('p4')
            p4in=0
        else:
            p4in = int(p4in)
            if win_lose(p4in, p4result):
                winners.append('p4')
            else:
                losers.append('p4')

        # checking if call over or under
        ls_sum_in.append(p1in)
        ls_sum_in.append(p2in)
        ls_sum_in.append(p3in)
        ls_sum_in.append(p4in)
        if sum(ls_sum_in) > 13:
            print('over')
            over = True
            under = False
        else:
            print('under')
            over = False
            under = True

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

        if self.call1.isVisible():
            p1.append('call')
        elif self.call2.isVisible():
            p2.append('call')
        elif self.call3.isVisible():
            p3.append('call')
        elif self.call4.isVisible():
            p4.append('call')

        if self.with1.isVisible():
            p1.append('with')
        if self.with2.isVisible():
            p2.append('with')
        if self.with3.isVisible():
            p3.append('with')
        if self.with4.isVisible():
            p4.append('with')

        if self.risk1.isVisible():
            if self.risk1.text()=='Risk':
                p1.append('risk')
            else:
                p1.append('d.risk')
        elif self.risk2.isVisible():
            if self.risk2.text()=='Risk':
                p2.append('risk')
            else:
                p2.append('d.risk')
        elif self.risk3.isVisible():
            if self.risk3.text()=='Risk':
                p3.append('risk')
            else:
                p3.append('d.risk')
        elif self.risk4.isVisible():
            if self.risk4.text()=='Risk':
                p4.append('risk')
            else:
                p4.append('d.risk')

        if self.p1sc.text() == 'Score':
            p1sc = 0
            p1sc = int(p1sc)
        else:
            p1sc = int(p1sc)

        if self.p2sc.text() == 'Score':
            p2sc = 0
            p2sc = int(p2sc)
        else:
            p2sc = int(p2sc)

        if self.p3sc.text() == 'Score':
            p3sc = 0
            p3sc = int(p3sc)
        else:
            p3sc = int(p3sc)

        if self.p4sc.text() == 'Score':
            p4sc = 0
            p4sc = int(p4sc)
        else:
            p4sc = int(p4sc)

        # calculation logic starts here
        # p1 score
        if 'p1' in winners:
            p1round += p1result
        else:
            p1round -= abs(p1in-p1result)

        if 'call' in p1:
            if 'p1' in winners:
                p1round += 20
            else:
                p1round -= 10
        if 'dash call' in p1:
            if 'p1' in winners:
                p1round += 23
            else:
                p1round -= 23
        if 'with' and 'risk' in p1:
            if 'p1' in winners:
                p1round += 30
            else:
                p1round -= 20
        elif 'with' and 'd.risk' in p1:
            if 'p1' in winners:
                p1round += 40
            else:
                p1round -= 30
        else:
            if 'with' in p1:
                if 'p1' in winners:
                    p1round += 20
                else:
                    p1round -= 10

            if 'risk' in p1:
                if 'p1' in winners:
                    p1round += 20
                else:
                    p1round -= 10
            elif 'd.risk' in p1:
                if 'p1' in winners:
                    p1round += 30
                else:
                    p1round -= 20

        if 'only win' in p1:
            p1round += 10

        if 'only lose' in p1:
            p1round -= 10

        if (('p1' in winners) and (0 in p1) and under) or (('p1' in losers) and (0 in p1) and over):
            p1round += 10

        for lopper in [8,9,10,11,12]:
            if lopper in p1:
                p1round *= 2

        # p2 score
        if 'p2' in winners:
            p2round += p2result
        else:
            p2round -= abs(p2in-p2result)

        if 'call' in p2:
            if 'p2' in winners:
                p2round += 20
            else:
                p2round -= 10
        if 'dash call' in p2:
            if 'p2' in winners:
                p2round += 23
            else:
                p2round -= 23
        if 'with' and 'risk' in p2:
            if 'p2' in winners:
                p2round += 30
            else:
                p2round -= 20
        elif 'with' and 'd.risk' in p2:
            if 'p2' in winners:
                p2round += 40
            else:
                p2round -= 30
        else:
            if 'with' in p2:
                if 'p2' in winners:
                    p2round += 20
                else:
                    p2round -= 10

            if 'risk' in p2:
                if 'p2' in winners:
                    p2round += 20
                else:
                    p2round -= 10
            elif 'd.risk' in p2:
                if 'p2' in winners:
                    p2round += 30
                else:
                    p2round -= 20

        if 'only win' in p2:
            p2round += 10

        if 'only lose' in p2:
            p2round -= 10

        if (('p2' in winners) and (0 in p2) and under) or (('p2' in losers) and (0 in p2) and over):
            p2round += 10

        for lopper in [8,9,10,11,12]:
            if lopper in p2:
                p2round *= 2

        # p3 score
        if 'p3' in winners:
            p3round += p3result
        else:
            p3round -= abs(p3in - p3result)

        if 'call' in p3:
            if 'p3' in winners:
                p3round += 20
            else:
                p3round -= 10
        if 'dash call' in p3:
            if 'p3' in winners:
                p3round += 23
            else:
                p3round -= 23
        if 'with' and 'risk' in p3:
            if 'p3' in winners:
                p3round += 30
            else:
                p3round -= 20
        elif 'with' and 'd.risk' in p3:
            if 'p3' in winners:
                p3round += 40
            else:
                p3round -= 30
        else:
            if 'with' in p3:
                if 'p3' in winners:
                    p3round += 20
                else:
                    p3round -= 10

            if 'risk' in p3:
                if 'p3' in winners:
                    p3round += 20
                else:
                    p3round -= 10
            elif 'd.risk' in p3:
                if 'p3' in winners:
                    p3round += 30
                else:
                    p3round -= 20

        if 'only win' in p3:
            p3round += 10

        if 'only lose' in p3:
            p3round -= 10

        if (('p3' in winners) and (0 in p3) and under) or (('p3' in losers) and (0 in p3) and over):
            p3round += 10

        for lopper in [8, 9, 10, 11, 12]:
            if lopper in p3:
                p3round *= 2

        # p4 score
        if 'p4' in winners:
            p4round += p4result
        else:
            p4round -= abs(p4in - p4result)

        if 'call' in p4:
            if 'p4' in winners:
                p4round += 20
            else:
                p4round -= 10
        if 'dash call' in p4:
            if 'p4' in winners:
                p4round += 23
            else:
                p4round -= 23
        if 'with' and 'risk' in p4:
            if 'p4' in winners:
                p4round += 30
            else:
                p4round -= 20
        elif 'with' and 'd.risk' in p4:
            if 'p4' in winners:
                p4round += 40
            else:
                p4round -= 30
        else:
            if 'with' in p4:
                if 'p4' in winners:
                    p4round += 20
                else:
                    p4round -= 10

            if 'risk' in p4:
                if 'p4' in winners:
                    p4round += 20
                else:
                    p4round -= 10
            elif 'd.risk' in p4:
                if 'p4' in winners:
                    p4round += 30
                else:
                    p4round -= 20

        if 'only win' in p4:
            p4round += 10

        if 'only lose' in p4:
            p4round -= 10

        if (('p4' in winners) and (0 in p4) and under) or (('p4' in losers) and (0 in p4) and over):
            p4round += 10

        for lopper in [8, 9, 10, 11, 12]:
            if lopper in p4:
                p4round *= 2

        p1sc += p1round
        p2sc += p2round
        p3sc += p3round
        p4sc += p4round

        self.p1sc.setText(str(p1sc))
        self.p2sc.setText(str(p2sc))
        self.p3sc.setText(str(p3sc))
        self.p4sc.setText(str(p4sc))

        print(p1, p2, p3, p4)
        print('winners',winners)
        print('losers',losers)
        # final step
        self.multi_no.setChecked(False)

    def Yes_bt(self):
        self.multi_yes.setChecked(True)

    def No_bt(self):
        self.multi_no.setChecked(True)

    def clear(self):
        self.p1edit.setEnabled(True)
        self.p2edit.setEnabled(True)
        self.p3edit.setEnabled(True)
        self.p4edit.setEnabled(True)

        self.p1result.setEnabled(True)
        self.p2result.setEnabled(True)
        self.p3result.setEnabled(True)
        self.p4result.setEnabled(True)

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

        self.call1.setVisible(False)
        self.call2.setVisible(False)
        self.call3.setVisible(False)
        self.call4.setVisible(False)

        self.dc1.setEnabled(True)
        self.dc2.setEnabled(True)
        self.dc3.setEnabled(True)
        self.dc4.setEnabled(True)

        self.dc1.setChecked(False)
        self.dc2.setChecked(False)
        self.dc3.setChecked(False)
        self.dc4.setChecked(False)

        self.multi_no.setChecked(False)

        self.call_group.setEnabled(False)

    def reset(self):
        self.p1sc.setText('Score')
        self.p2sc.setText('Score')
        self.p3sc.setText('Score')
        self.p4sc.setText('Score')

        self.p1edit.clear()
        self.p2edit.clear()
        self.p3edit.clear()
        self.p4edit.clear()

        self.p1edit.setEnabled(True)
        self.p2edit.setEnabled(True)
        self.p3edit.setEnabled(True)
        self.p4edit.setEnabled(True)

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


def risk(p1, p2, p3, p4):
    # p1 : player to be checked
    dif = abs(13 - (p2c + p4c + p3c))
    if abs(dif - p1c) == 3 or abs(dif - p1c) == 2:
        return 1
    elif abs(dif - p1c) == 1 or abs(dif - p1c) == 0:
        return 0
    else:
        return 2


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


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
