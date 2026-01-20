def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	PORTION_DOWN_PAYMENT=0.25 # Portion of cost needed for down payment as percent.
	#down_payment=cost_of_dream_home*PORTION_DOWN_PAYMENT
	current_savings=0# Amount saved thus far. Starts at $0.
	R=0.05# Annual return on current_savings such that an additional current_savings*R/12 is put into savings. Assume investments earn rate of return=4%.
	monthly_salary=yearly_salary/12#At the end of each month, savings increase by return on investment plus percentage of monthly_salary.
	#Write a program to calculate how many months it takes to save up enough money.
	months=0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while (current_savings<cost_of_dream_home*PORTION_DOWN_PAYMENT) :
	    current_savings+= portion_saved*monthly_salary + current_savings*R/12
	    months+=1
	print(f"Number of Months: {months}")
	return months