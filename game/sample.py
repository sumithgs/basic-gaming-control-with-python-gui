import snakegame,tictactoe,backend,spaceinvader,datetime,time,sqlite3,carracec,smtplib,random
from tkinter import *
import tkinter.messagebox
def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=f'Time:{time_string}')
    clock.after(200, tick)
root = Tk()
root.title('Game Hub')
root.geometry('750x270')
root.minsize(750,270)
root.maxsize(750,270)
root.configure(background='black')
hour = int(datetime.datetime.now().hour)
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
"""
def fp():
    # this method of sending email is not valid any more
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('gmail id', 'gmail password')
        server.sendmail('gmail id', to, content)
        server.close()
    content = f'{random.randrange(1000,9999,1)}'
    to = 'to gmail id'
    sendEmail(to, content)
    r = Tk()
    Label(r,text='OTP',font='Ariel 10 bold',fg='black').grid(row=0,column=0)
    ent = StringVar()
    e = Entry(r,textvariable=ent,show='*')
    e.grid(row=0,column=1)
    Label(r,text='enter new user',font='Ariel 10 bold',fg='black').grid()
    lo = StringVar()
    l = Entry(r,textvariable=lo)
    l.grid()
    pw = StringVar()
    Label(r, text='enter new password', font='Ariel 10 bold', fg='black').grid()
    p = Entry(r,textvariable=pw,show='*')
    p.grid()
    def log():
        if content == e.get():
            dbase = sqlite3.connect('history.db')  # Open a database File
            dbase.execute(''' CREATE TABLE IF NOT EXISTS game_records(
                LOGIN TEXT PRIMARY KEY NOT NULL,
                PASSWORD NOT NULL) ''')
            def insert_record(LOGIN, PASSWORD):
                dbase.execute(''' INSERT INTO game_records(LOGIN,PASSWORD)
                        VALUES(?,?)''', (LOGIN, PASSWORD))
                dbase.commit()
            insert_record(l.get(),p.get())
            dbase.close()
        tkinter.messagebox.showinfo('OTP','you have changed your user and password')
    Button(r,text='login',command=log,font='Ariel 10 bold', fg='black').grid()
    r.mainloop()
"""
def exitc():
    strTime = datetime.datetime.now().strftime('%H:%M:%S')
    f = open('file.txt','a')
    f.write(f'App closing time:{strTime}')
    f.close()
    exit()
def history():
    def clear1():
        #r = Tk()
        #ue = StringVar()
        #pwd = StringVar()
        #Label(r, text='User Name', font='Ariel 20 bold', fg='black').grid(row=1, column=0)
        #ue1 = Entry(r, textvariable=ue, bd=5)
        #ue1.grid(row=1, column=2)
        #Label(r, text='Password', font='Ariel 20 bold', fg='black').grid(row=2, column=0)
        #pwd1 = Entry(r, textvariable=pwd, bd=5, show='*')
        #pwd1.grid(row=2, column=2)

        dbase = sqlite3.connect('history.db')
        def read_Data():
            f = open('file.txt', 'r+')
            f.truncate(0)
            f.close()
            tkinter.messagebox.showinfo('History', 'History cleared')
        read_Data()
        dbase.close()
        #def clear():
            #ue1.delete(0, len(ue1.get()))
            #pwd1.delete(0, len(pwd1.get()))
        #Button(r, text='Login', font='Ariel 15 bold', fg='black', command=login).grid(row=3, column=0)
        #Button(r, text='Clear', font='Ariel 15 bold', fg='black', command=clear).grid(row=3, column=2)
        #Button(r, text='Forgot password', font='Ariel 15 bold', fg='black', command=fp).grid(row=4,column=2)
        #r.mainloop()
    r = Tk()

    with open('file.txt','r') as f:
        content = f.read()
    Label(r,text=content,font='Ariel 15 bold',fg='black').pack()
    f.close()
    Button(r,text='Clear History',font='Ariel 15 bold',fg='black',command=clear1).pack()
    r.mainloop()
logo = PhotoImage(file='s1.png')
logo1 = PhotoImage(file='lll.png')
logo2 = PhotoImage(file='ponglogo.png')
logo3 = PhotoImage(file='ssl1.png')
logo4 = PhotoImage(file='car1.png')
if hour > 21 and hour < 25 or hour > 0 and hour < 9:
    clock = Label(root, font=("times", 18, "bold"), bg="black",fg='white')
    clock.grid(row=0, column=0)
    tick()
    Button(root,text='History',font='Ariel 15 bold',fg='white',bg='black',command=history).grid(row=1,column=2)
elif hour > 10 and hour < 22:
    clock = Label(root, font=("times", 18, "bold"), bg="black",fg='white')
    clock.grid(row=0, column=0)
    tick()
    Button(root,text='History',font='Ariel 12 bold',fg='white',bg='black',height=2,width=5,command=history).grid(row=0,column=2)
    Button(root,command=snakegame.play,image=logo,height=100,width=100).grid(row=1,column=0)
    Label(root,text='Snake',font='Ariel 20 bold',fg='white',bg='black').grid(row=2,column=0)
    Button(root,command=tictactoe.playc,image=logo1,height=100,width=100).grid(row=1,column=2)
    Label(root,text='TicTacToe',font='Ariel 20 bold',fg='white',bg='black').grid(row=2,column=2)
    Button(root,command=backend.pong,image=logo2,height=100,width=100).grid(row=1,column=3)
    Label(root,text='Pong',font='Ariel 20 bold',fg='white',bg='black').grid(row=2,column=3)
    Button(root,command=spaceinvader.pp,image=logo3,height=100,width=100).grid(row=1,column=4)
    Label(root,text='Space invader',font='Ariel 20 bold',fg='white',bg='black').grid(row=2,column=4)
    Button(root,command=exitc,text='Exit',font='Ariel 25 bold',fg='white',bg='black',height=1,width=5).grid(row=3,column=3)
    Button(root, command=carracec.play, image=logo4, height=100, width=100).grid(row=1, column=5)
    Label(root, text='Car race', font='Ariel 20 bold', fg='white', bg='black').grid(row=2, column=5)
root.mainloop()
