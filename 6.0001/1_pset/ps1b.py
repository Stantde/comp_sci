
annual_salary=int(input("Enter your annual salary: "))
portion_saved=float(input("Enter the percent of your salary to save, as a decimal: "))# Amount of salary saved each month, dedicated to making down_payment
total_cost=int(input("Enter the cost of your dream home: ")) # Cost of dream home
semi_annual_raise=float(input("Enter the semi-annual raise, as a decimal: "))
PORTION_DOWN_PAYMENT=0.25 # Portion of cost needed for down payment as percent.
#down_payment=total_cost*PORTION_DOWN_PAYMENT
current_savings=0# Amount saved thus far. Starts at $0.
R=0.04# Annual return on current_savings such that an additional current_savings*R/12 is put into savings. Assume investments earn rate of return=4%.
monthly_salary=annual_salary/12#At the end of each month, savings increase by return on investment plus percentage of monthly_salary.
#Write a program to calculate how many months it takes to save up enough money.
total_months=0
while (current_savings<total_cost*PORTION_DOWN_PAYMENT) :
    current_savings+= portion_saved*monthly_salary + current_savings*R/12
    total_months+=1
    if total_months%6==0:
        #increase salary by raise.
        monthly_salary*=1+semi_annual_raise
    
print(f"Number of Months: {total_months}")