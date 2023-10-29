#Variable for the for loop
i = 0.0

for i in range(100):
	i = i+1
	if i % 3 == 0:
		print(i, "Fizz")
	if i % 5 == 0:
		print(i, "Buzz")
	if i % 7 == 0:
		print(i, "Fuzz")
	else:
		print(i)
