def print_patter(number):
    for i in range(number):
        for j in range(i):
            print("*",end=" ")
        print(" ")

print_patter(5)
