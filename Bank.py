from tkinter import *
#from ttkthemes import ThemedTk
import random

ntext="0231456789"
otext="9785634210"
ptext="0987653421"
ctext="9748210356"
expression = ""


window = Tk()
window.title("Banking App/ATM")
window.geometry("250x150")
window.configure(bg="Cadet blue")
window.resizable(False,False)
equation = StringVar()
firstdata = StringVar()
secondata = StringVar()
thirdata = StringVar()
fourthdata = StringVar()
fifthdata = StringVar()
sixthdata = StringVar()
genp = StringVar()

##############################################
#Function to display number on the entry widget
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

##############################################
####Function to display numbers on the entry widget
def presing(numb):
    global expression
    expression = expression + str(numb)
    secondata.set(expression)

#################################################
########Function to display numbers on the entry widget
def presnum(numbers):
    global expression
    expression = expression + str(numbers)
    thirdata.set(expression)
    fourthdata.set(expression)
    fifthdata.set(expression)
    sixthdata.set(expression)

####Function to be clear when user press on the enter button
def EnterPIN():
    global expression
    expression = ""
    equation.set("")
    secondata.set("")
    thirdata.set("")
    fourthdata.set("")
    fifthdata.set("")
    sixthdata.set("")

def ClearPIN():
    global expression
    expression = ""
    equation.set("")
    secondata.set("")
    thirdata.set("")
    fourthdata.set("")
    fifthdata.set("")
    sixthdata.set("")

                      
##############################################
###function to open the atm###################
def openATM():
    #newATM = Toplevel(window)
    global newATM
    try:
        if newATM.state()=="normal":
            newATM.focus()
    except:
        newATM = Toplevel(window)
        newATM.title("ATM")
        newATM.geometry("685x590+0+0")
        newATM.configure(bg="white")
        newATM.resizable(False,False)
   
    ##set heading
    Label(newATM,text = "ATM",font = "Arial 16 bold",bg = "green",fg = "white",width ="590").pack()
    ##Frame1
    MenuGroup1 = Frame(newATM,bg="green",bd=10,pady=120,relief=RIDGE)
    MenuGroup1.pack(side=LEFT,ipady=96)
    ##Frame2
    MenuGroup2 = Frame(newATM,bg="green",bd=10,pady=125,relief=RIDGE)
    MenuGroup2.pack(side=RIGHT,ipady=106)
    ##Frame3
    Number_B = Frame(newATM,bg="green",bd=10,pady=10,relief=RIDGE)
    Number_B.pack(side=BOTTOM,ipady=10,ipadx=120)
    ##Menu Group
    #middle_text = Frame(newATM,bg="white",bd=10,pady=130,relief=RIDGE)
    #middle_text.pack(side=TOP,ipady=130,ipadx=180)
    ##Enter ur pin
    b_text = Label(newATM,text="Enter your pin",font="Arial 21 bold",fg="red",bg="black")
    b_text.pack(side=LEFT,pady=22,padx=80)
    #b_texting = Label(newATM,text="Dont have atm pin click on gen-atm-pin",font="Arial 8 bold",fg="red",bg="black")
    #b_texting.pack(side=LEFT,pady=20,padx=52)
    ent1 = Entry(Number_B,textvariable=equation,font="Arial 11 normal",bd=3,show='*',width=3,fg="white",bg="green")
    ent1.pack(side=TOP,padx=0)
    ##Frame for buttons
    Numbers_Butt = Frame(Number_B,bg="green",bd=0,pady=4,relief=RIDGE)
    Numbers_Butt.pack(side=TOP,ipady=12,ipadx=30)
    ##Sub Frame second for buttons
    Numbering_Butt = Frame(Numbers_Butt,bg="green",bd=0,pady=4,relief=RIDGE)
    Numbering_Butt.pack(side=BOTTOM,ipady=8,ipadx=123)
    ##Sub Frame third for buttons
    Number_Button = Frame(Numbering_Butt,bg="green",bd=0,pady=6,relief=RIDGE)
    Number_Button.pack(side=BOTTOM,ipady=10,ipadx=123)
    ##Sub Frame fourth for buttons
    Number_Cancl = Frame(Number_Button,bg="green",bd=5,pady=1,relief=RIDGE)
    Number_Cancl.pack(side=BOTTOM,ipady=6,ipadx=150)
    ##Set Label for menu1
    extra = Label(MenuGroup1,text = "--------------------",font="Arial 15 normal",bd=4,fg="yellow",bg="green",width=12)
    extra.pack(ipady=2,pady=0)
    ##buttons
    anyth = Button(MenuGroup1,text = "UpdateCellNO",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    anyth.pack(ipady=2,side=TOP,pady=0)
    nor = Button(MenuGroup1,text = "changeAtM-Pin",font = "Arial 12 normal",bd=4,bg="red",fg="white",command=changeATMPIN,width=14)
    nor.pack(ipady=2,side=TOP,pady=0)
    get = Button(MenuGroup1,text = "genAtM-Pin",font = "Arial 12 normal",bd=4,bg="red",fg="white",command=genAtMPIN,width=14)
    get.pack(ipady=2,side=TOP,pady=0)
    go = Button(MenuGroup1,text = "Balance-INQ",font="Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    go.pack(ipady=2,side=TOP)
    gud = Button(MenuGroup1,text = "Deposit",font="Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    gud.pack(ipady=2,side=TOP)
    nfa = Button(MenuGroup1,text = "UpdatePSB",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    nfa.pack(ipady=2,side=TOP,pady=0)
    ##Set ending label
    extra = Label(MenuGroup1,text = "--------------------",font="Arial 15 normal",bd=4,fg="yellow",bg="green",width=12)
    extra.pack(ipady=2,pady=0)
    ##Set heading for menu2
    move = Label(MenuGroup2,text="--------------------",font="Arial 15 normal",bd=4,fg="yellow",bg="green",width=12)
    move.pack(ipady=0,pady=0)
    ##buttons
    anad = Button(MenuGroup2,text = "WithDraw",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    anad.pack(ipady=2,side=TOP,pady=0)
    norway = Button(MenuGroup2,text = "Savings/Account",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    norway.pack(ipady=2,side=TOP,pady=0)
    getadd = Button(MenuGroup2,text = "Current/Account",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    getadd.pack(ipady=2,side=TOP,pady=0)
    gotoadd = Button(MenuGroup2,text = "Quick Cash",font="Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    gotoadd.pack(ipady=2,side=TOP)
    guddo = Button(MenuGroup2,text = "MiniStatement",font="Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    guddo.pack(ipady=2,side=TOP)
    nfaass = Button(MenuGroup2,text = "Transfer",font = "Arial 12 normal",bd=4,bg="red",fg="white",width=14)
    nfaass.pack(ipady=2,side=TOP,pady=0)
    ##Set ending label
    exasf = Label(MenuGroup2,text = "--------------------",font="Arial 15 normal",bd=4,fg="yellow",bg="green",width=12)
    exasf.pack(ipady=2,pady=0)
    ##Set number buttons frame
    Num1 = Button(Numbers_Butt,text="1",command=lambda: press(1),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num1.pack(ipady=0,side=LEFT,pady=0,padx=25)
    Num2 = Button(Numbers_Butt,text="2",command=lambda: press(2),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num2.pack(ipady=0,side=LEFT,padx=12,pady=0)
    Num3 = Button(Numbers_Butt,text="3",command=lambda: press(3),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num3.pack(ipady=0,side=LEFT,padx=20,pady=0)
    Num4 = Button(Numbers_Butt,text="4",command=lambda: press(4),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num4.pack(ipady=0,side=LEFT,padx=17,pady=0)
    Num5 = Button(Numbering_Butt,text="5",command=lambda: press(5),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num5.pack(ipady=0,side=LEFT,padx=24,pady=0)
    Num6 = Button(Numbering_Butt,text="6",command=lambda: press(6),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num6.pack(ipady=0,side=LEFT,padx=17,pady=0)
    Num7 = Button(Numbering_Butt,text="7",command=lambda: press(7),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num7.pack(ipady=0,side=LEFT,padx=16,pady=0)
    Num8 = Button(Numbering_Butt,text="8",command=lambda: press(8),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num8.pack(ipady=0,side=LEFT,padx=21,pady=0)
    Num9 = Button(Number_Button,text="9",command=lambda: press(9),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num9.pack(ipady=0,side=LEFT,padx=24,pady=0)
    Num0 = Button(Number_Button,text="0",command=lambda: press(0),font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=3,height=1)
    Num0.pack(ipady=0,side=LEFT,padx=22,pady=0)
    Numcle = Button(Number_Button,text="Clear",command=ClearPIN,font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=7,height=1)
    Numcle.pack(ipady=0,side=LEFT,padx=26,pady=0)
    Numcanc = Button(Number_Cancl,text="Cancel",font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=7,height=1)
    Numcanc.pack(ipady=0,side=LEFT,padx=42,pady=0)
    NumEnt = Button(Number_Cancl,text="Enter",command=EnterPIN,font="Arial 13 normal",bd=4,bg="cadetblue",fg="white",width=7,height=1)
    NumEnt.pack(ipady=0,side=LEFT,padx=26,pady=0)
        
def genAtMPIN():
    ##generate user atm pin
    ###create window for generating pin
    #global newATM
    global newPin
    try:
        if newPin.state()=="normal":
            newPin.focus()
    except:
        newPin = Toplevel(newATM)
        newPin.title("ATM-Gen-Pin")
        newPin.geometry("475x502+0+0")
        newPin.configure(bg="white")
        newPin.resizable(False,False)

    def ProcessPin():
        num2Butt["state"]=DISABLED
        f=random.choice(ntext)
        d=random.choice(otext)
        q=random.choice(ptext)
        c=random.choice(ctext)
        genp.set(" ".join(f+d+q+c))
        savingdata = Button(newPin,text="save",command=lambda: (savingdata.pack_forget(),exitdata.pack_forget(),dispin.pack_forget(),newPin,num2Butt.config(state=NORMAL)),font="Arial 8 bold",bd=5,bg="red",fg="white",width=9,height=1)
        savingdata.pack(ipady=0,padx=0,pady=0)
        exitdata = Button(newPin,text="Cancel",command=lambda: (exitdata.pack_forget(),savingdata.pack_forget(),dispin.pack_forget(),newPin,num2Butt.config(state=NORMAL)),font="Arial 8 bold",bd=4,bg="blue",fg="red",width=9,height=1)
        exitdata.pack(ipady=0,padx=0,pady=0)
        dispin = Label(newPin,textvariable=genp,font="Arial 12 normal",fg="brown")
        dispin.pack(ipady=0,padx=12,pady=24)

    def ManualyGenPin():
        genmanpin = Toplevel(newPin)
        genmanpin.title("GenManATMPin")
        genmanpin.geometry("396x420")
        genmanpin.configure(bg="cadet blue")
        genmanpin.resizable(False,False)

        text1 = Entry(genmanpin,textvariable=secondata,font="Arial 13 normal",show='*',bd=4,width=3,fg="white",bg="black")
        text1.pack(padx=3,pady=45)
        gosub = Button(genmanpin,text="Save",command=EnterPIN ,font="Arial 9 bold",bd=4,bg="lightblue",fg="black",width=5,height=1)
        gosub.pack(ipady=0,padx=2,pady=0)
        gocler = Button(genmanpin,text="Clear",command=ClearPIN,font="Arial 9 bold",bd=4,bg="lightblue",fg="black",width=5,height=1)
        gocler.pack(ipady=0,padx=0,pady=1)
        Frameforbutts = Frame(genmanpin,bg="gray",bd=6,pady=4,relief=RIDGE)
        Frameforbutts.pack(ipadx=150,ipady=128)
        Frameforbut = Frame(Frameforbutts,bg="gray",bd=0,pady=0,relief=RIDGE)
        Frameforbut.pack(ipadx=85,ipady=5)
        m1but = Button(Frameforbut,text="1",command=lambda : presing(1),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m1but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m2but = Button(Frameforbut,text="2",command=lambda : presing(2),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m2but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m3but = Button(Frameforbut,text="3",command=lambda: presing(3),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m3but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        FrameforBut = Frame(Frameforbutts,bg="gray",bd=0,pady=0,relief=RIDGE)
        FrameforBut.pack(ipady=5,ipadx=85)
        m4but = Button(FrameforBut,text="4",command=lambda : presing(4),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m4but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m5but = Button(FrameforBut,text="5",command=lambda : presing(5),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m5but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m6but = Button(FrameforBut,text="6",command=lambda : presing(6),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m6but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        ButforFrame = Frame(Frameforbutts,bg="gray",bd=0,pady=0,relief=RIDGE)
        ButforFrame.pack(ipady=5,ipadx=85)
        m7but = Button(ButforFrame,text="7",command=lambda : presing(7),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m7but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m8but = Button(ButforFrame,text="8",command=lambda : presing(8),font="Arial 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m8but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m9but = Button(ButforFrame,text="9",command=lambda : presing(9),font="Arail 10 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m9but.pack(ipady=5,ipadx=5,side=LEFT,pady=10,padx=30)
        m0but = Button(ButforFrame,text="0",command=lambda : presing(0),font="Arial 12 normal",bd=3,bg="brown",fg="white",width=2,height=1)
        m0but.pack(ipady=12,ipadx=10,side=LEFT,pady=5,padx=10)

    def TwoButtons():
        sea1["state"] = DISABLED
        global num1Butt
        num1Butt = Button(newPin,text="Manually GenATMPin",command=ManualyGenPin,font="Arial 9 bold",bd=5,bg="red",fg="yellow",width=17,height=1)
        num1Butt.pack(ipady=0,padx=10,pady=10)
        global num2Butt
        num2Butt = Button(newPin,text="Computerised GenATMPin",command=ProcessPin,#command=lambda num2Butt=num2Butt: [newPin,num2Butt.config(state=DISABLED)]
                          font="Arial 9 bold",bd=5,bg="red",fg="yellow",width=21,height=2)
        num2Butt.pack(ipady=0,padx=10,pady=18)
        num2Butt.config(height=1, width=21, # USE command SHOWN BELOW. ##
                        command=ProcessPin)
    
    ##set Heading
    Label(newPin,text = "Create Pin",font = "Arial 16 bold",bg = "black",fg = "white",width ="280").pack()
    accno = Label(newPin,text="Account Number :",font="Arial 14 bold",fg="red")
    accno.pack(padx=6,pady=12)
    d1 = Entry(newPin,textvariable=firstdata,font="Arial 13 normal",bd=2,width=18,fg="white",bg="black")
    d1.pack(padx=3)
    sea1 = Button(newPin,text="Search&GenPin",command=TwoButtons,font="Arial 8 bold",bd=5,bg="red",fg="blue",width=12,height=2)
    sea1.pack(ipady=0,padx=3,pady=10)


###############################################
########change atm-pin####################
def changeATMPIN():
    genchatmpin = Toplevel(newATM)
    genchatmpin.title("ChangeATM-PIN")
    genchatmpin.geometry("475x470+0+0")
    genchatmpin.configure(bg="purple")
    genchatmpin.resizable(False,False)

    def ShowButt():
        da2["state"]=DISABLED
        Sh1butf = Frame(genchatmpin,bg="yellow",bd=3,pady=2,relief=RIDGE)
        Sh1butf.pack(side=TOP,ipady=10,ipadx=190)
        oldlab = Label(Sh1butf,text="Old :",font="Arial 10 bold",bg="yellow",fg="red",width=8)
        oldlab.pack(side=LEFT)
        oldbut = Entry(Sh1butf,textvariable=fourthdata,font="Arial 14 bold",bd=4,width=5,show="*",fg="white",bg="black")
        oldbut.pack(side=LEFT)
        newlab = Label(Sh1butf,text="New :",font="Arial 10 bold",bg="yellow",fg="red",width=8)
        newlab.pack(side=LEFT)
        newbut = Entry(Sh1butf,textvariable=fifthdata,font="Arial 14 bold",bd=4,width=5,fg="white",show="*",bg="black")
        newbut.pack(side=LEFT)
        cnewlab = Label(Sh1butf,text="Confirm :",font="Arial 9 bold",bg="yellow",fg="red",width=9)
        cnewlab.pack(side=LEFT)
        cnewbut = Entry(Sh1butf,textvariable=sixthdata,font="Arial 14 bold",bd=4,width=5,show="*",fg="white",bg="black")
        cnewbut.pack(side=LEFT)
        ##FRAMES
        Sh2butf = Frame(genchatmpin,bg="green",bd=3,pady=5,relief=RIDGE)
        Sh2butf.pack(side=TOP,ipady=100,ipadx=150)
        Shbutframe = Frame(Sh2butf,bg="green",bd=0,pady=2,relief=RIDGE)
        Shbutframe.pack(side=TOP,ipady=3,ipadx=150)
        Shwbutframe = Frame(Shbutframe,bg="green",bd=0,pady=2,relief=RIDGE)
        Shwbutframe.pack(side=BOTTOM,ipady=3,ipadx=150)
        Shobutframe = Frame(Shwbutframe,bg="green",bd=0,pady=2,relief=RIDGE)
        Shobutframe.pack(side=BOTTOM,ipady=3,ipadx=150)
        ##BUTTONS
        onebut = Button(Shbutframe,text="1",command=lambda:presnum(1),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        onebut.pack(padx=10,pady=2,side=LEFT)
        twobut = Button(Shbutframe,text="2",command=lambda:presnum(2),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        twobut.pack(padx=10,pady=2,side=LEFT)
        threebut = Button(Shbutframe,text="3",command=lambda:presnum(3),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        threebut.pack(padx=10,pady=2,side=LEFT)
        fourbut = Button(Shbutframe,text="4",command=lambda:presnum(4),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        fourbut.pack(padx=10,pady=2,side=LEFT)
        fivebut = Button(Shwbutframe,text="5",command=lambda:presnum(5),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        fivebut.pack(padx=10,pady=2,side=LEFT)
        sixbut = Button(Shwbutframe,text="6",command=lambda:presnum(6),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        sixbut.pack(padx=10,pady=2,side=LEFT)
        sevenbut = Button(Shwbutframe,text="7",command=lambda:presnum(7),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        sevenbut.pack(padx=10,pady=2,side=LEFT)
        eightbut = Button(Shwbutframe,text="8",command=lambda:presnum(8),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        eightbut.pack(padx=10,pady=2,side=LEFT)
        ninebut = Button(Shobutframe,text="9",command=lambda:presnum(9),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        ninebut.pack(padx=10,pady=2,side=LEFT)
        zerobut = Button(Shobutframe,text="0",command=lambda:presnum(0),font="Arial 10 bold",bd=5,bg="blue",fg="white",width=3,height=2)
        zerobut.pack(padx=10,pady=2,side=LEFT)
        Canbut = Button(Shobutframe,text="CANCEL",command=ClearPIN,font="Arial 9 bold",bd=8,bg="red",fg="white",width=8,height=2)
        Canbut.pack(padx=36,pady=2,side=LEFT)
        clearbut = Button(Shobutframe,text="CLEAR",command=EnterPIN,font="Arial 9 bold",bd=8,bg="red",fg="white",width=7,height=2)
        clearbut.pack(padx=38,pady=2,side=LEFT)
        Savebut = Button(Shwbutframe,text="SAVE",command=EnterPIN,font="Arial 9 bold",bd=8,bg="brown",fg="white",width=8,height=2)
        Savebut.pack(padx=60,pady=2,side=LEFT)
     
    Label(genchatmpin,text="Change Pin",font="Arial 16 bold",bg="red",fg="white",width=280).pack()
    accnum = Label(genchatmpin,text="Account Number",font="Arial 14 bold",fg="brown",bg="red")
    accnum.pack(padx=6,pady=12)
    da1 = Entry(genchatmpin,textvariable=thirdata,font="Arial 13 normal",bd=2,width=18,fg="white",bg="black")
    da1.pack(padx=3)
    da2 = Button(genchatmpin,text="Ch-atm-pin",command=ShowButt,font="Arial 9 bold",bd=5,bg="red",fg="white",width=12,height=2)
    da2.pack(ipady=0,padx=3,pady=8)
    
   
##############################################
#####function to open the bank app############
def openBank():
    newBank = Toplevel(window)
    newBank.title("Bank")
    newBank.state('zoomed')
    newBank.resizable(False,False)
    #newBank.geometry("19441x19810")
    ##set heading
    Label(newBank,text = "Banking Application",font = "Arial 16 bold",bg = "gray").pack()

######################################################################################################################
head = Label(window,text = "Welcome To The e-Bank",font = "Arial 16 bold",fg = "red",bg="Cadet blue")
head.pack()
bnk = Button(window,text = "Go-Bank",font = "Arial 11 normal",command = openBank,bg="orange",fg="white",bd=4)
bnk.pack(padx = 10,pady = 10)
atm = Button(window,text = "ATM",font = "Arial 11 normal",command = openATM,bg="brown",fg="white",bd=4)
atm.pack(padx = 20,pady = 11,ipadx = 1)

window.mainloop()
