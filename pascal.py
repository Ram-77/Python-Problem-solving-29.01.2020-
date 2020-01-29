rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    coff = 1
    for j in range(1, rows-i):
        print("  ", end="")
    
    for k in range(0, i+1):
        print("  ", coff, end="")
        coff = int(coff * (i - k) / (k + 1))
    print()



sample output:
Enter the number of rows : 4
         1
       1   1
     1   2   1
   1   3   3   1
