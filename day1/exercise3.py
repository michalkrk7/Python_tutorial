username = input("Username: ")
password = input("Password: ")

length = len(password)

hidden_password = str("*" * length)

print(f"Hi, {username}! \nYour password ,{hidden_password}, is  {length} letters long")