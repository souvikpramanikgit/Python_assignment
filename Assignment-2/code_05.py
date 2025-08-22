# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

noc=int(input("Enter the number of calls: "))

bill=0

if noc<=100:
    bill=200