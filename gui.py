#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
import core
from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QWidget,QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush

class gui(QWidget):
    def __init__(self):
        super().__init__()
        self.lifegame = core.Lifegame(50)
        self.initUI()

    #UIの初期化を行うところ
    def initUI(self):
        
        #windowの設定
        self.setGeometry(0, 0, 800, 550)
        self.setWindowTitle('life-game')

        #1つ進むbuttonの設定
        button = QPushButton(u'1つ進む',self)  
        ##ボタンがクリックされたらredraw()が呼ばれる
        button.clicked.connect(self.redraw)
        button.move(600,500)
        
        #windowの表示
        self.show()

    #画面更新のときに呼ばれるイベント
    #起動時の他にself.repaint()で呼ぶことができる
    def paintEvent(self,event):
        q_paint = QPainter()
        q_paint.begin(self)
        self.drawField(q_paint)
        q_paint.end()

    #クリックされるたびに呼ばれるイベント
    def mousePressEvent(self,event):
        #event.x(),event.y()で現在の座標を取得
        #表示上の盤面は10倍+25されているので元に戻す
        #math.floorで小数を切り捨て
        x = math.floor((event.x()  - 25) / 10)
        y = math.floor((event.y()  - 25) / 10)
        if (x >= 0 and x < 50 and y >= 0 and y < 50):
            self.lifegame.field[x][y] = not (self.lifegame.field[x][y])
            self.repaint()

    #描画メゾット
    def drawField(self,q_paint):
        for i in range(50):
            for j in range (50):
                if (self.lifegame.field[i][j] == 0):
                    q_paint.setBrush(QColor(255,255,255,128))
                else:
                    q_paint.setBrush(QColor(0,0,0,128))
                q_paint.drawRect(i*10+25,j*10+25,10, 10)
    
    #1つ進むボタンが押されたときに呼ばれるメゾット
    def redraw(self):
        self.lifegame.forward()
        self.repaint()
              
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = gui()
    sys.exit(app.exec_())
