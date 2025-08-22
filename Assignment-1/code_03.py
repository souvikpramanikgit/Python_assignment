# Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361

num=int(input("Enter a 4 digit number: "))

print("Face value: ",end="")

for i in str(num):
    print(i,end=" ")

print("\n")

n=num
rev=0
while n!=0:
    digit=n%10
    rev=(rev*10)+digit
    n=n//10

n=rev

i=3 # As it is a 4 digit number
while n!=0:
    digit=n%10
    print(f"The place value of {digit} is {digit*(10**i)}")
    n=n//10
    i=i-1

print(f"\nThe reverse of {num} is {rev}")