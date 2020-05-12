from tkinter import *
from numpy import *
from sqlite3 import *
import pyperclip as ppc
import datetime



class Calculator:

    def __init__(self):
        self.eqn = ""
        self.time_ = str(datetime.datetime.now())
        self.root = Tk()
        p1 = PhotoImage(file=r'calc.png')
        self.root.iconphoto(True,p1)
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()
        try:
            self.cursor1.execute(''' create table calcsa (Equation varchar(200) , Timing varchar(15) , Date date )''')

        except:
            pass

        self.conn.commit()
        self.cursor1.close()

        #                           -----------------------------------  Menu Bar -----------------------------
        menubar = Menu(self.root)
        #                   -----------------------------------  View    ------------------------------

        viewmenu = Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Standard", command=self.standard)
        viewmenu.add_command(label="Scientific", command=self.scientific)

        viewmenu.add_separator()

        viewmenu.add_command(label="Exit", command=self.root.destroy)
        menubar.add_cascade(label="View", menu=viewmenu)

        #                   -----------------------------------  Edit    ------------------------------
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Copy", command=lambda: ppc.copy(self.eqn))
        editmenu.add_command(label="Paste", command=self.pasting)

        editmenu.add_separator()

        editmenu.add_command(label="History", command=self.history)
        menubar.add_cascade(label="Edit", menu=editmenu)
        #                   -----------------------------------  Help    ------------------------------
        headmen = Menu(menubar, tearoff=0)
        headmen.add_command(label="About", command=self.root.destroy)

        menubar.add_cascade(label="Help", menu=headmen)
        self.root.configure(bg="skyblue2", menu=menubar)

    def scientific(self):
        Label(self.root, )
        self.root.geometry("450x369")
        self.root.minsize(450, 369)
        self.root.maxsize(450, 369)
        self.root.title("CALCULATOR")
        self.val1 = StringVar()
        self.val2 = StringVar()

        bg_button = "white"
        reliefs = "raised"
        active = "gray87"
        width_button = 3
        height_button = 39
        differ = 54
        font_ = ("Seoge UI semibold", 15)
        font_2 = ("Seoge UI semibold", 12)
        cursor_ = "hand2"

        x1 = 392
        y1 = 92

        Label(self.root, bd=0, font=("Seoge UI semibold", 17), bg="skyblue2",
              relief="groove").place(x=0, y=0, width=435, height=350)
        Entry(self.root, textvariable=self.val2, bd=2, font=("Seoge UI semibold", 17), bg="white", justify="right",
              relief="groove", cursor="arrow").place(x=8, y=10, width=436, height=75)
        Entry(self.root, textvariable=self.val1, bd=0, font=("Seoge UI semibold", 17), justify="right", relief="groove",
              cursor="arrow", bg="white").place(x=9, y=38, width=426, height=45)
        Entry(self.root, textvariable=self.val2, bd=0, font=("Seoge UI semibold", 17), bg="white", justify="right",
              relief="groove",
              cursor="arrow").place(x=9, y=11, width=426, height=40)

        #                            -------------------------------- COLUMN-1 ----------------------

        Button(self.root, text="√", command=lambda: self.sqrtroot(), cursor=cursor_, font=font_,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button).place(x=x1, y=y1, height=height_button)
        Button(self.root, text="%", command=lambda: self.percent(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 45, height=height_button)
        Button(self.root, text="1/x", command=lambda: self.dividebyx(), cursor=cursor_, font=font_,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 90, height=height_button)
        Button(self.root, text="=", command=lambda: self.equal(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 135, height=height_button + 44)

        #                                -------------------- COLUMN-2 -----------------------------------

        x2 = x1 - differ
        Button(self.root, text="±", command=lambda: self.plus_minus(), cursor=cursor_, font=font_,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1, height=height_button)
        Button(self.root, text="/", command=lambda: self.cal("/"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 45, height=height_button)
        Button(self.root, text="*", command=lambda: self.cal("*"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 90, height=height_button)
        Button(self.root, text="-", command=lambda: self.cal("-"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 135, height=height_button)
        Button(self.root, text="+", command=lambda: self.cal("+"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 180, height=height_button)

        #                              ------------------------ COLUMN-3 -----------------------------------

        x3 = x2 - differ
        Button(self.root, text="C", command=lambda: self.clear(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x3, y=y1, height=height_button)
        Button(self.root, text="9", command=lambda: self.cal("9"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 45, height=height_button)
        Button(self.root, text="6", command=lambda: self.cal("6"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 90, height=height_button)
        Button(self.root, text="3", command=lambda: self.cal("3"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 135, height=height_button)
        Button(self.root, text=".", command=lambda: self.cal("."), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 180, height=height_button)

        #            ---------------------------- COLUMN-4 & 5 ----------------------

        x4 = x3 - differ
        x5 = x4 - (differ - 2)
        Button(self.root, text="←", command=lambda: self.back(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 5).place(x=x5, y=y1, height=height_button)
        Button(self.root, text="8", command=lambda: self.cal("8"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 45, height=height_button)
        Button(self.root, text="5", command=lambda: self.cal("5"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 90, height=height_button)
        Button(self.root, text="2", command=lambda: self.cal("2"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 135, height=height_button)
        Button(self.root, text="0", command=lambda: self.cal("0"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 5).place(x=x5, y=y1 + 180, height=height_button)
        Button(self.root, text="7", command=lambda: self.cal("7"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 45, height=height_button)
        Button(self.root, text="4", command=lambda: self.cal("4"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 90, height=height_button)
        Button(self.root, text="1", command=lambda: self.cal("1"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 135, height=height_button)

        #               ------------------------- COLUMN-6 & 7 & 8 -------------------------

        x6 = x5 - differ
        x7 = x6 - differ
        x8 = x7 - differ

        Button(self.root, text="Cil", command=lambda: self.cil(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x6, y=y1, height=height_button)
        Button(self.root, text="Flr", command=lambda: self.flr(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x6, y=y1 + 45, height=height_button)
        Button(self.root, text="Rnd", command=lambda: self.round_(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x6, y=y1 + 90, height=height_button)
        Button(self.root, text="LCM", command=lambda: self.lcm_(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x6, y=y1 + 135, height=height_button)
        Button(self.root, text="10^x", command=lambda: self.cal("10**"), cursor=cursor_,
               font=font_2, activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x6, y=y1 + 180, height=height_button)
        Button(self.root, text="cos", command=lambda: self.cosine(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x7, y=y1, height=height_button)
        Button(self.root, text="sin", command=lambda: self.sine(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x7, y=y1 + 45, height=height_button)
        Button(self.root, text="tan", command=lambda: self.tangent(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x7, y=y1 + 90, height=height_button)
        Button(self.root, text="e^x", command=lambda: self.e_power_x(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x7, y=y1 + 135, height=height_button)
        Button(self.root, text="x^y", command=lambda: self.cal("**"), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x7, y=y1 + 180, height=height_button)
        Button(self.root, text="log", command=lambda: self.log_(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x8, y=y1, height=height_button)
        Button(self.root, text="log10", command=lambda: self.log10_(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x8, y=y1 + 45, height=height_button)
        Button(self.root, text="log2", command=lambda: self.log2_(), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x8, y=y1 + 90, height=height_button)
        Button(self.root, text="n!", command=lambda: self.fact(), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x8, y=y1 + 135, height=height_button)
        Button(self.root, text="x^2", command=lambda: self.cal("**2"), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button, relief=reliefs,
               width=width_button + 1).place(x=x8, y=y1 + 180, height=height_button)
        Button(self.root, text="Mod", command=lambda: self.cal("%"), cursor=cursor_, font=font_2,
               activebackground=active, bg=bg_button,
               relief=reliefs, width=width_button + 1).place(x=x8, y=y1 + 225, height=height_button)
        Button(self.root, text="π", command=lambda: self.cal("3.14159265358979323846264"), cursor=cursor_, font=font_2, activebackground=active, bg=bg_button,
               relief=reliefs, width=width_button + 1).place(x=x6, y=y1 + 225, height=height_button)
        Button(self.root, text=",", command=lambda: self.cal(","), cursor=cursor_, font=font_2, activebackground=active,
               bg=bg_button,
               relief=reliefs, width=width_button + 1).place(x=x7, y=y1 + 225, height=height_button)

        #  -------------------------------------- LABEL ----------------------------------------------------------------

        Label(self.root,text = "* Cil = Ceil", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x5+4, y=y1+226)
        Label(self.root, text="* Flr = Floor", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x3-24, y=y1 + 226)
        Label(self.root, text="* Rnd = Round", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x2+9, y=y1 + 226)
        Label(self.root, text="* sin = sine", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x5 + 4, y=y1 + 246)
        Label(self.root, text="* cos = cosine", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x3 - 24, y=y1 + 246)
        Label(self.root, text="* tan = tangent", bd=0, font=("Seoge UI semibold", 10), fg="white", bg="skyblue2",
              relief="groove").place(x=x2 + 9, y=y1 + 246)




        self.root.mainloop()

    def standard(self):
        self.root.geometry("290x330")
        self.root.minsize(290, 330)
        self.root.maxsize(290, 330)
        self.root.title("CALCULATOR")
        self.val1 = StringVar()
        self.val2 = StringVar()

        bg_button = "white"
        reliefs = "raised"
        active = "gray87"
        width_button = 4
        height_button = 40
        differ = 54
        font_ = ("Seoge UI bold", 13)
        font_2 = ("Seoge UI bold", 12)
        cursor_ = "hand2"
        _cursor_ = "arrow"

        x1 = 228
        y1 = 96

        Label(self.root, bd=0, font=("Seoge UI semibold", 17), bg="skyblue2",
              relief="groove").place(x=0, y=0, width=435, height=350)
        Entry(self.root, textvariable=self.val2, bd=2, font=("Seoge UI semibold", 17), bg="white", justify="right",
              relief="groove", cursor=_cursor_).place(x=8, y=10, width=273, height=75)
        Entry(self.root, textvariable=self.val1, bd=0, font=("Seoge UI semibold", 17), justify="right", relief="groove",
              cursor=_cursor_, bg="white").place(x=9, y=38, width=263, height=45)
        Entry(self.root, textvariable=self.val2, bd=0, font=("Seoge UI semibold", 17), bg="white", justify="right",
              relief="groove",
              cursor=_cursor_).place(x=9, y=11, width=263, height=40)

        #                            -------------------------------- COLUMN-1 ----------------------

        Button(self.root, text="√", command=lambda: self.sqrtroot(), cursor=cursor_, font=font_,
               activebackground=active, bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x1, y=y1, height=height_button)
        Button(self.root, text="%", command=lambda: self.percent(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 45, height=height_button)
        Button(self.root, text="1/x", command=lambda: self.dividebyx(), cursor=cursor_, font=font_,
               activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 90, height=height_button)
        Button(self.root, text="=", command=lambda: self.equal(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x1, y=y1 + 135, height=height_button + 44)

        #                                -------------------- COLUMN-2 -----------------------------------

        x2 = x1 - differ
        Button(self.root, text="±", command=lambda: self.plus_minus(), cursor=cursor_, font=font_,
               activebackground=active,
               bg=bg_button, relief=reliefs,
               width=width_button).place(x=x2, y=y1, height=height_button)
        Button(self.root, text="/", command=lambda: self.cal("/"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 45, height=height_button)
        Button(self.root, text="*", command=lambda: self.cal("*"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 90, height=height_button)
        Button(self.root, text="-", command=lambda: self.cal("-"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 135, height=height_button)
        Button(self.root, text="+", command=lambda: self.cal("+"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x2, y=y1 + 180, height=height_button)

        #                              ------------------------ COLUMN-3 -----------------------------------

        x3 = x2 - differ
        Button(self.root, text="C", command=lambda: self.clear(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x3, y=y1, height=height_button)
        Button(self.root, text="9", command=lambda: self.cal("9"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 45, height=height_button)
        Button(self.root, text="6", command=lambda: self.cal("6"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 90, height=height_button)
        Button(self.root, text="3", command=lambda: self.cal("3"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 135, height=height_button)
        Button(self.root, text=".", command=lambda: self.cal("."), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x3, y=y1 + 180, height=height_button)

        #            ---------------------------- COLUMN-4 & 5 ----------------------

        x4 = x3 - differ
        x5 = x4 - (differ - 2)
        Button(self.root, text="←", command=lambda: self.back(), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button + 6).place(x=x5, y=y1, height=height_button)
        Button(self.root, text="8", command=lambda: self.cal("8"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 45, height=height_button)
        Button(self.root, text="5", command=lambda: self.cal("5"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 90, height=height_button)
        Button(self.root, text="2", command=lambda: self.cal("2"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x4, y=y1 + 135, height=height_button)
        Button(self.root, text="0", command=lambda: self.cal("0"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button + 6).place(x=x5, y=y1 + 180, height=height_button)
        Button(self.root, text="7", command=lambda: self.cal("7"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 45, height=height_button)
        Button(self.root, text="4", command=lambda: self.cal("4"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 90, height=height_button)
        Button(self.root, text="1", command=lambda: self.cal("1"), cursor=cursor_, font=font_, activebackground=active,
               bg=bg_button,
               relief=reliefs,
               width=width_button).place(x=x5, y=y1 + 135, height=height_button)

        # self.val1.set("0")
        self.root.mainloop()

    def cal(self, value):
        self.eqn += value

        if "%" in self.eqn or "%" in value:
            temp = self.eqn
            self.val1.set(temp.replace("%", "Mod"))
            print(temp)

        else:
            pass
            #self.val1.set(self.eqn)
        print(self.eqn)

    def clear(self):
        self.eqn = ""
        self.val1.set(self.eqn)
        self.val2.set(self.eqn)
        # self.val1.set("0")

    def back(self):
        self.eqn = self.eqn[: len(self.eqn) - 1]
        self.val1.set(self.eqn)

    def equal(self):
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()
        print("eqn:" , self.eqn)
        if len(self.eqn) <= 35:
            try:
                if len(self.val1.get()) != 0:
                    print(self.val1.get())
                    values_ = self.val1.get()
                    if "Mod" in values_:
                        values_=values_.replace("Mod","%")
                else:
                    values_ = self.eqn

                ans = eval(str(values_))
                self.val2.set(values_ + " = ")
                self.val1.set(str(ans))
                self.eqn = str(ans)

            except ZeroDivisionError:
                self.val1.set("Cannot divide by zero")
        else:
            self.val1.set("Maximum limit")
        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             [values_ + '=' + str(ans), self.time_[11:19], self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()

    def lcm_(self):
        values_ = self.eqn.split(",")
        _list_ = [int(i) for i in values_ if i.isdigit()]
        print(_list_)
        ans = lcm.reduce(_list_)
        self.val2.set("LCM of (" + self.eqn + ") = ")
        self.val1.set(str(ans))

        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["LCM({})".format(self.eqn) + '=' + str(ans), self.time_[11:19], self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(ans)

    def plus_minus(self):
        ans = (-1) * eval(self.eqn)
        self.val1.set(str(ans))
        self.eqn = str(ans)

    def sqrtroot(self):
        self.val1.set((eval(self.eqn)) ** 0.5)

        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["sqrt({})".format(self.eqn) + '=' + str((eval(self.eqn)) ** 0.5), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str((eval(self.eqn)) ** 0.5)

    def dividebyx(self):
        self.val2.set("1/" + self.eqn + " = ")
        self.val1.set(str(eval(str("1/" + self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["1/" + self.eqn + '=' + str((eval(str("1/" + self.eqn)))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(eval(str("1/" + self.eqn)))

    def percent(self):
        values_ = self.eqn
        index_ = str()
        print(values_)
        if "+" in values_:
            values_ = values_.replace("+","*")
            index_ = values_.index("*")
            per = eval(values_)/100
            values_ = values_[:index_]+"+"+str(per)
            self.val1.set(values_)
            self.eqn = values_
            print(values_)

        if "-" in values_:
            values_ = values_.replace("-","*")
            index_ = values_.index("*")
            per = eval(values_) / 100
            values_ = values_[:index_] + "-" + str(per)
            self.val1.set(values_)
            self.eqn = values_

        if "*" in values_:
            values_ = values_.replace("*","*")
            index_ = values_.index("*")
            per = eval(values_) / 100
            values_ = values_[:index_] + "*" + str(per)
            self.val1.set(values_)
            self.eqn = values_

        if "/" in values_:
            values_ = values_.replace("/","*")
            index_ = values_.index("*")
            per = eval(values_) / 100
            values_ = values_[:index_] + "/" + str(per)
            self.val1.set(values_)
            self.eqn = values_

    def round_(self):
        self.val2.set("Round of " + self.eqn + " is ")
        self.val1.set(str(round(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["Round({})".format(self.eqn) + '=' + str(round(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(round(eval(self.eqn)))

    def cil(self):
        self.val2.set("Ceil of " + self.eqn + " is ")
        self.val1.set(str(ceil(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["ceil({})".format(self.eqn) + '=' + str(ceil(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(ceil(eval(self.eqn)))

    def flr(self):
        self.val2.set("Floor of " + self.eqn + " is ")
        self.val1.set(str(floor(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["Floor({})".format(self.eqn) + '=' + str(floor(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(floor(eval(self.eqn)))

    def log_(self):
        self.val2.set("Log of " + self.eqn + " is ")
        self.val1.set(str(log(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["Log2({})".format(self.eqn) + '=' + str(log(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(log(eval(self.eqn)))

    def log10_(self):
        self.val2.set("Log10 of " + self.eqn + " is ")
        self.val1.set(str(log10(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["Log10({})".format(self.eqn) + '=' + str(log10(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(log10(eval(self.eqn)))

    def log2_(self):
        self.val2.set("Log2 of " + self.eqn + " is ")
        self.val1.set(str(log2(eval(self.eqn))))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["Log2({})".format(self.eqn) + '=' + str(log2(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(log2(eval(self.eqn)))

    def fact(self):
        n = self.eqn

        def factorial_(n):

            if float(n) <= 1:
                return 1
            else:
                return n * factorial_(n - 1)

        self.val1.set(str(factorial_(eval(self.eqn))))
        self.val2.set("fact ({})".format(self.eqn))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["factorial({})".format(self.eqn) + '=' + str(factorial_(eval(self.eqn))),
                              self.time_[11:19], self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(factorial_(eval(self.eqn)))

    def cosine(self):
        self.val1.set(str(cos(eval(self.eqn))))
        self.val2.set("cosine of ({})".format(self.eqn))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["cosine({})".format(self.eqn) + '=' + str(cos(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(cos(eval(self.eqn)))

    def sine(self):
        self.val1.set(str(sin(eval(self.eqn))))
        self.val2.set("sine of ({})".format(self.eqn))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["sine({})".format(self.eqn) + '=' + str(sin(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(sin(eval(self.eqn)))

    def tangent(self):
        self.val1.set(str(tan(eval(self.eqn))))
        self.val2.set("tangent of ({})".format(self.eqn))
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["tangent({})".format(self.eqn) + '=' + str(tan(eval(self.eqn))), self.time_[11:19],
                              self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(tan(eval(self.eqn)))

    def e_power_x(self):
        e = 2.718281828459045
        ans = (e) ** eval(self.eqn)
        self.val1.set(str(ans))
        self.val2.set("e ^ " + self.eqn)
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()

        self.cursor1.execute("insert into calcsa values(?,?,?)",
                             ["e ^ " + self.eqn + '=' + str(ans), self.time_[11:19], self.time_[:10]])
        for i in self.cursor1.execute("select * from calcsa"):
            print(i)
        self.conn.commit()
        self.conn.close()
        self.eqn = str(ans)

    def pasting(self):
        self.eqn = ppc.paste()
        self.val1.set(ppc.paste())

    def history(self):
        self.conn = connect("calculator.db")
        self.cursor1 = self.conn.cursor()
        self.hist = Tk()
        self.hist.title("History")
        self.hist.maxsize(400, 430)
        self.hist.minsize(400, 430)
        self.hist.geometry("400x430")

        scrollbar = Scrollbar(self.hist, cursor ="hand2")
        scrollbar.pack(side=RIGHT, fill=Y)
        mylist = Listbox(self.hist, yscrollcommand=scrollbar.set, width=83, height=43)
        self.cursor1.execute("select * from calcsa")
        data = self.cursor1.fetchall()
        
        for i in range(len(data)-1,-1,-1):

            mylist.insert(END, "Date : "+data[i][2], "Equation : "+data[i][0], "\t\t")

        mylist.pack()
        scrollbar.config(command=mylist.yview)
        mainloop()


x = Calculator()
x.standard()
