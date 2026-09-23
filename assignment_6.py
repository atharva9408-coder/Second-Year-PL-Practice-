while True:
    password = input("Enter password: ")
    if password == "stop":
        break
    l=len(password)>= 8
    u=any(i.isupper() for i in password)
    low=any(i.islower() for i in password)
    d=any(i.isdigit() for i in password)
    if l and u and low and d:
        print("Strong password!")
    else:
        print("Weak password!")