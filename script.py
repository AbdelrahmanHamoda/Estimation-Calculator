import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtCore import *
#from PyQt5.QtGui import *

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

        #self.dc1.toggled.connect(self.dash_call)
        #self.dc2.toggled.connect(self.dash_call)
        #self.dc3.toggled.connect(self.dash_call)
        #self.dc4.toggled.connect(self.dash_call)

        #self.p1call.toggled.connect(self.update)
        #self.p2call.toggled.connect(self.update)
        #self.p3call.toggled.connect(self.update)
        #self.p4call.toggled.connect(self.update)

        #self.p1call.toggled.connect(self.with_update)
        #self.p2call.toggled.connect(self.with_update)
        #self.p3call.toggled.connect(self.with_update)
        #self.p4call.toggled.connect(self.with_update)

        self.p1edit.textChanged.connect(self.edit1)
        self.p2edit.textChanged.connect(self.edit2)
        self.p3edit.textChanged.connect(self.edit3)
        self.p4edit.textChanged.connect(self.edit4)

        #self.p4edit.editingFinished.connect(self.ui_update)

        self.p1result.textChanged.connect(self.ui_update)
        self.p2result.textChanged.connect(self.ui_update)
        self.p3result.textChanged.connect(self.ui_update)
        self.p4result.textChanged.connect(self.ui_update)

    def dash_call(self):
        if self.dc1.isChecked() and self.dc2.isChecked():
            self.dc3.setEnabled(False)
            self.dc4.setEnabled(False)
            self.p1edit.setEnabled(False)
            self.p2edit.setEnabled(False)
            return True
        else:
            print('here')
            if self.p3edit.text() == '':
                self.dc3.setEnabled(True)
            if self.p4edit.text() == '':
                self.dc4.setEnabled(True)
            #self.p1edit.setEnabled(True)
            #self.p2edit.setEnabled(True)

            if self.dc1.isChecked() and self.dc3.isChecked():
                self.dc2.setEnabled(False)
                self.dc4.setEnabled(False)
                self.p1edit.setEnabled(False)
                self.p3edit.setEnabled(False)
                return True
            else:
                if self.p2edit.text() == '':
                    self.dc2.setEnabled(True)
                if self.p4edit.text() == '':
                    self.dc4.setEnabled(True)
                print('here1')
                #self.p1edit.setEnabled(True)
                #self.p3edit.setEnabled(True)

                if self.dc1.isChecked() and self.dc4.isChecked():
                    self.dc2.setEnabled(False)
                    self.dc3.setEnabled(False)
                    self.p1edit.setEnabled(False)
                    self.p4edit.setEnabled(False)
                    return True
                else:
                    print('here2')
                    if self.p2edit.text() == '':
                        self.dc2.setEnabled(True)
                    if self.p3edit.text() == '':
                        self.dc3.setEnabled(True)
                    #self.p1edit.setEnabled(True)
                    #self.p4edit.setEnabled(True)

                    if self.dc2.isChecked() and self.dc3.isChecked():
                        self.dc1.setEnabled(False)
                        self.dc4.setEnabled(False)
                        self.p2edit.setEnabled(False)
                        self.p3edit.setEnabled(False)
                        return True
                    else:
                        print('here3')
                        if self.p1edit.text()=='':
                            self.dc1.setEnabled(True)
                        if self.p4edit.text() == '':
                            self.dc4.setEnabled(True)
                        #self.p2edit.setEnabled(True)
                        #self.p3edit.setEnabled(True)

                        if self.dc2.isChecked() and self.dc4.isChecked():
                            self.dc1.setEnabled(False)
                            self.dc3.setEnabled(False)
                            self.p2edit.setEnabled(False)
                            self.p4edit.setEnabled(False)
                            return True
                        else:
                            print('here4')
                            if self.p1edit.text() == '':
                                self.dc1.setEnabled(True)
                            if self.p3edit.text() == '':
                                self.dc3.setEnabled(True)
                            #self.p2edit.setEnabled(True)
                            #self.p4edit.setEnabled(True)

                            if self.dc3.isChecked() and self.dc4.isChecked():
                                self.dc1.setEnabled(False)
                                self.dc2.setEnabled(False)
                                self.p3edit.setEnabled(False)
                                self.p4edit.setEnabled(False)
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
            self.p1edit.setEnabled(False)
            self.p1edit.clear()
            self.p2edit.setFocus(True)
        else:
            self.p1edit.setEnabled(True)
            self.p1edit.setFocus(True)
        self.ui_update()

    def dash_call2(self):
        self.dash_call()
        if self.dc2.isChecked():
            self.p2edit.setEnabled(False)
            self.p2edit.clear()
            self.p3edit.setFocus(True)
        else:
            self.p2edit.setEnabled(True)
            self.p2edit.setFocus(True)
        self.ui_update()

    def dash_call3(self):
        self.dash_call()
        if self.dc3.isChecked():
            self.p3edit.setEnabled(False)
            self.p3edit.clear()
            self.p4edit.setFocus(True)
        else:
            self.p3edit.setEnabled(True)
            self.p3edit.setFocus(True)
        self.ui_update()

    def dash_call4(self):
        self.dash_call()
        if self.dc4.isChecked():
            self.p4edit.setEnabled(False)
            self.p4edit.clear()
            self.p1result.setFocus(True)
        else:
            self.p4edit.setEnabled(True)
            self.p4edit.setFocus(True)
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

    def with_update2(self):
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
        ls_players=['p1','p2','p3','p4']
        caller=[]

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
            self.p1edit.setEnabled(False)
            self.p2edit.setEnabled(False)
            self.p3edit.setEnabled(False)
            self.p4edit.setEnabled(False)
            self.risk1.setVisible(False)
            self.risk2.setVisible(False)
            self.risk3.setVisible(False)
            self.risk4.setVisible(False)
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
                    self.risk1.setVisible(False)
                else:
                    self.p1with.setEnabled(True)
                    self.p1with.setChecked(True)

            if 'p2' in caller:
                self.p2call.toggled.connect(self.with_update2)
                if self.p2call.isChecked():
                    self.p2with.setEnabled(False)
                    self.risk2.setVisible(False)
                else:
                    self.p2with.setEnabled(True)
                    self.p2with.setChecked(True)

            if 'p3' in caller:
                self.p3call.toggled.connect(self.with_update2)
                if self.p3call.isChecked():
                    self.p3with.setEnabled(False)
                    self.risk3.setVisible(False)
                else:
                    self.p3with.setEnabled(True)
                    self.p3with.setChecked(True)

            if 'p4' in caller:
                self.p4call.toggled.connect(self.with_update2)
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

    def edit1(self):
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

    def ui_update(self):
        if self.p1result.text() != '':
            clickable(self.p1result).connect(self.clear_11)

        if self.p2result.text() != '':
            clickable(self.p2result).connect(self.clear_12)

        if self.p3result.text() != '':
            clickable(self.p3result).connect(self.clear_13)

        if self.p4result.text() != '':
            clickable(self.p4result).connect(self.clear_14)

        if (self.p1edit.text() != '' or self.dc1.isChecked()) and (self.p2edit.text() != '' or self.dc2.isChecked())\
                and (self.p3edit.text() != '' or self.dc3.isChecked()) and \
                (self.p4edit.text() != '' or self.dc4.isChecked()):
            print('True')
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
            return

        # calculate button control
        if (self.p1edit.text()!='' or self.dc1.isChecked()) and (self.p2edit.text()!='' or self.dc2.isChecked())\
                and (self.p3edit.text()!='' or self.dc3.isChecked()) and \
                (self.p4edit.text()!='' or self.dc4.isChecked())\
                and self.p1result.text() != '' and self.p2result.text() != '' and \
                self.p3result.text() != '' and self.p4result.text() != '':
            self.calculate_bt.setEnabled(True)
        else:
            self.calculate_bt.setEnabled(False)

        if (self.p1edit.text()!='' or self.dc1.isChecked()) and (self.p2edit.text()!='' or self.dc2.isChecked())\
                and (self.p3edit.text()!='' or self.dc3.isChecked()) and \
                (self.p4edit.text()!='' or self.dc4.isChecked()):
            self.call_group.setEnabled(True)
        else:
            self.call_group.setEnabled(False)

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
        self.p2edit.setEnabled(True)
        self.p3edit.setEnabled(True)
        self.p4edit.setEnabled(True)
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
