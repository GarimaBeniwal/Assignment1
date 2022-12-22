a=float(input("Enter your gross income:"))
b=int(input("Enter the no of dependents:"))
std_deduction=10000
tax_rate=20
additional_deduction=3000
taxable_income=a-std_deduction-(b*additional_deduction)
tax=(taxable_income*tax_rate)/100
print("taxable income is",str(taxable_income))
print("tax is"+str(tax))


