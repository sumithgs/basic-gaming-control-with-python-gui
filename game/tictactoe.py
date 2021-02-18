from tkinter import *
import tkinter.messagebox
import datetime
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)
srt = datetime.datetime.now().strftime('%H:%M:%S')

bclick = True
flag = 0
def playc():
    f = open('file.txt', 'a')
    f.write(f'Game:Tic Tac Toe,Date:{day},Month:{month},Start time:{srt}\n')
    f.close()
    root = Tk()
    root.geometry('400x200')
    root.minsize(400, 200)
    root.maxsize(400, 200)
    root.title('Tic tac toe')

    bclick = True
    flag = 0
    #logo = PhotoImage(file='lll.png')
    def play():

        roo = Tk()
        buttons = StringVar()

        def disableButton():
            b1.configure(state=DISABLED)
            b2.configure(state=DISABLED)
            b3.configure(state=DISABLED)
            b4.configure(state=DISABLED)
            b5.configure(state=DISABLED)
            b6.configure(state=DISABLED)
            b7.configure(state=DISABLED)
            b8.configure(state=DISABLED)
            b9.configure(state=DISABLED)


        def btnClick(buttons):
            global bclick, flag, pb, pa, p1, p2
            if buttons["text"] == " " and bclick == True:
                buttons["text"] = "X"
                bclick = False
                pb = pne2.get() + " Wins!"
                pa = pne1.get() + " Wins!"
                checkForWin()
                flag += 1

            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                checkForWin()
                flag += 1
            else:
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

        def checkForWin():
            if (b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
                    b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X' or
                    b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X' or
                    b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X' or
                    b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X' or
                    b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X' or
                    b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X' or
                    b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X' or
                    b7['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X'):
                disableButton()
                tkinter.messagebox.showinfo("Tic-Tac-Toe", pne1.get()+'Wins')

            elif (flag == 8):
                tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

            elif (b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
                  b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O' or
                  b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O' or
                  b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O' or
                  b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O' or
                  b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O' or
                  b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O' or
                  b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O' or
                  b7['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O'):
                disableButton()
                tkinter.messagebox.showinfo("Tic-Tac-Toe", pne2.get()+'Wins')

        label = Label(roo, text='Player1:' + pne1.get(), font='Times 15 bold', bg='white', fg='black', height=2,
                      width=11)
        label.grid(row=1, column=0)
        label = Label(roo, text="Player2:" + pne2.get(), font='Times 15 bold', bg='white', fg='black', height=2,
                      width=11)
        label.grid(row=1, column=1)

        b1 = Button(roo, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b1))
        b1.grid(row=3, column=0)
        b2 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b2))
        b2.grid(row=3, column=1)
        b3 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b3))
        b3.grid(row=3, column=2)
        b4 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b4))
        b4.grid(row=4, column=0)
        b5 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b5))
        b5.grid(row=4, column=1)
        b6 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b6))
        b6.grid(row=4, column=2)
        b7 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b7))
        b7.grid(row=5, column=0)
        b8 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b8))
        b8.grid(row=5, column=1)
        b9 = Button(roo, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
                    command=lambda: btnClick(b9))
        b9.grid(row=5, column=2)

        roo.mainloop()

    #Label(root, image=logo, height=100, width=100).grid()

    #Label(text='Tic Tac Toe', font='Times 20 bold', fg='green').grid(row=0,column=0)

    p11 = StringVar()
    p22 = StringVar()

    pn1 = Label(root, text='Player1', fg='black', font='Ariel 20 bold')
    pn1.grid(row=1,column=1)
    pne1 = Entry(root, textvariable=p11, bd=5)
    pne1.grid(row=1,column=2)
    pn2 = Label(root, text='Player2', fg='black', font='Ariel 20 bold')
    pn2.grid(row=2,column=1)
    pne2 = Entry(root, textvariable=p22, bd=5)
    pne2.grid(row=2,column=2)

    pa = StringVar()
    pb = StringVar()

    # p1 = StringVar()
    # p2 = StringVar()

    def exitc():
        return exit()

    Button(root, command=play, text='Play', font='Ariel 15').grid(row=3,column=0)
    Button(root, text='Exit', font='Ariel 15', command=exitc).grid(row=3,column=3)

    root.mainloop()
