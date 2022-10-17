def startup():
    print("--This program will calculate the total surface area of a rectangular prism--")

def inputs():
    l = float(input("Input length >> "))
    w = float(input("Input width >> "))
    h = float(input("Input height >> "))

def calculations():
    tb = float((l * w)*2)
    lr = float((h * l)*2)
    fb = float((h * w)*2)
    sa = float(tb + lr + fb)
def end_result():
    return calculations()
    print("Total surface area:", sa)

def main():
    startup()
    inputs()
    calculations()
    end_result()

if __name__ == '__main__':
    main()

