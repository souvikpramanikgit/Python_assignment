# Write a Python Program to Convert Celsius To Fahrenheit vice versa.
# Fahrenheit to Celsius: °C = (°F - 32) × 5/9
# Celsius to Fahrenheit: °F = (°C × 9/5) + 32

f=int(input("Enter the temperature in Fahrenheit: "))
c=(f-23)*(5/9)
print(f"The temperature in celcius: {c}")

c=int(input("Enter the temperature in celsius: "))
f=(c*(9/5))+32
print(f"The temperature in fahrenheit: {c}")