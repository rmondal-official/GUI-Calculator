# importing
from tkinter import *
from tkinter import ttk
# from ttkthemes import ThemedStyle


a_root = Tk()
a_root.geometry('320x315')
a_root.title('Calculator')
# style = ThemedStyle(a_root)
# style.set_theme("plastik")
a_root.resizable(False, False)
a = StringVar()
Label(text='').pack()
user_input1 = Entry(a_root, textvariable=a, width=25, font='calibri 18')
user_input1.pack()
user_output = Entry(a_root, width=43)
user_output.pack()


# Define functions for commands
def result():
    try:
        com_result = eval(str(a.get()))
        user_output.delete(0, END)
        user_output.insert(0, com_result)
        print(com_result)
    except Exception as e:
        print(e)
        user_output.delete(0, END)
        user_output.insert(0, 'Error')

def clean():
    user_input1.delete(0, END)
    user_output.delete(0, END)

def backspace():
    user_input1.delete(0, 1)

def click(event):
    text = event.widget.cget("text")
    user_input1.insert(10, text)


# Packing button under different frame
# Packing button under 'my_frametop' frame
my_frametop = Frame(a_root)
my_frametop.pack()
Button(my_frametop, text='=', command=result, padx=100, font='clibri 11 bold', bg='grey').pack(side=LEFT)
Label(my_frametop, text='').pack(side=LEFT)

ttk.Button(my_frametop, text='Backspace', command=backspace).pack(side=LEFT)


# Packing button under 'my_frame' frame
my_frame = Frame(a_root)
my_frame.pack()
b = ttk.Button(my_frame, text='[')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame, text=']')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame, text='{')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame, text='}')
b.pack(side=LEFT)
b.bind("<Button-1>", click)


# Packing button under 'my_frame1' frame
my_frame1 = Frame(a_root)
my_frame1.pack()
b = ttk.Button(my_frame1, text='(')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame1, text=')')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame1, text='%')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame1, text='^')
b.pack(side=LEFT)
b.bind("<Button-1>", click)


# Packing button under 'my_frame2' frame
my_frame2 = Frame(a_root)
my_frame2.pack()
b = ttk.Button(my_frame2, text='7')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame2, text='8')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame2, text='9')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame2, text='/')
b.pack(side=LEFT)
b.bind("<Button-1>", click)


# Packing button under 'my_frame3' frame
my_frame3 = Frame(a_root)
my_frame3.pack()
b = ttk.Button(my_frame3, text='4')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame3, text='5')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame3, text='6')

b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame3, text='*')
b.pack(side=LEFT)
b.bind("<Button-1>", click)


# Packing button under 'my_frame4' frame
my_frame4 = Frame(a_root)
my_frame4.pack()
b = ttk.Button(my_frame4, text='1')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame4, text='2')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame4, text='3')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame4, text='-')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
# Packing button under 'my_frame5' frame
my_frame5 = Frame(a_root)
my_frame5.pack()
b = ttk.Button(my_frame5, text='0')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame5, text='00')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame5, text='.')
b.pack(side=LEFT)
b.bind("<Button-1>", click)
b = ttk.Button(my_frame5, text='+')
b.pack(side=LEFT)
b.bind("<Button-1>", click)


# Packing button under 'my_frame6' frame
my_frame6 = Frame(a_root)
my_frame6.pack()
Button(my_frame6, text='Clear All', command=clean, padx=117, font='clibri 11 bold', bg='grey').pack(side=LEFT)


a_root.mainloop()
# finish

