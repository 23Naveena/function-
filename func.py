s=input("Enter a string: ")
def most_frequent(str):
    a=dict()
    for i in str:
        if i not in a:
            a[i]=1
        else:
            a[i]=a[i]+1
    return a
print(most_frequent(s))
