def startup():
    print("--This program will calculate the total surface area of a rectangular prism--")

def inputs():
    global l
    global h
    global w
    l = float(input("Input length >> "))
    w = float(input("Input width >> "))
    h = float(input("Input height >> "))

def calculations(l, w, h):
    global sa
    tb = float((l * w)*2)
    lr = float((h * l)*2)
    fb = float((h * w)*2)
    sa = float(tb + lr + fb)
    return tb, lr, fb, sa
def end_result(sa):
    print("Total surface area:", sa)

def main():
    startup()
    inputs()
    calculations(l, w, h)
    end_result(sa)
if __name__ == '__main__':
    main()