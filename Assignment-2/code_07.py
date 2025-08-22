# Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit price is Rs 5 
# and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for quantities over 50

b=int(input("Enter the quantity you want to buy: "))

if b<=30 and b>=1:
    print(f"The price of {b} quantities is {b*5}")
elif b>50:
    print(f"The price of {b} quantities is {(b*5)*0.85}")
elif b>30:
    print(f"The price of {b} quantities is {(b*5)*0.9}")
else:
    print("Enter a number greater that zero")
