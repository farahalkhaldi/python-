def get_float(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("invalid numbers")

num1 = get_float("Enter the first number: ")
num2 = get_float("Enter the second number: ")


choice = input("Choose the operation (+, -, /, *): ")

if choice == '+' :
	answer = num1 + num2  
	answer_1 = "The answer is {}".format(answer)
	print(answer_1)
elif choice == '-':
	answer = num1 - num2
	answer_2 = "The answer is {}".format(answer)
	print(answer_2)
elif choice == '/':
	answer = num1 / num2
	answer_3 = "The answer is {}".format(answer)
	print(answer_3)
elif choice == '*':
	answer = num1 + num2
	answer_4 = "The answer is {}".format(answer)
	print(answer_4)
else :
	print("wrong choice, operation is not valid.")