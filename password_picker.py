import string 
import random
adj=['pretty', 'red', 'smart', 'big', 'small', 'brave', 'handsome']
noun=['apple', 'table', 'bottle', 'purse', 'toaster', 'pillow']
print("Get a random uncrackable password")
ran_adj=random.choice(adj)
ran_noun=random.choice(noun)
num=random.randint(0,100)
char=random.choice(string.punctuation)
password=ran_adj + ran_noun + str(num) + char 
print("Your new password is" + password)