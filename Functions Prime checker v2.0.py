def prime_checker_100(min, max):
    total_prime = 0
    for num in range(min, max):
        count_zeros = 0
        # print(f"\nThe current number being tested is {num}.")
        for divisor in range(min, num +1):
            # print(f"The current divisor is {divisor}")
            rem = num % divisor
            # print(f"The remainder is {rem}")
            if rem == 0:
                count_zeros += 1
                # print(f"The count of zeros is {count_zeros}")

        if count_zeros == 2:
            # print(count_zeros)
            total_prime += 1
            print(num)
    print(f"The are {total_prime} prime numbers between {min} and {max}")

min = int(input("Enter the range you want to check\n"))
max = int(input(""))

print(f"The prime numbers between {min} and {max} are: ")
prime_checker_100(min = min, max = max)