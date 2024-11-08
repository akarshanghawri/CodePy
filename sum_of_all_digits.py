#sum of all digits until it becomes a sigle digit

#first method 
x = 1234
l = []

for i in str(x) :
    l.append(int(i))

def sumDigits(l) :
    while len(l) > 1 :
        sum = 0
        for i in l :
            sum += i 

        l.clear()

        for i in str(sum) :
            l.append(int(i))
    print(sum)

sumDigits(l)

#trying by recursion
def sumdigits(x) :
    l=[]
    for i in str(x) :
        l.append(int(i))
    
    if len(l) == 1 :
        print(l[0])
    else :
        sum = 0
        for i in l :
            sum += i
        sumdigits(sum)

sumdigits(12344)

#third method 
def sumdigits(x) :
    sum = 0
    while x > 0 :
        y = x % 10
        sum += y
        x = x // 10
    
    if sum < 10 :
        print(sum)
    else :
        sumdigits(sum)
sumdigits(1234567)
