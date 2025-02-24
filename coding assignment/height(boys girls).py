def check_height(N,boys_height,girls_height):
    boys_height.sort()
    girls_height.sort()
        
    pass

N=int(input("Enter number of test cases:"))
for _ in range(N):
    size=int(input("Enter number of boys and girls:"))
    boys_height=[int(i) for i in input("Enter boys heights:").split()]
    girls_height=[int(i) for i in input("Enter girls heights:").split()]
    result=check_height(N,boys_height,girls_height)
    print(result)
