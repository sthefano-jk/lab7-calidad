def f(t, a, b=0):
    if t == "c":
        r = 3.14 * a * a
    elif t == "r":
        r = a * b
    elif t == "t":
        r = a * b / 2
    else:
        r = 0
    print("El area es", r)
    return r


f("c", 5)
f("r", 4, 6)
f("t", 3, 8)