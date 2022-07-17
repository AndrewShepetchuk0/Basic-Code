import random
import string
pl = int(input("How long do you want your password to be?"))
pw = []
char = list("qwertyuiopasdfghjklzxcvbnm" + "QWERTYUIOPASDFGHJKLZXCVBNM" + "1234567890" + "`-=[]\;',./" + "~!@#$%&*()_+{}|:<>?")
for i in range(pl):
    random.shuffle(char)
    pw.append(random.choice(char))
random.shuffle(pw)
print("".join(pw))
