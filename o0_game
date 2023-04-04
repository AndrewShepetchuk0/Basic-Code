#imports
import random

#variables
num = random.randint(0,25)
num1 = random.randint(0,25)
list = 'u','i','o','p','y','t','r','e','w','q', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'

#Determines which letter is displayed
text = list[num]

#Converts the number to a string to write it to a file
conv = str(num1)

#Creates file and prints the letter and number to the file
fp = open('ex00000000.txt', 'w')
fp.write(text)
fp.write('''
''')
fp.write(conv)
fp.close()

#Prints letter and number
print(text)
print(num1)

#Prints "nice" if the letter is o and the number is zero
if text == 'o' and num1 == 0:
    print('nice')
    fp.write('''
''')
    fp.write('nice')
