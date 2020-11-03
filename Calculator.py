import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk

class Mainwindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Calculator")
        #Grid
        grid=Gtk.Grid()
        self.add(grid)

        buttonclear=Gtk.Button(label="CE")
        buttonclear.connect("clicked",self.buttonclear_clicked)
        buttonequal=Gtk.Button(label="=")
        buttonequal.connect("clicked",self.buttonequal_clicked)
        button1=Gtk.Button(label="1")
        button1.connect("clicked",self.button1_clicked)
        button2=Gtk.Button(label="2")
        button2.connect("clicked",self.button2_clicked)
        button3=Gtk.Button(label="3")
        button3.connect("clicked",self.button3_clicked)
        button4=Gtk.Button(label="4")
        button4.connect("clicked",self.button4_clicked)
        button5=Gtk.Button(label="5")
        button5.connect("clicked",self.button5_clicked)
        button6=Gtk.Button(label="6")
        button6.connect("clicked",self.button6_clicked)
        button7=Gtk.Button(label="7")
        button7.connect("clicked",self.button7_clicked)
        button8=Gtk.Button(label="8")
        button8.connect("clicked",self.button8_clicked)
        button9=Gtk.Button(label="9")
        button9.connect("clicked",self.button9_clicked)
        button0=Gtk.Button(label="0")
        button0.connect("clicked",self.button0_clicked)
        buttonadd=Gtk.Button(label="+")
        buttonadd.connect("clicked",self.buttonadd_clicked)
        buttonsub=Gtk.Button(label="-")
        buttonsub.connect("clicked",self.buttonsub_clicked)
        buttonmul=Gtk.Button(label="*")
        buttonmul.connect("clicked",self.buttonmul_clicked)
        buttondiv=Gtk.Button(label="/")
        buttondiv.connect("clicked",self.buttondiv_clicked)
        grid.add(button1)
        grid.attach(button2,1,0,1,1)
        grid.attach(button3,2,0,1,1)
        grid.attach(buttonequal,3,0,1,1)
        grid.attach(button4,0,1,1,1)
        grid.attach(button5,1,1,1,1)
        grid.attach(button6,2,1,1,1)
        grid.attach(buttonadd,3,1,1,1)
        grid.attach(button7,0,2,1,1)
        grid.attach(button8,1,2,1,1)
        grid.attach(button9,2,2,1,1)
        grid.attach(buttonsub,3,2,1,1)
        grid.attach(buttonclear,0,3,1,1)
        grid.attach(button0,1,3,1,1)
        grid.attach(buttondiv,2,3,1,1)
        grid.attach(buttonmul,3,3,1,1)

    a1=0
    b1=0
    i=0
    def button1_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+1
        elif(op1==''):
            b1=b1*10+1
    def button2_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+2
        elif(op1==''):
            b1=b1*10+2
    def button3_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+3
        elif(op1==''):
            b1=b1*10+3
    def button4_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+4
        elif(op1==''):
            b1=b1*10+4
    def button5_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+5
        elif(op1==''):
            b1=b1*10+5
    def button6_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+6
        elif(op1==''):
            b1=b1*10+6
    def button7_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+7
        elif(op1==''):
            b1=b1*10+7
    def button8_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+8
        elif(op1==''):
            b1=b1*10+8
    def button9_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+9
        elif(op1==''):
            b1=b1*10+9
    def button0_clicked(self,widget):
        global a1
        global b1
        if(op==''):
            a1=a1*10+0
        elif(op1==''):
            b1=b1*10+0
    def buttonadd_clicked(self,widget):
        global op
        print(a1)
        if(op==''):
            op='+'
            print("+")
    def buttonsub_clicked(self,widget):
        global op
        print(a1)
        if(op==''):
            op='-'
            print("-")
    def buttonmul_clicked(self,widget):
        global op
        print(a1)
        if(op==''):
            op='*'
            print("*")
    def buttondiv_clicked(self,widget):
        global op
        print(a1)
        if(op==''):
            op='/'
            print("/")
    def buttonclear_clicked(self,widget):
        print("Clear")
        global a1
        a1=0
        global b1
        b1=0
        global op
        op=''
        global op1
        op1=''
        global i
        i=0
        global j
        j=0
    def buttonequal_clicked(self,widget):
        print(b1)
        print("=")
        op1='='
        operate(a1,b1,op)
def operate(a1,b1,op):
    if(op==''):
        print("No operator")
    elif(op=='+'):
        print(a1+b1)
    elif(op=='-'):
        print(a1-b1)
    elif(op=='*'):
        print(a1*b1)
    elif(op=='/'):
        print(a1/b1)
global a1
a1=0
global b1
b1=0
global i
i=0
global j
j=0
global op
op=''
global op1
op1=''

W=Mainwindow()
W.connect("delete_event",Gtk.main_quit)
W.show_all()
Gtk.main()
