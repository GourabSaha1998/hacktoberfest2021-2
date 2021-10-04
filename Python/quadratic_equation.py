def quadratic():
    """ ""  This functions determines roots of a quadratic equation
             i.e of the form ax^2+bx+c = 0  "" """
    a = int(input("Enter the co_efficient of x^2 : "))
    b = int(input("Enter the co_efficient of x : "))
    c = int(input("Enter the constant term : "))
    d = ((b ** 2) - (4 * a * c))
    if d > 0:  # For real and distinct roots
        D = d ** (1 / 2)
        x_1 = (-b + D) / 2
        x_2 = (-b - D) / 2
        print("The required roots are \nx1 =", x_1, "\nx2 =", x_2)
    elif d == 0:  # For equal roots
        x = (-b) / 2
        print("The required roots are equal & the double root is \nx1 = x2 =", x)
    else:  # For complex roots
        D = (-d) ** (1 / 2)
        x = (-b) / 2
        print("The required roots are imaginary")
        print("The roots are \nx1 =", x, "+", D, "i", "\nx2 =", x, "-", D, "i")


print(quadratic.__doc__)
quadratic()
