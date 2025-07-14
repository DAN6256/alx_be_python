number = int(input("Enter the size of the pattern:"))
i=0
while i <number:
    for _ in range(1,number + 1):
        print("*", end="")
    print("\n")
    i=i+1