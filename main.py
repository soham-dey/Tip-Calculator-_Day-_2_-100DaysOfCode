total_bill= float(input("Enter total bill amount: "))
tip_percent=float(input("Enter tip percentage: "))
people=int(input("How many people tosplit the bill into: "))
bill_ph_with_tip= (total_bill/people)*(1+round(tip_percent/100, 2))
rounded_bill_with_tip= round(bill_ph_with_tip, 2)
print(f"The bill with tip for each person is: {rounded_bill_with_tip}")

