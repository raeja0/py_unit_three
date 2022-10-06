# Write your addition function in the space below...
number_1 = input("First Number >> ")
num1 = int(number_1)

number_2 = input("Second Number >> ")
num2 = int(number_2)

total = num1 + num2

def add_two(num1, num2):
    print("The sum of", num1, "and", num2, "is", total)
# Do not change anything below these lines
def main():
    add_two(num1, num2)
    pass

if __name__ == '__main__':
    main()