#Variable for the for loop
i = 0.0

#For loop
for i in range(100):
	#This could be better... probably
	i = i+1
	#Prints the number and if it's divisible by 3, prints Fizz
	if i % 3 == 0:
		print(i, "Fizz")
	#Prints the number and if it's divisible by 5, prints Buzz
	if i % 5 == 0:
		print(i, "Buzz")
	#Prints the number and if it's divisible by 7, prints Fuzz
	if i % 7 == 0:
		print(i, "Fuzz")
	#Just prints the number by default
	else:
		print(i)
