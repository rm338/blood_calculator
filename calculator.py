def interface():
	print("My Program")
	while True:
		print("Options")
		print("1 - HDL")
		print("9 - Quit")
		choice = input("Enter your choice: ")
		if choice == '9':
			return
		elif choice == '1':
			HDL_driver()


def HDL_driver():
	# Get input
	HDL_result = get_HDL_input()
	# Check if HDL is normal
	# Output

def get_HDL_input():
	HDL_input = input("Enter the HDL test result: ")
	return int(HDL_input)



interface()
