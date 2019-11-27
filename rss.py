from tkinter import *
import sqlite3
import pyperclip
import feedparser


links = sqlite3.connect("links.db")
cursor = links.cursor()
bigdata = dict()
resource = [row[1] for row in cursor.execute("SELECT rowid, * FROM links ORDER BY adress")]


def copy_link():
	select = list(listbox.curselection())
	select = [listbox.get(i) for i in select]
	select = ' '.join(select)
	pyperclip.copy(select)

def find():
	key = entry1.get()
	for i in bigdata:
		for j in range(len(bigdata[i])):
			for k in range(3):
				if key in bigdata[i][j][k]:
					listbox.insert(END, bigdata[i][j][k])

def delete():
	select = list(listbox.curselection())
	select.reverse()
	for i in select:
		listbox.delete(i)
		string = resource.pop(i)
		sql = "DELETE FROM links WHERE adress = '%s'" % string
		cursor.execute(sql)
		links.commit()

def add_new():
	new_task = """INSERT INTO links VALUES ('%s')""" % entry2.get()
	cursor.execute(new_task)
	links.commit()
	listbox.insert(END, entry2.get())
	resource.append(entry2.get())
    

def see_all():
	global right, listbox, scroll, button7, bigdata, resource
	right.destroy()
	right = Frame(window, bg = 'yellow')
	right.grid(column = 1, row = 1, rowspan = 3)
	top = Frame(right)
	top.pack()
	listbox = Listbox(top, selectmode = EXTENDED, width = 120, height = 27)
	scroll = Scrollbar(top, command = listbox.yview)
	listbox.pack(side = LEFT, fill = Y)
	scroll.pack(fill = Y)
	listbox.config(yscrollcommand = scroll.set)
	button7 = Button(right, text = 'Copy', command = copy_link, bg = 'pale goldenrod', font = ('Arial', 16), fg = 'gray23')
	button7.pack(side = BOTTOM)
	for source in resource:
		feeds = feedparser.parse(source)
		bigdata[feeds['feed']['title']] = []
		for article in feeds['entries']:
			bigdata[feeds['feed']['title']].append([article['title'], article['description'], article['link']])
			listbox.insert(END, article['title'])
			listbox.insert(END, article['description'])
			listbox.insert(END, article['link'])

def find_in():
	global right, entry1, label2, label3, listbox, scroll1, button6, button8
	right.destroy()
	right = Frame(window, bg = 'yellow')
	right.grid(column = 1, row = 1, rowspan = 3, sticky = N + S + W + E)
	top = Frame(right)
	label2 = Label(right, text = 'Search for news: ', bg = 'yellow', fg = 'gray', font = ('Arial', 16))
	label3 = Label(right, text = 'Results: ', bg = 'yellow', fg = 'gray', font = ('Arial', 16), height = 2)
	entry1 = Entry(right, font = ('Arial', 16), width = 40)
	button6 = Button(right, text = 'Search', command = find, bg = 'pale goldenrod', font = ('Arial', 16), fg = 'gray23')
	listbox = Listbox(top, selectmode = EXTENDED, width = 120, height = 18)
	scroll1 = Scrollbar(top, command = listbox.yview)
	button8 = Button(right, text = 'Copy', command = copy_link, bg = 'pale goldenrod', font = ('Arial', 16), fg = 'gray23')
	label2.pack()
	entry1.pack()
	button6.pack()
	label3.pack()
	top.pack()
	listbox.pack(side = LEFT, fill = Y)
	scroll1.pack(side = LEFT, fill = Y)
	listbox.config(yscrollcommand = scroll1.set)
	button8.pack()

def add_feed():
	global right, entry2, label4, label5, listbox, scroll2, button4, button9
	right.destroy()
	right = Frame(window, bg = 'yellow')
	right.grid(column = 1, row = 1, rowspan = 3, sticky = N + S + W + E)
	label4 = Label(right, text = 'Source administration: ', bg = 'yellow', fg = 'gray', font = ('Arial', 16))
	label4.pack()
	top = Frame(right)
	top.pack()
	listbox = Listbox(top, selectmode = EXTENDED, width = 120, height = 18)
	scroll2 = Scrollbar(top, command = listbox.yview)
	listbox.pack(side = LEFT, fill = Y)
	scroll2.pack(side = LEFT, fill = Y)
	listbox.config(yscrollcommand = scroll2.set)
	bottom = Frame(right)
	bottom.pack()
	button4 = Button(bottom, text = 'Delete', command = delete, bg = 'IndianRed1', font = ('Arial', 16), fg = 'gray92')
	label5 = Label(right, text = 'Adding new source: ', bg = 'yellow', fg = 'gray', font = ('Arial', 16), height = 2)
	entry2 = Entry(right, font = ('Arial', 16), width = 40)
	button5 = Button(right, text = 'Add new source', command = add_new, bg = 'DarkOliveGreen1', font = ('Arial', 16), fg = 'gray47')
	button9 = Button(bottom, text = 'Copy', command = copy_link, bg = 'pale goldenrod', font = ('Arial', 16), fg = 'gray23')
	button5.pack(side = BOTTOM)
	button9.pack(side = LEFT)
	entry2.pack(side = BOTTOM)
	label5.pack(side = BOTTOM)
	button4.pack(side = LEFT)
	for source in resource:
		listbox.insert(END, source)


window = Tk()
window.title('RSS Reader')
window.geometry('888x516')
window['bg'] = 'yellow'


label1 = Label(window, text = 'Monnar I. S.', font = ('Arial', 16), bg = 'light yellow', fg = 'gray26', anchor = 'w', relief = RAISED)
label1.grid(column = 0, row = 0, columnspan = 2, sticky = W + E)


button1 = Button(window, text = 'Watch all', command = see_all, bg = 'khaki', font = ('Arial', 16), fg = 'black')
button2 = Button(window, text = 'Search at list', command = find_in, bg = 'khaki', font = ('Arial', 16), fg = 'black')
button3 = Button(window, text = 'Source administration', command = add_feed, bg = 'khaki', font = ('Arial', 16), fg = 'black')
button1.grid(column = 0, row = 1, sticky = N + S + W + E)
button2.grid(column = 0, row = 2, sticky = N + S + W + E)
button3.grid(column = 0, row = 3, sticky = N + S + W + E)


right = Frame()
see_all()

window.mainloop()
