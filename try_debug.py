def odd_even(num):
    if num%2 == 0:
        print("Even")
    else :
        print("odd")

# odd_even(3)


def find_prime(num):
    for i in range (2,num):

        if num%i == 0:
            print("NOT PRIME")
            odd_even(num)
            break
    else: 
        print("IS PRIME")
        odd_even(num)   

find_prime(15)