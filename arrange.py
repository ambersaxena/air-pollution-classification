rd=open("C2015.csv","r")
wd=open("aqi3.csv","w")
j=0
for i in rd:
    #print i
    l=i.split(",")
    print l
    break
    if l[0]=='NA' or l[1]=='NA' or l[2]=='NA' or l[2]=='NA\n':
        continue
    if int(l[0])>=350 or int(l[1])>=200 or int(l[2])>=100:
        y=1
    elif (int(l[0])>=100 and int(l[1])>=100) or (int(l[0])>=100 and int(l[2])>=50) or (int(l[1])>=100 and int(l[2])>=50):
        y=1
    else:
        y=0
    j=j+1
    print j
    cl=str(y)
    l[2]=l[2][0:-1]
    a=l[0]+","+l[1]+","+l[2]+","+cl
    wd.write(a)
    wd.write("\n")
    j=j+1
wd.close()