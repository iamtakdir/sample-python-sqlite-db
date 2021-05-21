from database import*


menu= """Please select one of the following Options :
1) Add new Note .
2) View Notes .
3) Exit .

Your Selection """

def new_entry():
    entry_note = input(" What you have learnt today ? - ")
    entry_date = input("Enter the date - ")
    add_entry(entry_note, entry_date)

def view_entries(entries):
    for entry in entries:
        print (f"{entry['date']} \n {entry['note']} \n\n")

create_table()


while (user_input:= input(menu)) != '3':
    if user_input=="1":
        new_entry()
        

    elif user_input =='2':
        view_entries(get_entry())

    else:
        print ("invalid option please enter again")

