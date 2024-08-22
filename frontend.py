from tkinter import *
import backend



def clear_list():
    list1.delete(0, END) 
    
    
def fill_list(books):
    for book in books:
        list1.insert(END, book) 


window = Tk()
window.title("Book Stor")


#Label

l1 = Label(window, text= "Title")
l1.grid(row= 0, column= 0)

l2 = Label(window, text= "Author")
l2.grid(row= 0, column= 2)

l3 = Label(window, text= "Year")
l3.grid(row= 1, column= 0)

l4 = Label(window, text= "ISBN")
l4.grid(row= 1, column= 2)


#Entreis

title_text = StringVar()
autor_text = StringVar()
year_text = StringVar()
isbn_text = StringVar()


entry1 = Entry(window, textvariable= title_text)
entry1.grid(row= 0, column= 1)

entry2 = Entry(window, textvariable= autor_text)
entry2.grid(row= 0, column= 3)

entry3 = Entry(window, textvariable= year_text)
entry3.grid(row= 1, column= 1)

entry4 = Entry(window, textvariable= isbn_text)
entry4.grid(row= 1, column= 3)


list1 = Listbox(window, width= 35, height= 6)
list1.grid(row= 2, column= 0, rowspan= 6, columnspan= 2)

sb1 = Scrollbar(window)
sb1.grid(row= 2, column= 2, rowspan= 6)

list1.configure(yscrollcommand= sb1.set)
sb1.configure(command= list1.yview)



def get_selecter_row(event):
    global selected_book
    index = list1.curselection()[0]
    selected_book = list1.get(index)
    #title
    entry1.delete(0, END)
    entry1.insert(END, selected_book[1])
    #autor
    entry2.delete(0, END)
    entry2.insert(END, selected_book[2])
    #year
    entry3.delete(0, END)
    entry3.insert(END, selected_book[3])
    #isbn
    entry4.delete(0, END)
    entry4.insert(END, selected_book[4])
    
    
list1.bind("<<ListboxSelect>>", get_selecter_row)


def view_commnad():
    clear_list()
    books = backend.view()
    fill_list(books)
    

b1 = Button(window, text= "View All", width= 12, command= lambda : view_commnad())
b1.grid(row= 2, column= 3)


def search_command():
    clear_list()
    books = backend.search(title_text.get(), autor_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)
    

b2 = Button(window, text= "Search Entry", width= 12, command= lambda: search_command())
b2.grid(row= 3, column= 3)


def add_command():
    backend.insert(title_text.get(), autor_text.get(), year_text.get(), isbn_text.get())
    view_commnad()

b3 = Button(window, text= "Add Entry", width= 12, command= lambda: add_command())
b3.grid(row= 4, column= 3)


def update_command():
    backend.update(selected_book[0], title_text.get(), autor_text.get(), year_text.get(), isbn_text.get())
    view_commnad()
    

b4 = Button(window, text= "Update Selected", width= 12, command= lambda: update_command())
b4.grid(row= 5, column= 3)


def delete_command():
    backend.delete(selected_book[0])
    view_commnad()

b5 = Button(window, text= "Delete Seleted", width= 12, command= lambda: delete_command())
b5.grid(row= 6, column= 3)

b6 = Button(window, text= "Close", width= 12, command= window.destroy)
b6.grid(row= 7, column= 3)


window.mainloop()