# Write a python program using function to convert Celsius to Fahrenheit.


# Function to convert Celsius to Fahrenheit
def c_to_f(c):
    return c * 1.8 + 32

# Take input from user
c = float(input("Enter temperature in Celsius: "))

# Convert and display result
f = c_to_f(c)
print(f"{c}°C is equal to {round(f,2)}°F")
