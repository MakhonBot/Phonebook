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
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed.")
            return pb
    if temp == 0:
        print("Sorry, you've entered an invalid query. Please try again later.")
        return pb
def delete_all(pb):
    return pb.clear
def search_existing(pb):
    choice = int(input("Enter search criteria... \n \n \n1. Name \n2. Number \n3. E-mail \n4.DOB \n5. Category (family/work/friends/other) \nPlease enter..."))
    temp = []
    check = -1
    if choice == 1:
        query = str(input("Please enter name..."))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    
    elif choice == 2:
        query = int(input("Please enter number..."))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
        query = str(input("Please enter email..."))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
        query = str(input("Please enter DOB (dd/mm/yyyy)..."))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    
