username = input("Enter Username: ")
age = int(input ("Enter Age: "))
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("=====================================")
print("Username:", username)
print("age:", age)
print("Category:", category)

if age>40 and category == 'fun':
    print("you are old what is fun for you?")