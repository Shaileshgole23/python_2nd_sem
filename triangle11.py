rows=20
for i in range(1,rows+1):
    print('*'*i + ' '*(rows-i)+ ' '*(rows-i)+'*'*i)


row=10
val=1
for i in range(1,row+1):
    for j in range(i):
        print(val%10,end=' ')
        val+=1
        if val>9:
            val=0
    print()