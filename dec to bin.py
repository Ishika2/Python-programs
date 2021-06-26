#decimal to binary
'''
num = int(input("Enter number: "))

new_bin = []
while num>0:
    dig = num%2
    new_bin.append(dig)    
    num = num//2
print("Binary: ", end='')
for i in range(len(new_bin)-1,-1,-1):
    print(new_bin[i], end='')
'''

#decimal to binary

num = int(input("Enter number: "))
print("Binary: ", end = '')
s = ""
while num>0:
    dig = num&1
    s = str(dig) + s
    num = num>>1
print(s)


##  1000 <-- num = 8
##& 0001
##  0000 <-- dig = 0
##  
##  0100 <-- num = 4
##& 0001
##  0000 <-- dig = 0
##
##  0010 <-- num = 2
##& 0001
##  0000 <-- dig = 0
##
##  0001 <-- num = 1
##& 0001
##  0001 <-- dig = 1
##
##BINARY : 1000
##----------------------
##
##  0110 <-- num = 6
##& 0001
##  0000 <-- dig = 0
##
##  0011 <-- num = 3
##& 0001
##  0001 <-- dig = 1
##
##  0001 <-- num = 1
##& 0001
##  0001 <-- dig = 1
##BINARY : 110

#decimal to binary

##num = int(input("Enter number: "))
##new_bin = 0
##cnt = 0
##while num > 0:
##    dig = num%2
##    c = pow(10,cnt)
##    new_bin += dig*c
##    num = num//2
##    cnt += 1
##print("Binary: ", new_bin)
