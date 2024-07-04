
import math

# Returns the smallest integer greater than or equal to x.
num1 = 5.0
print(math.ceil(num1))

# Returns the largest integer less than or equal to x
print(math.floor(num1))

# Returns the absolute value of x
x = -5.2
abs_x = math.fabs(x)
print("Returns absolute value",abs_x)


print("math.modf(math.pi) : ", math.modf(math.pi))
print("math.modf(786.11) : ", math.modf(786.11))
print("math.modf(-786.69) : ", math.modf(-786.69))