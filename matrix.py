#matrix operation
'''

'''
class array:
    def __init__(self,lst,r=0,c=0):
        self.lst=lst
        self.r=r
        self.c=c
        M=[]
        tmp=[]
        for i in self.lst:
            tmp.append(i)
            if len(tmp)==c:
                M.append(tmp)
                tmp=[]
        self.lst=M
    def __add__(self,other):
        if (self.r,self.c) == (other.r, other.c):
            M= eval(str([[0]*self.c]*self.r))
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j] = self.lst[i][j]
            return array(M)
        else:
            print('No compatible for addition')
    def __sub__(self,other):
        pass
    def __mul__(self,other):
        if (self.r, self.c)== (other.r , other.c):
            M= eval(str([[0]* self.c]*self.r))
            for i in range(self.r):
                for j in range(self.c):
                    M[i][j]= self.lst[i][j]*other.lst[i][j]
            return array(M)
        else:
            print('No campatible for Multiplication')
    def dot(self,other):
        if self.c == other.r:
            M = eval(str([[0]*other.c]*self.r))
            for i in range(self.r):
                for j in range(other.c):
                    for k in range(self.c):
                       M[i][j] += self.lst[i][k]*other.lst[k][j]
            return array(M)
        else:
            print('dimension not valid for Multiplication')
    def transpose(self, other):
        M = eval(str([[0]*self.r]*self.c))
        for i in range(self.r):
            for j in range(self.r):
                M[i][j]=self.lst[j][i]
        return array(M)
        
    def disp_mat(self):
        for i in self.lst:
            print(*i)
            
    
        

        # self.lst
        # self.other
lst1= list(map(eval,input("Enter the number of matrix 1").split()))
r1,c1 = list(map(eval,input("R x C").split()))
arr1 = array(lst1,r1,c1)

lst2= list(map(eval,input().split()))
r2 , c2 = list(map(eval,input().split()))
arr2 = array(lst2,r2,c2)

print('\mMatrix 1')
arr1.disp_mat()
print('\mMatrix 2')
arr2.disp_mat()
out=arr1+arr2

