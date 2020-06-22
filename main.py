import tkinter
from subprocess import call
import os

root = tkinter.Tk()
root.title("Fairfield Inn Hotel")
root.geometry('1920x1080')
root.configure(bg='black')  


def click_checkin():
    call(["python", "checkin.py"])
def click_list():
    call(["python", "guest_list.py"])
def click_checkout():
    call(["python", "checkout.py"])
def click_getinfo():
    call(["python","info.py"])         


Frame1 = tkinter.Frame(root)
Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
Frame1.configure(borderwidth="2")
Frame1.configure(background="#d9d9d9")
Frame1.configure(highlightbackground="#d9d9d9")
Frame1.configure(highlightcolor="black")
Frame1.configure(width=925)

Button2 = tkinter.Button(Frame1)
Button2.place(relx=0.18, rely=0.17, height=103, width=566)
Button2.configure(activebackground="#d9d9d9")
Button2.configure(activeforeground="#000000")
Button2.configure(background="#d9d9d9")
Button2.configure(disabledforeground="#bfbfbf")
Button2.configure(foreground="#000000")
Button2.configure(highlightbackground="#d9d9d9")
Button2.configure(highlightcolor="black")
Button2.configure(pady="0")
Button2.configure(text='''1.CHECK INN''')
Button2.configure(width=566)
Button2.configure(command=click_checkin)

Button3 =tkinter.Button(Frame1)
Button3.place(relx=0.18, rely=0.33, height=93, width=566)
Button3.configure(activebackground="#d9d9d9")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#d9d9d9")
Button3.configure(disabledforeground="#bfbfbf")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''2.SHOW GUEST LIST''')
Button3.configure(width=566)
Button3.configure(command=click_list)

Button4 = tkinter.Button(Frame1)
Button4.place(relx=0.18, rely=0.47, height=93, width=566)
Button4.configure(activebackground="#d9d9d9")
Button4.configure(activeforeground="#000000")
Button4.configure(background="#d9d9d9")
Button4.configure(disabledforeground="#bfbfbf")
Button4.configure(foreground="#000000")
Button4.configure(highlightbackground="#d9d9d9")
Button4.configure(highlightcolor="black")
Button4.configure(pady="0")
Button4.configure(text='''3.CHECK OUT''')
Button4.configure(width=566)
Button4.configure(command=click_checkout)
        
Button5 = tkinter.Button(Frame1)
Button5.place(relx=0.18, rely=0.61, height=103, width=566)
Button5.configure(activebackground="#d9d9d9")
Button5.configure(activeforeground="#000000")
Button5.configure(background="#d9d9d9")
Button5.configure(disabledforeground="#bfbfbf")
Button5.configure(foreground="#000000")
Button5.configure(highlightbackground="#d9d9d9")
Button5.configure(highlightcolor="black")
Button5.configure(pady="0")
Button5.configure(text='''4.GET INFO OF ANY GUEST''')
Button5.configure(width=566)
Button5.configure(command=click_getinfo)
        
Button6 = tkinter.Button(Frame1)
Button6.place(relx=0.18, rely=0.77, height=103, width=566)
Button6.configure(activebackground="#d9d9d9")
Button6.configure(activeforeground="#000000")
Button6.configure(background="#d9d9d9")
Button6.configure(disabledforeground="#bfbfbf")
Button6.configure(foreground="#000000")
Button6.configure(highlightbackground="#d9d9d9")
Button6.configure(highlightcolor="black")
Button6.configure(pady="0")
Button6.configure(text='''5.EXIT''')
Button6.configure(width=566)
Button6.configure(command=quit)



root.mainloop()