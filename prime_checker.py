def prime_checker(number):
    is_prime= True
    for i in range(2,n):
        if (n%i) == 0:
            is_prime=False
    if is_prime==False:
        print("this is a composite number")
    else:
        print("this is a prime number")
n= int(input("Enter a number:\n"))
prime_checker(n)