#If the bill was $150.00, split between 5 people, with 12% tip. 
total_bill= float(input("Enter total bill amount:"))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
bill_ph_with_tip= (total_bill/5)*1.12
#Format the result to 2 decimal places = 33.60
rounded_bill_with_tip= round(bill_ph_with_tip, 2)
print(f"The bill with tip for each person is: {rounded_bill_with_tip}")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
