def prime_checker(number):
    rem = 0
    count_rem = 0

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

def fibonacci_checker(number):
    fib_seq_list = [0, 1]
    keep_checking = True
    while keep_checking:
        # print(fib_seq_list)
        if fib_seq_list[-1] <= number:
            if number in fib_seq_list:
                 print(f"{number} is in the Fibonacci sequence.")
                 keep_checking = False
        else:
            print(f"{number} is not in the Fibonacci sequence")
            keep_checking = False

        fib_num = fib_seq_list[-1] + fib_seq_list[-2]
        fib_seq_list.append(fib_num)

n = int(input("Check this number: "))
if n == 0:
    print("Enter an integer greater than zero")
else:
    prime_checker(n)
    fibonacci_checker(n)