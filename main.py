total_bill= float(input("Enter total bill amount:"))
bill_ph_with_tip= (total_bill/5)*1.12
rounded_bill_with_tip= round(bill_ph_with_tip, 2)
print(f"The bill with tip for each person is: {rounded_bill_with_tip}")

