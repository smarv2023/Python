# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Enter number: "))  # Check this number
prime_checker(number=n)

y = int(input("Enter number")) #test to be erased