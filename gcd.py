#greatest common divisor 

#first method 
def factors(x):
    l=[]
    for i in range(1,x//2+1) :
        if x % i == 0 :
            l.append(i)
    return l

x = 25
y = 20
lx = factors(x)
ly = factors(y)
commonfactors = []

lz = lx + ly
setlz = set(lz)
for i in setlz :
    if lz.count(i) == 2:
        commonfactors.append(i)

print(f"gcd of {x} and {y} is {max(commonfactors)}")

#Euclid's Algorithm
def gcd(a,b) :
    while b :
        a , b = b , a%b
    return a

x = 25
y = 20
print(f"gcd of {x} and {y} is {gcd(x,y)}")