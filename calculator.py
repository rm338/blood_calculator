def interface():
	print("My Program")
	while True:
		print("Options")
		print("1 - HDL")
		print("2 - LDL")
		print("9 - Quit")
		choice = input("Enter your choice: ")
		if choice == '9':
			return
		elif choice == '1':
			HDL_driver()
		elif choice == '2':
			LDL_driver()


def HDL_driver():
	# Get input
	HDL_result = get_HDL_input()
	# Check if HDL is normal
	HDL_analysis = analyze_HDL_result(HDL_result)
	# Output
	output_HDL_analysis(HDL_result, HDL_analysis)


def get_HDL_input():
	HDL_input = input("Enter the HDL test result: ")
	return int(HDL_input)

def analyze_HDL_result(HDL_test_value):
	if HDL_test_value >= 60:
		return "Normal"
	elif 40 <= HDL_test_value < 60:
		return "Borderline Low"
	else:
		return "Low"

def output_HDL_analysis(test_result, analysis):
	print("This HDL result is {}".format(test_result))
	print("That is {}".format(analysis))
		
def LDL_driver():
	# Get input
	LDL_result = get_LDL_input()
	# Check if HDL is normal
	LDL_analysis = analyze_LDL_result(LDL_result)
	# Output
	output_LDL_analysis(LDL_result, LDL_analysis)


def get_LDL_input():
	LDL_input = input("Enter the LDL test result: ")
	return int(LDL_input)

def analyze_LDL_result(LDL_test_value):
	if LDL_test_value < 130:
		return "Normal"
	elif 130 <= LDL_test_value < 160:
		return "Borderline High"
	elif 160 <= LDL_test_value < 190:
		return "High"
	else:
		return "Very High"

def output_LDL_analysis(test_result, analysis):
	print("This LDL result is {}".format(test_result))
	print("That is {}".format(analysis))



interface()
