#
#!/usr/bin/python3
#
#  [Program]
#
#
#
#  CalDisplay
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.



########################################################################################
########################################################################################
## # CODE LANGUAGE IS PYHTON!          ##      ##                                     ##
## # DATE: 1-JULY-2021                 ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                     ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!     ##########    #######   ##     ##   ##     ##  ##
## # GUI CALCULATOR!                   ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                    ##      ##    #######   ##     ##   ########   ##
########################################################################################
########################################################################################



from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("400x130")
root.resizable(0, 0)
root.config(bg="#142232")
root.title("CalDisplay")
image = PhotoImage(file='calculator.png')
root.iconphoto(False, image)


def About():
    tmsg.showwarning("About..", "[+] CalDisplay MADE BY HANU!\n"
                  "[+] Version 1.0\n"
                           "[+] All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")

def Refresh():
    scvalue.set("")
    Screen.update()




def join():
    reply = tmsg.askquestion("Join..", "Would You Like Join Us")
    if reply == "yes":
        tmsg.showerror("Join..", "contact us on Go To ->Github.com/HorridHanu<-\n "
                            "For More Update And Versions....")
    else:
        tmsg.showwarning("Warning..", "Without Joining you can't get Update And Versions....")



def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(scvalue.get())
            scvalue.set(value)
            Screen.update()
    elif text == "C":
        scvalue.set("")
        Screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        Screen.update()




mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)

m1.add_command(label="Refresh", command=Refresh)
m1.add_command(label="About", command=About)
m1.add_command(label="Join", command=join)
m1.add_separator()
m1.add_command(label="Exit", command=exit)
mainmenu.add_cascade(label="Help", menu=m1)
root.config(menu=mainmenu)


scvalue = StringVar()
scvalue.get()


Screen = Entry(root, text=scvalue, font = "helvetica 20", fg="black")
Screen.pack(fill=X, ipadx=10, padx=40, pady=13)


f1 = Frame(root, bg="white", relief=SUNKEN)
f1.pack()


button = Button(f1, text="C", fg="RED")
button.pack(side=LEFT, anchor="w", padx=0, pady=0)
button.bind("<Button-1>", click)


button = Button(f1, text="=", fg="RED")
button.pack(side=LEFT, anchor="w", padx=0, pady=0)
button.bind("<Button-1>", click)


root.mainloop()