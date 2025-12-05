import sys

def initial_phonebook():
    rows, cols = int(input("Please enter initial number of contacts:..")),5
    phone_book = []
    print(phone_book)
    for i in range (rows):
        print("Enter contact &d details in the following order (only):" % (i+1))
        print("Note: * indiactes mandatory field")
        temp = []
        for j in range (cols):
            if j == 0:
                temp.append(str(input("Name...")))
                if temp[j] == '' or temp[j] == ' ':
                    sys.exit("Name is a mandatory field. Process exiting due to blank field...")
            if j == 1:
                temp.append(int(input("Number...")))
            if j == 3:
                temp.append(str(input("Date of birth (dd/mm/yyyy)...")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Category (family/work/friends/other)...")))
                if temp[j] == '' or temp[j] == ' ':
                    temp[j] = None
        phone_book.append(temp)
    print(phone_book)
    return phone_book
def menu():
    print("*****************************************************")
    print("\t\t\tSMARTPHONE DICTIONARY", flush = False)
    print("\tYou can now perform the following options on this phonebook:\n")
    print("1. Add new contact.")
    print("2. Remove an existing contact.")
    print("3. Delete all contacts.")
    print("4. Search for a contact.")
    print("5. Display all contacts.")
    print("6. Exit phonebook.")

    choice = int(input("Please enter your choice..."))
    return choice
def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Name...")))
        if i == 1:
            dip.append(int(input("Number...")))
        if i == 2:
            dip.append(str(input("E-mail address...")))
        if i == 3:
            dip.append(str(input("Date of birth (dd/mm/yyyy)...")))
        if i == 4:
            dip.append(str(input("Category (family/work/friends/other)...")))
    pb.append(dip)
    return pb
def remove_existing(pb):
    query = str(input("Please enter the name of the contact you wish to remove..."))
    temp = 0