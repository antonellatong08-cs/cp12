def add(a, b):
    # return sum
    pass

def maxOfTwo(a, b):
    # return bigger number
    pass

def isEven(n):
    # return True/False
    pass

def countVowels(s):
    # return number of vowels
    pass

def reverseString(s):
    # return reversed string
    pass

def isPrime(n):
    # return True/False
    pass

def sumOfFactors(n):
    # return sum of all factors of a number
    pass

def numOfFactor(n):
    # count how many factors n has
    pass

def removeNegatives(lst):
    # return new list without negatives
    pass


def print_menu():
    print("\n=== Function Gym ===")
    print("1. Add two numbers")
    print("2. Max of two numbers")
    print("3. Check even")
    print("4. Count vowels")
    print("5. Reverse string")
    print("6. Prime check")
    print("7. Sum of factors")
    print("8. Number of factors")
    print("9. Remove negatives")
    print("0. Exit")


while True:
    print_menu()
    choice = input("Choose: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(add(a, b))

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(maxOfTwo(a, b))

    elif choice == "3":
        n = int(input("Enter number: "))
        print(isEven(n))

    elif choice == "4":
        s = input("Enter string: ")
        print(countVowels(s))

    elif choice == "5":
        s = input("Enter string: ")
        print(reverseString(s))

    elif choice == "6":
        n = int(input("Enter number: "))
        print(isPrime(n))

    elif choice == "7":
        n = int(input("Enter number: "))
        print(sumOfFactors(n))

    elif choice == "8":
        n = int(input("Enter number: "))
        print(numOfFactor(n))

    elif choice == "9":
        lst = [int(x) for x in input("Enter numbers separated by space: ").split()]
        print(removeNegatives(lst))

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")