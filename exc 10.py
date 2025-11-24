def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

def main():
    num = int(input("Enter a number: "))
    result = check_even_odd(num)
    print(result)

if __name__ == "__main__":
    main()