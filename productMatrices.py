l=[[1,0,0],  
   [0,1,0],
   [0,0,1]]

l2=[[4,5,2],
    [3,1,2],
    [4,8,1]]

print("matrice 1 :") 
  
for i in range(3) :
    for j in range(3) :
        print(l[i][j],end=" ")
    print()
    
print("matrice 2 :")  
for i in range(3) :
    for j in range(3) :
        print(l2[i][j],end=" ")
    print()
     
t = []
for i in range(len(l2[0])):
    row = []
    for j in range(len(l2)):
        row.append(l2[j][i])
    t.append(row)

def rc(r,c) :
    x=0
    for i in range (3) :
        x = x + r[i] * c[i]
    return x

print("Product of both the matrices is :")
for i in range (3) :
    for j in range (3) :
        print(rc(l[i],t[j]),end = " ")
    print()
