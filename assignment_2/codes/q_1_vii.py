from sympy import Symbol,sec,csc,integrate,simplify


if __name__ == "__main__":
    x = Symbol('x')
    print(simplify(integrate(sec(x)**2/csc(x)**2,x)))
    