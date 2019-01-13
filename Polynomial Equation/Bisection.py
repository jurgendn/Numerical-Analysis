import sympy as sy

#Define x as a symbolic variable
x = sy.Symbol("x")


# Define function
func = sy.Pow(x, 3)-2*x*x+1+sy.sin(x-1)
f = sy.lambdify(x, func)


#Input 
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
epsilon = float(input("Nhap sai so: "))


# Check input
def verify(func, a, b):
    check = True
    if f(a)*f(b) > 0:
        check = False
    else:
        check = True
    return check


# Iteration step
def iteration(func, a, b, err):
    root = (a+b)/2
    count = 1
    while b-a >= err:
        if f(root) == 0:
            return root
        elif f(a)*f(root) < 0:
            b = root
        elif f(a)*f(root) > 0:
            a = root
        root = (a + b) / 2
        count += 1
    return root, count  # Return root and number of iteration steps


# Main function
if verify(func, a, b) == False:
    print("Failure")
else:
    print("Root: ")
    print(iteration(func, a, b, epsilon))
