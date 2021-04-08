def PrimeNumber(n): #Here I'm defining the function checking if the number is prime
    for i in range(2, n // 2 + 1): #The range consists of 2 (1 is not prime) and odd numbers (even numbers cannot be prime)
        if (n % i == 0): #Function will check if there is a reminder of the division
            return (0)
    return (1)
N = int(input("Choose N:")) #N needs to be chosen in the Python Console
i = 2
items = [] #List named items is created
while (1):
    if (PrimeNumber(i)):
        items.append(i) #Here the elements meeting the requirements are added to the list (items)
        if (len(items) == N):
            break #The calculation will stop when the number of itmes in the list is equal to N
    i = i + 1
print("First " + str(N) + " prime numbers: ", end="")
print(*items)