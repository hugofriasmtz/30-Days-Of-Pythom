# Declare your age as an integer variable
age = 22

# Declare your height as a float variable
height = 1.78

# Declare a variable that stores a complex number
complex_num = 1 + 0j

# Area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print(f"The area of the triangle is {area}")

# Perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}")

# Rectangle area and perimeter
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

# Circle area and circumference
pi = 3.14
radius = float(input("Enter radius: "))
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area: {area}")
print(f"Circumference: {circumference}")

# Slope, x-intercept, y-intercept
m = 5
b = -5
x_intercept = 5   
y_intercept = -5  

print(f"Slope: {m}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Slope and distance between points (6,6) and (2,6)
x1, y1 = 6, 6
x2, y2 = 2, 6
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print(f"Slope: {slope}")
print(f"Distance: {distance}")

# Compare slopes
print(f"Slopes are equal: {m == slope}")

# Solve quadratic y = x² + 6x + 9
# factorized: (x+3)^2 = 0 => x = -3
x = -3
y = x**2 + 6*x + 9
print("y =", y, "when x =", x)

# Length comparison of ‘Hola’ and ‘Lalo’
len_hola = len('Hola')
len_lalo = len('Lalo')
print(f"Is length of Hola equal to length of Lalo? {len_hola == len_lalo}")

#  Check if ‘on’ in both ‘Hola’ and ‘Lalo’
print(f"Is 'on' in both 'Hola' and 'Lalo'? {'on' in 'Hola' and 'on' in 'Lalo'}")

# Check if ‘jargon’ in sentence
sentence = "I hope this course is not full of jargon."
print(f"Is 'jargon' in sentence? {'jargon' in sentence}")

# Check if ‘on’ is not in both
print(f"Is 'on' not in both 'dragon' and 'python'? {'on' not in 'dragon' and 'on' not in 'python'}")

# Convert length of text to float and string
length = len('Frias')
length_float = float(length)
length_str = str(length_float)
print(length_str)

# Check if a number is even
num = 4
is_even = num % 2 == 0
print(f"Is number even? {is_even}")

# Floor division check
print(f"Is 7 // 3 equal to int(2.7)? {7 // 3 == int(2.7)}")

# Type comparison
print(type('10') == type(10))

# Convert ‘9.8’ to int
print(int(float('9.8')) == 10)

# Calculate weekly pay
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
pay = hours * rate
print(f"Your weekly earning is {pay}")

# Calculate seconds lived
years = int(input("Enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print(f"You have lived for {seconds} seconds.")

# Display table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)