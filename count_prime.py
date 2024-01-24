import sys

# Write a function that returns the number of prime numbers that exist up to and including a given number
# BY convention 0 and  1 is not prime
# Example: count_primes(100) --> 25

def is_prime(n):
    if (n < 2):
        return False
    elif (n == 2):
        return True

    ''' The reason for using the square root is based on the observation that if a number n is not a prime,
    it can be factored into two factors, a and b, such that n = a * b. If both a and b are greater than the
    square root of n, their product would be greater than n. Therefore, at least one of the factors must be
    less than or equal to the square root of n. Checking only up to the square root reduces the number of
    divisions needed to determine primality.
    '''
    limit = int(n**0.5)+1
    for j in range(3, limit, 2):
        if n % j == 0:
            return False
    
    return True

def count_primes(num):
    count = 0
    if (num >=2):
        count = 1
    primes = [2]
    for n in range(3, num+1, 2): # range(start, end, step) Just consider odd number including given num
#        cn = 0
#        for j in range(3, n+1, 2):
#            if (n % j == 0):
#                cn = cn + 1
#        
#        if (cn == 1):
#            count = count + 1
        if is_prime(n):
            primes.append(n)
            count += 1
    
    print('count_primes(): Prime numbers: {}'.format(primes))
    return count

def count_primes1( num ):
    if (num < 2):
        return 0

    primes = [2] # store prime numbers

    x = 3
    while x <= num:
        # chk if x is prime
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else: # NOTE: This 'else' will execute only if 'break' in for loop is
              # ***NOT*** executed
            primes.append(x)
            x += 2

    print('count_primes1(): Prime numbers: {}'.format(primes))
    return len(primes)

def main():
    if len(sys.argv) != 2:
        print('Usage: {} Number'.format(sys.argv[0]))
        sys.exit(1)

    num = int(sys.argv[1])
    print('count_primes():Number of primes: {}'.format(count_primes(num)))
    print('count_primes1():Number of primes: {}'.format(count_primes1(num)))

if __name__ == '__main__':
    main()
