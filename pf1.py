import math
import time
from datetime import datetime
#from multiprocessing import Pool
#from functools import partial
import json


def pcalc(rge):
    global x
    global xc
    global c

    #print(x)
    #print (rge)

    for y in rge :
        #print(y)
        if (x % y == 0) :
            #print("Failed with " + str(y) + " in " + str(c) + " calcs")
            nfile = open('lastNumber.txt', 'w', encoding='utf-8')
            write = str(x) + "," + str(c)
            nfile.write(write)
            nfile.close()
            break

        if len(str(x)) > 20 :
            if(c % 100000000000 == 0 and c <999999999999):
                print(str(int(c*0.000000001)) + "B calculations processed ")

            elif(c % 10000000000 == 0 and c < 99999999999):
                print(strrge(int(c*0.000000001)) + "B calculations processed")

            elif(c % 1000000000 == 0 and c < 9999999999):
                print(str(int(c*0.000000001)) + "B calculations processed")

            elif(c % 100000000 == 0 and c < 999999999):
                print(str(int(c*0.000001)) + "M calculations processed ")

            #if(c % 10000000 == 0 and c < 99999999):
                #print(str(int(c*0.000001)) + "M calculations processed")
                #print(x)
                #print(y)
        #print("Prime = " + str(x) + " with " + str(c) + " calculations")
        c=c+1

    else:
        nfile = open('lastNumber.txt', 'w', encoding='utf-8')
        write = str(x) + "," + str(c)
        nfile.write(write)
        nfile.close()

        f = open('primes.txt', 'a')

        if len(str(x)) <= 5 :
            if c % 10 == 0 :
        #print(str(c)+" calc "+str(y))
                print("Prime = " + str(x) + " with " + str(c) + " calculations")
        elif 5 < len(str(x)) <= 7  :
            if c % 50 == 0 :
                #print(str(c)+" calc "+str(y))
                print("Prime = " + str(x) + " with " + str(c) + " calculations")
        elif 7 < len(str(x)) <= 14  :
            if c % 250 == 0 :
                #print(str(c)+" calc "+str(y))
                print("Prime = " + str(x) + " with " + str(c) + " calculations")
        elif 14 < len(str(x)) <= 15 :
            if c % 100 == 0 :
                #print(str(c)+" calc "+str(y))
                print("Prime = " + str(x) + " with " + str(c) + " calculations")
        elif 15 < len(str(x)) <= 20 :
            if c % 10 == 0 :
                #print(str(c)+" calc "+st)
                print("Prime = " + str(x) + " with " + str(c) + " calculations")
        elif len(str(x)) > 20 :
            print("Prime = " + str(x) + " with " + str(c) + " calculations")

        if xc%10 == 0:

            lbr = "\n"
            f.write(lbr)


        prime = str(x) + ","
        f.write(prime)
        f.close()
        xc = xc+1

#        return x



try:
    file = open('lastNumber.txt', 'r')
    info = (file.readline())
    splift = info.split(",",1)[0]
    clinfo = info.split(",",1)[1]
    print("previous number checked " + str(splift))
    print("Calculations for last number: " + str(clinfo))

except IOError :
    print()

ui1 = int(input("How many numbers would you like to process?: "))
#start = 3
start = int(splift) + 2
stop = start + int(ui1)

plist = []
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
tstart = time.time()
xc = 0

print(current_time)

x = start
sqr = int(math.sqrt(x))
rge = range(3,sqr,2)


for x in range(start, stop +1):

    s = int(str(x)[-1])
#print(s)
    if s in (1,3,7,9) :
        #print(s)
        if len(str(x)) > 20 :
            print("Testing " + str(x))

        sqr = int(math.sqrt(x))

        c = 1

        pcalc(rge)


tend = time.time()




#print(plist)
print("Completed in " + str(round((tend-tstart),3)/60) + " minutes")
file = open('lastNumber.txt', 'r')
info = (file.readline())
splift = info.split(",",1)[0]
clinfo = info.split(",",1)[1]
print("last number checked " + str(splift))
