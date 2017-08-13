print "welcome..! "
num=int(raw_input("Enter number to check its factorial "))

factorial=1

if num<0:
    print"Enter a positive number"
elif num==0:
    print "factorial is 1"
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print "the factorial of",num,"is",factorial


