def sum_of_even(num):
    sum=0
    for i in range(len(num)):
        if i%2==0 and num[i]%2==0:
            sum+=num[i]
    return sum
num=[int(i) for i in input("Enter the numbers:")]
print("Sum of odd placed even numbers is", sum_of_even(num))

