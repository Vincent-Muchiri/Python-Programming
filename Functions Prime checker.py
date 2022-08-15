def prime_checker(number):
    rem = 0
    count_rem = 0
    if number == 0:
        print("Enter an integer greater than zero")
    else:
        for divisor in range(1, number + 1):
            # print(f"The divisor is {divisor}")
            rem = number % divisor
            # print(f"The remainder is {rem}")
            if rem == 0:
                count_rem += 1
            # print(f"The number of perfect divisors are {count_rem}")
        if count_rem == 2:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not a prime number")

n = int(input("Check this number: "))
prime_checker(number = n)