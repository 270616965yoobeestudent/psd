def factorial(number):
    if number < 0:
        return "Error: Number must be positive"
    if number == 0:
        return 1
    
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

if __name__ == "__main__":
    number = int(input("Enter number: "))
    print(f"Result: {factorial(number)}")
