def startup():
    print("--This program will calculate the total surface area of a rectangular prism--")

def length():
    l = float(input("Input length >> "))
    return l

def width():
    w = float(input("Input width >> "))
    return w

def height():
    h = float(input("Input height >> "))
    return h

def side1(l, w):
    tb = float((l * w)*2)
    return tb

def side2(w, h):
    fb = float((w * h)*2)
    return fb

def side3(l, h):
    lr = float((l * h)*2)
    return lr

def calculations(tb, fb, lr):
    sa = (tb+fb+lr)
    return sa

def output(sa):
    print("Total surface area:", sa)

def main(l, w, h, tb, fb, lr, sa):
    startup()
    length()
    width()
    height()
    side1(l, w)
    side2(l, h)
    side3(w, h)
    calculations(tb, fb, lr)
    output(sa)
if __name__ == '__main__':
    main(l, w, h, tb, fb, lr, sa)