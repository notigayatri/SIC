def check_height(size,boys_height,girls_height):
    boys_height.sort()
    girls_height.sort()
    arr1=[]
    for i in range(size):
        arr1.append(boys_height[i])
        arr1.append(girls_height[i])
    
    arr2=[]
    for i in range(size):
        arr2.append(girls_height[i])
        arr2.append(boys_height[i])
    
    def is_valid(arr):
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                return False
        return True
    
    if is_valid(arr1) or is_valid(arr2):
        return "Yes"
    else:
        return "No"

N=int(input("Enter number of test cases:"))
for _ in range(N):
    size=int(input("Enter number of boys and girls:"))
    boys_height=[int(i) for i in input("Enter boys heights:").split()]
    girls_height=[int(i) for i in input("Enter girls heights:").split()]
    result=check_height(size,boys_height,girls_height)
    print(result)
