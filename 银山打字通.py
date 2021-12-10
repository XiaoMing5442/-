#导包
#-*- coding:UTF-8 -*-
from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtWidgets
import random
import time
import sys
from decimal import Decimal
import os

dec=open('decimal.txt',mode='rb')#加载难度
a=dec.read()
a=int(a)
dec.close()

main_win2 = None
main_win4 = None
main_win = None
main_win3 = None
main_end = None
an=None
StRing=None
class About():
    def __init__(self):#加载窗口5
        super().__init__()
        win5=QFile('ui/about.ui')
        win5.open(QFile.ReadOnly)
        win5.close
        self.about=QUiLoader().load(win5)
    def close_about(self):
        global main_win2
        main_win2 = Stats()
        # 显示新窗口
        main_win2.ui.show()
        # 关闭自己
        self.about.close()
class Setting():
    def __init__(self):#加载窗口4
        super().__init__()
        win4=QFile('ui/setting.ui')
        win4.open(QFile.ReadOnly)
        win4.close
        self.setting=QUiLoader().load(win4)
    def save_exit(self):#难度保存并返回
        a=self.setting.decim.text()
        os.remove('decimal.txt')
        dec=open('decimal.txt',mode="a")
        dec.write(a)
        dec.close
        a=int(a)
        global main_win2
        main_win2 = Stats()
        # 显示新窗口
        main_win2.ui.show()
        # 关闭自己
        self.setting.close()
class End():
    def __init__(self):#加载窗口3
        super().__init__()
        win3=QFile('ui/end.ui')
        win3.open(QFile.ReadOnly)
        win3.close
        self.end=QUiLoader().load(win3)
    def get_back(self):#返回按键的函数
        global main_win2
        main_win2 = Stats()
        # 显示新窗口
        main_win2.ui.show()
        # 关闭自己
        self.end.close()

class Window2():
    def __init__(self):#加载窗口2
        super().__init__()
        win2=QFile('ui/game.ui')
        win2.open(QFile.ReadOnly)
        win2.close
        self.window2=QUiLoader().load(win2)
    def game_end(self):#提交按键的函数
        #s1程序
        text=self.window2.usestr.toPlainText()
        usestr_num=len(text)
        b=usestr_num-1
        #s2程序
        STr=StRing[0:usestr_num]
        i=0
        x=0
        while i<=b:
            if STr[i] == text[i]:
                x+=1
                i+=1
            else:
                i+=1
        x=Decimal(x)
        usestr_num=Decimal(usestr_num)
        x_per=x/usestr_num*100
        x_per=round(x_per,1)
        #计算时间(s3)  
        hou=Decimal(time.time())
        TiMe=hou-an
        global main_end
        main_end = End()
        TiMe=round(TiMe,1)
        # 显示新窗口
        main_end.end.show()
        # 关闭自己
        self.window2.close()
        #显示数据
        s1='原本有{}个字符，您输入了{}个字符'.format(a,usestr_num)
        s2='您输入对了{}个，正确率约是{}%'.format(x,x_per)
        s3='您输入共用了{}秒'.format(TiMe)
        main_end.end.mess.append(s1)
        main_end.end.mess.append(s2)
        main_end.end.mess.append(s3)
        #返回按钮
        main_end.end.retuen.clicked.connect(main_end.get_back)
    
class Stats():
    def __init__(self):
        # 加载窗口
        super().__init__()
        qfile_stats=QFile('ui/stats.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close
        self.ui=QUiLoader().load(qfile_stats)
        #按键交互
        self.ui.start.clicked.connect(self.start_click)#开始按键
        self.ui.easy.clicked.connect(self.easy_diff)#难度按键
        self.ui.bilibili.clicked.connect(self.goto_about)
    def goto_about(self):
        global main_win4
        main_win4 = About()
        # 显示新窗口
        main_win4.about.show()
        # 关闭自己
        self.ui.hide()
        #返回按键
        main_win4.about.goto_2.clicked.connect(main_win4.close_about)
    def easy_diff(self):#难度按键函数
        global main_win3
        main_win3 = Setting()
        # 显示新窗口
        main_win3.setting.show()
        # 关闭自己
        self.ui.hide()
        #设置文本框
        global a
        a=str(a)
        main_win3.setting.decim.setText(a)
        main_win3.setting.savE.clicked.connect(main_win3.save_exit)#保存按键
    def start_click(self):
        global main_win
        main_win = Window2()
        # 显示新窗口
        main_win.window2.show()
        # 关闭自己
        self.ui.hide()
        main_win.window2.seconds.append('打完请按提交哦')
        #开始按键侦测
        main_win.window2.begin.clicked.connect(self.str_time)
    def str_time(self):#当按下开始按键后的函数
        #字库
        chinese="的一是在不了有和人这中大为上个国我以要他时来用们生到作地于出就分对成会可主发年动同工也能下过子说产种面而方后多定行学法所民得经十三之进着等部度家电力里如水化高自二理起小物现实加量都两体制机当使点从业本去把性好应开它合还因由其些然前外天政四日那社义事平形相全表间样与关各重新线内数正心反你明看原又么利比或但质气第向道命此变条只没结解问意建月公无系军很情者最立代想已通并提直题党程展五果料象员革位入常文总次品式活设及管特件长求老头基资边流路级少图山统接知较长将组见计别她手角期根论运农指几九区强放决西被干做必战先回则任取据处队南给色光门即保治北造百规热领七海地口东导器压志世金增争济阶油思术极交受联什认六共权收证改清已美再采转更单风切打白教速花带安场身车例真务具万每目至达走积示议声报斗完类八离华名确才科张信马节话米整空元况今集温传土许步群广石记需段研界拉林律叫且究观越织装影算低持音众书布复容儿须际商非验连断深难近矿千周委素技备半办青省列习响约支般史感劳便团往酸历市克何除消构府称太准精值号率族维划选标写存候毛亲快效斯院查江型眼王按格养易置派层片始却专状育厂京识适属圆包火住调满县局照参红细引听该铁价严首底液官德调随病苏失尔死讲配女黄推显谈罪神艺呢席含企望密批营项防举球英氧势告李台落木帮轮破亚师围注远字材排供河态封另施减树溶怎止案言士均武固叶鱼波视仅费紧爱左章早朝害续轻服试食充兵源判护司足某练差致板田降黑犯负击范继兴似余坚曲输修的故城夫够送笔船占右财吃富春职觉汉画功巴跟虽杂飞检"
        i=0
        #准备
        global StRing
        StRing=''
        global a
        a=int(a)
        while i<a:#随机取字
            选取字索引=random.randint(0,639)
            选取字=chinese[选取字索引]
            main_win.window2.str.insertPlainText(选取字)
            StRing+=选取字
            i+=1
        main_win.window2.seconds.append('开始计时')
        global an
        an=Decimal(time.time())#获取当前时间
        
        #侦测按键：提交
        main_win.window2.daTa.clicked.connect(main_win.game_end)
    

#显示第一个窗口        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Stats()
    window.ui.show()
    sys.exit(app.exec_())
