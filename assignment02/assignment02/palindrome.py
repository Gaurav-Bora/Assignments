string = input("Enter name :")
string = string.lower()
if (string == string[::-1]):
    print(f"{string} True")
else:
    print(f"{string} False")
    
 