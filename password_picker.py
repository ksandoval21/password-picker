import string 
import random
import json
with open("passwords.json") as file:
    reader = json.load(file)
    passwords = list(reader)
adj=['pretty', 'red', 'smart', 'big', 'small', 'brave', 'handsome']
noun=['apple', 'table', 'bottle', 'purse', 'toaster', 'pillow']
print("Get a random uncrackable password")
ran_adj=random.choice(adj)
ran_noun=random.choice(noun)
num=random.randint(0,100)
char=random.choice(string.punctuation)
password=ran_adj + ran_noun + str(num) + char 
print("Your new password is" + password)
response=input('Would you like to save this password?')
if response== "yes".lower():
    user=input("Enter a username: ")
    pin=input("Enter a pin: ")
    data={"User": user, "Pin": pin, "Password": password}
    with open("passwords.json", "w", newline='') as file:
        json.dump(data, file)
elif response=="no".lower():
    print("Goodbye!")