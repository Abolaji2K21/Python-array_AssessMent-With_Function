
employee_name=input("Enter Employee's Full Name: ")

hours_worked=int(input("Enter Number Of Hours Worked In A Week:"))

hourly_pay_rate=float(input("EnterHourly Pay Rate:"))

month=input("Enter Month : ")

federal_tax_rate=int(input("Enter Federal Tax WithHolding Rate: "))

state_tax_rate=int(input("Enter State Tax WithHolding Rate: "))

employers_name=input("Enter Employers Name :")

gross_pay= hours_worked * hourly_pay_rate;

federal_withholding = (gross_pay * (federal_tax_rate / 100))

state_withholding = (gross_pay * (state_tax_rate / 100))
	
total_deduction = federal_withholding + state_withholding

net_pay = gross_pay - total_deduction


print("=================================================")
print(employers_name," Payroll Statement For The Month Of", month)
print("=================================================")
print("Employee Name: ", employee_name)
print("Hours Worked:", hours_worked)
print("Hourly Pay Rate: $", hourly_pay_rate)
print("Gross Pay: $", gross_pay)

print("Deductions:")
print("Federal Tax Withholding: $", federal_withholding)
print("State Tax Withholding: $", state_withholding)
print("Total Deduction: $", total_deduction)
print("Net Pay: $", net_pay)
print("=================================================")


	
	