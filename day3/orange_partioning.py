no_of_oranges=int(input("Enter the no of oranges:"))
input_diameters=list(map(int,input().split()))
medium_size=input_diameters[-1]
k=0
for i in range(len(input_diameters)):
    if input_diameters[i] < medium_size:
        input_diameters[i], input_diameters[k]=input_diameters[k], input_diameters[i]
        k+=1
input_diameters[k],input_diameters[-1]=input_diameters[-1], input_diameters[k]
print(input_diameters)