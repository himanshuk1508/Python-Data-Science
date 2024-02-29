contacts={'police':112, 'emergency':101,}

while True:
    name=input('🔎search any contacts:')
    #closing the program
    if len(name)==0:
        print("👋Bye")
        break

    #searching the contacts
    if name in contacts:
        print(f"📞{name}:{contacts[name]}")
    elif name=='all':
        for name,numbers in contacts.items():
            print(f"📞 {name}:{numbers}")
        print('-'*20)
    else:
        print(f" {name} not found")
        ch=input('🤔 Want to add contact? (y/n):')
        if ch=="y":
            numbers=input("📞 Enter Contact:")
            contacts[name]=numbers
            print(f'👍 {name} added to contatcs')
            print('-'*20)


