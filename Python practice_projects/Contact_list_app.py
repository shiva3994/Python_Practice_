#empty disctonary to store contact details

contacts = {}

while True:
    print("\n Contact Book App")
    print('1. Add Contact')
    print('2. View Contacts')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contact')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input("Enter your choice = ")

    if choice == '1':
        name = input("Enter contact name = ")
        if name in contacts:
            print(f'Contact name{name} already exists!')
        else:
            age = input('Enter age = ')
            email = input('Enter your email = ')
            mobile = input('Enter mobile number = ')
            contacts[name] = {'age':int(age),'email':email,'mobile':mobile}
            print(f'Contact name {name} has been created sucessfully!')

    elif choice == "2":
        name = input('Enter contact name to view = ')
        if name in contacts:
            contacts = contacts[name]
            print(f'Name: {name}, Age: {age}, Mobile Number: {mobile}')
        else:
            print('Contact not found!')

    elif choice == "3":
        name = input('Enter name to update contact = ')
        if name is contacts:
            age = input('Enter updated age = ')
            email = input('Enter update email = ')
            mobile = input('Enter update mobile number = ')
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
        else:
            print('Contact not found!')
    
    elif choice == "4":
        name = input('Enter contact name to delete = ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} has been deleted susessfully!')
        else:
            print('Conact not found')

    elif choice == "5":
        search_name = input('Enter contact name to search = ')
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'Found - name{name}, Age:{age}, Mobile Number:{mobile}, Email:{email}')
                found = True
        if not found:
            print('No contact found with that name')

    elif choice == "6":
        print(f'Total contacts in your book: {len(contacts)}')

    elif choice == "7":
        print('Good bye.. closing the program')

    else:
        print('Invalid input')