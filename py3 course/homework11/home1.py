def print_table(a,b):
    for i in range(len(a)):
        lst = ""
        for j in range(len(b)):
            lst += a[i]+b[j]+" "
        print(lst)
            
print_table(['1', '2', '3'], ['a', 'b', 'c'])