def insertion_sort(string):
    for i in range(1,len(string)):
        key=string[i]
        j=i-1
        while j>=0 and string[j]>key:
            string[j+1]=string[j]
            j-=1
        string[j+1]=key
string=[s for s in input("Enter the string to perform insertion sort:").lower()]
insertion_sort(string)
print('The sorted array is',string)