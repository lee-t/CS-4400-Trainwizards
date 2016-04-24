#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.7
# In conjunction with Tcl version 8.6
#    Apr 24, 2016 12:56:14 AM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import makereservation_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    makereservation_support.set_Tk_var()
    top = New_Toplevel_1 (root)
    makereservation_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel_1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    makereservation_support.set_Tk_var()
    top = New_Toplevel_1 (w)
    makereservation_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel_1():
    global w
    w.destroy()
    w = None


class New_Toplevel_1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {DejaVu Sans} -size 20 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font14 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("704x460+325+290")
        top.title("New Toplevel 1")
        top.configure(highlightcolor="black")



        self.searchtrain = Frame(top)
        self.searchtrain.place(relx=0.03, rely=0.07, relheight=0.86
                , relwidth=0.79)
        self.searchtrain.configure(relief=GROOVE)
        self.searchtrain.configure(borderwidth="2")
        self.searchtrain.configure(relief=GROOVE)
        self.searchtrain.configure(width=555)

        self.Label1-3 = Label(self.searchtrain)
        self.Label1-3.place(relx=0.34, rely=0.05, height=33, width=161)
        self.Label1-3.configure(activebackground="#f9f9f9")
        self.Label1-3.configure(font=font10)
        self.Label1-3.configure(foreground="#ffa300")
        self.Label1-3.configure(text='''Search Train''')

        self.Label2-3 = Label(self.searchtrain)
        self.Label2-3.place(relx=0.22, rely=0.23, height=18, width=90)
        self.Label2-3.configure(activebackground="#f9f9f9")
        self.Label2-3.configure(text='''Deaparts from''')

        self.Label3-3 = Label(self.searchtrain)
        self.Label3-3.place(relx=0.23, rely=0.43, height=18, width=62)
        self.Label3-3.configure(text='''Arrives At''')

        self.Label4-3 = Label(self.searchtrain)
        self.Label4-3.place(relx=0.07, rely=0.61, height=18, width=185)
        self.Label4-3.configure(text='''Departure Date (DD/MM/YYYY)''')

        self.Entrydate = Entry(self.searchtrain)
        self.Entrydate.place(relx=0.43, rely=0.61, relheight=0.05, relwidth=0.26)

        self.Entrydate.configure(background="white")
        self.Entrydate.configure(font="TkFixedFont")

        self.Scrolledlistbox1 = ScrolledListBox(self.searchtrain)
        self.Scrolledlistbox1.place(relx=0.41, rely=0.23, relheight=0.15
                , relwidth=0.14)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(width=10)

        self.Scrolledlistbox2 = ScrolledListBox(self.searchtrain)
        self.Scrolledlistbox2.place(relx=0.41, rely=0.41, relheight=0.17
                , relwidth=0.14)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(width=10)

        self.Buttonsearchtrain = Button(self.searchtrain)
        self.Buttonsearchtrain.place(relx=0.43, rely=0.71, height=26, width=92)
        self.Buttonsearchtrain.configure(activebackground="#d9d9d9")
        self.Buttonsearchtrain.configure(text='''Find Trains''')

        self.searchdeparture = Frame(self.searchtrain)
        self.searchdeparture.place(relx=0.0, rely=0.0, relheight=0.95
                , relwidth=0.98)
        self.searchdeparture.configure(relief=GROOVE)
        self.searchdeparture.configure(borderwidth="2")
        self.searchdeparture.configure(relief=GROOVE)
        self.searchdeparture.configure(width=545)

        self.Label4-4 = Label(self.searchdeparture)
        self.Label4-4.place(relx=0.31, rely=0.06, height=53, width=251)
        self.Label4-4.configure(activebackground="#f9f9f9")
        self.Label4-4.configure(font=font10)
        self.Label4-4.configure(foreground="#ffa300")
        self.Label4-4.configure(text='''Search Departure''')
        self.Label4-4.configure(width=251)

        self.Label5-4 = Label(self.searchdeparture)
        self.Label5-4.place(relx=0.09, rely=0.21, height=18, width=75)
        self.Label5-4.configure(text='''Select Train''')

        self.TCombobox1 = ttk.Combobox(self.searchdeparture)
        self.TCombobox1.place(relx=0.09, rely=0.27, relheight=0.05
                , relwidth=0.32)
        self.TCombobox1.configure(textvariable=makereservation_support.combobox)
        self.TCombobox1.configure(takefocus="")

        self.departue_time = ttk.Label(self.searchdeparture)
        self.departue_time.place(relx=0.11, rely=0.37, height=26, width=82)
        self.departue_time.configure(background=_bgcolor)
        self.departue_time.configure(foreground="#000000")
        self.departue_time.configure(relief=FLAT)
        self.departue_time.configure(textvariable=makereservation_support.deptime)
        self.departue_time.configure(width=82)

        self.tlabel = ttk.Label(self.searchdeparture)
        self.tlabel.place(relx=0.11, rely=0.35, height=16, width=29)
        self.tlabel.configure(background=_bgcolor)
        self.tlabel.configure(foreground="#000000")
        self.tlabel.configure(relief=FLAT)
        self.tlabel.configure(text='''time''')

        self.TCombobox2 = ttk.Combobox(self.searchdeparture)
        self.TCombobox2.place(relx=0.55, rely=0.27, relheight=0.05
                , relwidth=0.32)
        self.TCombobox2.configure(textvariable=makereservation_support.combobox)
        self.TCombobox2.configure(takefocus="")

        self.Label6 = Label(self.searchdeparture)
        self.Label6.place(relx=0.55, rely=0.21, height=18, width=74)
        self.Label6.configure(text='''Select class''')

        self.Label7 = Label(self.searchdeparture)
        self.Label7.place(relx=0.55, rely=0.35, height=18, width=30)
        self.Label7.configure(text='''Cost''')

        self.ticketcost = ttk.Label(self.searchdeparture)
        self.ticketcost.place(relx=0.55, rely=0.4, height=26, width=87)
        self.ticketcost.configure(background=_bgcolor)
        self.ticketcost.configure(foreground="#000000")
        self.ticketcost.configure(relief=FLAT)
        self.ticketcost.configure(textvariable=makereservation_support.depticketcost)
        self.ticketcost.configure(width=87)

        self.Buttontosearch = Button(self.searchdeparture)
        self.Buttontosearch.place(relx=0.18, rely=0.59, height=26, width=55)
        self.Buttontosearch.configure(activebackground="#d9d9d9")
        self.Buttontosearch.configure(text='''back''')

        self.Buttontoextras = Button(self.searchdeparture)
        self.Buttontoextras.place(relx=0.61, rely=0.59, height=26, width=54)
        self.Buttontoextras.configure(activebackground="#d9d9d9")
        self.Buttontoextras.configure(text='''Next''')

        self.menubar = Menu(top,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.03, rely=0.11, relheight=0.73, relwidth=0.79)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(width=555)

        self.Label8-3 = Label(self.Frame2)
        self.Label8-3.place(relx=0.11, rely=0.01, height=63, width=421)
        self.Label8-3.configure(activebackground="#f9f9f9")
        self.Label8-3.configure(font=font10)
        self.Label8-3.configure(foreground="#ffa300")
        self.Label8-3.configure(text='''Travel Extras & Passenger Info''')
        self.Label8-3.configure(width=421)

        self.TCombobox3 = ttk.Combobox(self.Frame2)
        self.TCombobox3.place(relx=0.45, rely=0.33, relheight=0.05
                , relwidth=0.21)
        self.TCombobox3.configure(textvariable=makereservation_support.combobox)
        self.TCombobox3.configure(width=117)
        self.TCombobox3.configure(takefocus="")

        self.Label9 = Label(self.Frame2)
        self.Label9.place(relx=0.16, rely=0.33, height=18, width=125)
        self.Label9.configure(text='''Number of Baggage''')

        self.Entry2 = Entry(self.Frame2)
        self.Entry2.place(relx=0.47, rely=0.45, relheight=0.06, relwidth=0.26)
        self.Entry2.configure(background="white")
        self.Entry2.configure(font="TkFixedFont")

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.18, rely=0.45, height=26, width=125)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(text='''Passenger name''')

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.16, rely=0.69, height=26, width=55)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(text='''Back''')

        self.Button6 = Button(self.Frame2)
        self.Button6.place(relx=0.59, rely=0.69, height=26, width=54)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(text='''Next''')

        self.Frame3 = Frame(top)
        self.Frame3.place(relx=0.01, rely=0.04, relheight=0.75, relwidth=0.93)
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief=GROOVE)
        self.Frame3.configure(width=655)

        self.Label10 = Label(self.Frame3)
        self.Label10.place(relx=0.11, rely=0.06, height=63, width=421)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(font=font10)
        self.Label10.configure(foreground="#ffa300")
        self.Label10.configure(text='''Make Reservation''')

        self.Label11 = Label(self.Frame3)
        self.Label11.place(relx=0.09, rely=0.2, height=22, width=144)
        self.Label11.configure(font=font14)
        self.Label11.configure(text='''Currently Selected''')

        self.style.configure('Treeview.Heading',  font="TkDefaultFont")
        self.Scrolledtreeview1 = ScrolledTreeView(self.Frame3)
        self.Scrolledtreeview1.place(relx=0.02, rely=0.26, relheight=0.31
                , relwidth=0.98)
        self.Scrolledtreeview1.configure(columns="Col1 Col2 Col3 Col4 Col5 Col6 Col7")
        self.Scrolledtreeview1.heading("#0",text="Train")
        self.Scrolledtreeview1.heading("#0",anchor="center")
        self.Scrolledtreeview1.column("#0",width="105")
        self.Scrolledtreeview1.column("#0",minwidth="20")
        self.Scrolledtreeview1.column("#0",stretch="1")
        self.Scrolledtreeview1.column("#0",anchor="w")
        self.Scrolledtreeview1.heading("Col1",text="Time")
        self.Scrolledtreeview1.heading("Col1",anchor="center")
        self.Scrolledtreeview1.column("Col1",width="105")
        self.Scrolledtreeview1.column("Col1",minwidth="20")
        self.Scrolledtreeview1.column("Col1",stretch="1")
        self.Scrolledtreeview1.column("Col1",anchor="w")
        self.Scrolledtreeview1.heading("Col2",text="Departs")
        self.Scrolledtreeview1.heading("Col2",anchor="center")
        self.Scrolledtreeview1.column("Col2",width="106")
        self.Scrolledtreeview1.column("Col2",minwidth="20")
        self.Scrolledtreeview1.column("Col2",stretch="1")
        self.Scrolledtreeview1.column("Col2",anchor="w")
        self.Scrolledtreeview1.heading("Col3",text="Arrival")
        self.Scrolledtreeview1.heading("Col3",anchor="center")
        self.Scrolledtreeview1.column("Col3",width="106")
        self.Scrolledtreeview1.column("Col3",minwidth="20")
        self.Scrolledtreeview1.column("Col3",stretch="1")
        self.Scrolledtreeview1.column("Col3",anchor="w")
        self.Scrolledtreeview1.heading("Col4",text="Class")
        self.Scrolledtreeview1.heading("Col4",anchor="center")
        self.Scrolledtreeview1.column("Col4",width="46")
        self.Scrolledtreeview1.column("Col4",minwidth="20")
        self.Scrolledtreeview1.column("Col4",stretch="1")
        self.Scrolledtreeview1.column("Col4",anchor="w")
        self.Scrolledtreeview1.heading("Col5",text="Price")
        self.Scrolledtreeview1.heading("Col5",anchor="center")
        self.Scrolledtreeview1.column("Col5",width="50")
        self.Scrolledtreeview1.column("Col5",minwidth="20")
        self.Scrolledtreeview1.column("Col5",stretch="1")
        self.Scrolledtreeview1.column("Col5",anchor="w")
        self.Scrolledtreeview1.heading("Col6",text="# Bags")
        self.Scrolledtreeview1.heading("Col6",anchor="center")
        self.Scrolledtreeview1.column("Col6",width="48")
        self.Scrolledtreeview1.column("Col6",minwidth="20")
        self.Scrolledtreeview1.column("Col6",stretch="1")
        self.Scrolledtreeview1.column("Col6",anchor="w")
        self.Scrolledtreeview1.heading("Col7",text="Name")
        self.Scrolledtreeview1.heading("Col7",anchor="center")
        self.Scrolledtreeview1.column("Col7",width="61")
        self.Scrolledtreeview1.column("Col7",minwidth="20")
        self.Scrolledtreeview1.column("Col7",stretch="1")
        self.Scrolledtreeview1.column("Col7",anchor="w")

        self.Button7 = Button(self.Frame3)
        self.Button7.place(relx=0.2, rely=0.61, height=26, width=130)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(text='''Remove Selected''')

        self.Button8 = Button(self.Frame3)
        self.Button8.place(relx=0.11, rely=0.9, height=26, width=55)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(text='''Back''')

        self.Button9 = Button(self.Frame3)
        self.Button9.place(relx=0.27, rely=0.9, height=26, width=70)
        self.Button9.configure(activebackground="#d9d9d9")
        self.Button9.configure(text='''Submit''')

        self.Button10 = Button(self.Frame3)
        self.Button10.place(relx=0.2, rely=0.72, height=26, width=117)
        self.Button10.configure(activebackground="#d9d9d9")
        self.Button10.configure(text='''Continue''')
        self.Button10.configure(width=117)





# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=self._autoscroll(vsb),
        #    xscrollcommand=self._autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


if __name__ == '__main__':
    vp_start_gui()



