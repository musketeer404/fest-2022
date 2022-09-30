n = int(input("Enter any no: "))
divs = 0
for _ in range(1,n):
    if n % _ == 0:
        divs += 1
    else:
        divs += 0
if divs == 1:
    print(n, "is prime.")
else:
    print(n, "is not prime.")
