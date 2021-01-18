# Python3 implementation of the above approach

# Function to precompute all the primes
# upto 1000000 and store it in a set
# using Sieve of Eratosthenes
def getPrimesFromSeive(primes):
    prime = [True] * (1000001)
    prime[0], prime[1] = False, False
    i = 2
    while (i * i <= 1000000):
        if (prime[i] == True):
            for j in range(i * i, 1000001, i):
                prime[j] = False
        i += 1

    # Here str() is used for
    # converting int to string
    for i in range(2, 1000001):
        if (prime[i] == True):
            primes.append(str(i))

        # A function to find the minimum


# number of segments the given string
# can be divided such that every
# segment is a prime
def splitIntoPrimes(number):
    n = len(number)

    # Declare a splitdp[] array
    # and initialize to 0
    splitDP = [0] * (n + 1)

    # Call sieve function to store
    # primes in primes array
    primes = []
    getPrimesFromSeive(primes)

    # Build the DP table in a bottom-up manner
    for i in range(1, n + 1):

        # If the prefix is prime then the prefix
        # will be found in the prime set
        if (i <= 6 and number[:i] in primes):
            splitDP[i] = 1

        # If the Given Prefix can be split into Primes
        # then for the remaining string from i to j
        # Check if Prime. If yes calculate
        # the minimum split till j
        if (splitDP[i] != 0):
            j = 1
            while j <= 6 and i + j <= n:

                # To check if the substring from i to j
                # is a prime number or not
                if number[i : i + j] in primes:

                    # If it is a prime, then
                    # update the dp array
                    if splitDP[i + j] == 0:
                        splitDP[i + j] = 1 + splitDP[i]
                    else:
                        splitDP[i + j] = min(splitDP[i + j],
                                             1 + splitDP[i])

                j += 1

    # Return the minimum number of
    # splits for the entire string
    #return splitDP[n]
    return ((splitDP[n]))


# Driver code
# print(splitIntoPrimes("11373"))
# print(splitIntoPrimes("3175"))

# This code is contributed by chitranayal


sieve = []
MOD = 1000000007
def buildSieve():
    for i in range(1000000):
        sieve.append(True)

    sieve[0] = False
    sieve[1] = False

    p = 2
    while p * p <= 1000000:
        if sieve[p]:
            for i in range(p * p, 1000000, p):
                sieve[i] = False
        p += 1

def isPrime(number):
    return sieve[int(number)]

def rec(number, i, dp):
    if dp[i] != -1: return dp[i]

    cnt = 0
    for j in range(1, 7):
        if i - j >= 0 and number[i - j] != '0' and isPrime(number[i - j : i]):
            cnt += rec(number, i - j, dp)
            cnt %= MOD

    dp[i] = cnt
    return cnt

def countPrimeStrings(number):
    n = len(number)
    dp = [-1] * (n + 1)
    dp[0] = 1
    return rec(number, n, dp)


buildSieve()
print(countPrimeStrings('43'))












































