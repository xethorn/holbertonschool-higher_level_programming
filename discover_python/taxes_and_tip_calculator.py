print "Welcome to the taxes and tip calculator!" 
price=input("What is the price before tax? ") 
tax=input("What are the taxes?(in %) ")
tip=input("What do you want to tip? (in %) ")


tax=tax/100.0

tip=tip/100.0 

price=price+price*tax 

total = price+ price*tip

print ("The price that you need to pay is: $%.6f" %total)
