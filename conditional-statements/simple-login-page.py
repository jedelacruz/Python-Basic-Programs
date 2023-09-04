#Login Form

username = "je"
password = "pogi"

print("============= Login Form =============")
print()
userName = input("Userame: ")
passWord = input("Password: ")
print()

if(userName == username and passWord == password):
    print("Succesfuly Login")
elif(userName == username and passWord != password):
    print("Wrong password")
elif(userName != username and passWord == password):
    print("Wrong username")
else:
    print("Invalid Account")
