def arithmetic_arranger(problems, show_solution=False):
	# check if the number of problems exceeds 5
	if len(problems) > 5:
		return "Error: Too many problems."

	# initialize variables to store lines for the arrangement
	top_line = ""
	bottom_line = ""
	dash_line = ""
	solution_line = ""

	# iterate through each problem in the list
	for problem in problems:
		# Split the problem into its components: operand1, operator, operand2
		elements = problem.split()
		num1 = elements[0]
		operator = elements[1]
		num2 = elements[2]

		# check if the operator is valid (+ or -)
		if operator not in ["+", "-"]:
			return "Error: Operator must be '+' or '-'."
	
		# check if operands contain only digits
		if not (num1.isdigit() and num2.isdigit()):
			return "Error: Numbers must only contain digits."
	
		# check if the length of operands is not more than 4 digits
		if len(num1) > 4 or len(num2) > 4:
			return "Error: Numbers cannot be more than four digits."
	
		# calculate the width required for each column
		width = max(len(num1), len(num2)) + 2
	
		# build the top line with right-aligned operand1
		top_line += num1.rjust(width) + "    "
	
		# build the bottom line with operator and right-aligned operand2
		bottom_line += operator + num2.rjust(width - 1) + "    "
	
		# build the dashed line
		dash_line += "-" * width + "    "
	
		# if show_solution is True, calculate the solution and build the solution line
		if show_solution:
			if operator == "+":
				solution = str(int(num1) + int(num2))
			else:
				solution = str(int(num1) - int(num2))
			solution_line += solution.rjust(width) + "    "

	# combine the lines into the final arranged problems
	arranged_problems = top_line.rstrip() + "\n" + bottom_line.rstrip(
	) + "\n" + dash_line.rstrip()
	
	# if show_solution is True, add the solution line to the arranged problems
	if show_solution:
		arranged_problems += "\n" + solution_line.rstrip()

	return arranged_problems