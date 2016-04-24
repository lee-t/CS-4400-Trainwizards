#!/usr/bin/python

from Tkinter import *

root = Tk()
root.geometry("600x400")
root.title("Login")

def Enter():
	text_contents = text.get()
	listbox.insert(END, text_contents)
	text.delete(0,END)

def Remove():
	listbox.delete(ANCHOR)	

def Save():
	f = file("notes.db", "wb")	
	notes = listbox.get(0, END)
	pickle.dump(notes, f)

def ReturnInsert(event):
	Enter()

def DeleteCurrent(event):
	Remove()

def CopyToText(event):
	text.delete(0, END)
	current_note = listbox.get(ANCHOR)
	text.insert(0, current_note)

textframe = Frame(root)

enter_button = Button(textframe, text="Enter", command = Enter)
remove_button = Button(textframe, text="Remove", command = Remove)
save_button = Button(textframe, text="Save", command = Save)

text = Entry(textframe)

text.bind("<Return>", ReturnInsert)
listbox.bind("<Double-Button-3>", DeleteCurrent)
listbox.bind("<Double-Button-1>", CopyToText)

text.pack(side=LEFT, fill=X, expand=1)
enter_button.pack(side=LEFT)
remove_button.pack(side=LEFT)
save_button.pack(side=LEFT)
listbox.pack(side=LEFT,fill=BOTH, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)

textframe.pack(fill=X)
listframe.pack(fill=BOTH, expand=1)



root.mainloop()
