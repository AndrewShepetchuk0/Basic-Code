import random
import string
#Determines how long the password will be

pl = int(input("How long do you want your password to be?"))
pw = []

#Creates a list of characters for the password generator to choose from
char = list("qwertyuiopasdfghjklzxcvbnm" + "QWERTYUIOPASDFGHJKLZXCVBNM" + "1234567890" + "`-=[]\;',./" + "~!@#$%&*()_+{}|:<>?")

#Generates the password
for i in range(pl):
    random.shuffle(char)
    pw.append(random.choice(char))
random.shuffle(pw)

#Prints the password
print("".join(pw))
