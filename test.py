# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print(f"Fibonacci sequence upto {nterms}:")
   print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        nth = n1 + n2
        count += 1
        if count == nterms:
           print (f"Posicion number {count} is {nth}")
        # update values
        n1 = n2
        n2 = nth
