import re
f = open('encoded_new_fr.txt','r')
s = open('encoded_new_fr2.txt','a+')
for i in f:
    l = i.split()
    if('[' in l):
        for i in range(len(l)):
            if(l[i]=='['):
                tl = l[:i+1]
                tl2 = l[i+1:]
                for j in range(len(tl2)):
                    tl2[j] = tl2[j]+','
                l = tl+tl2
                k = ' '.join(l)
                s.write(k)
                s.write('\n')
    elif(']' in l):
        for i in range(len(l)):
            if(l[i]==']'):
                tl = l[:i]
                tl2 = l[i:]
                for j in range(len(tl)):
                    tl[j] = tl[j]+','
                l = tl+tl2
                k = ' '.join(l)
                s.write(k)
                s.write('\n')
    else:
        for i in range(len(l)):
            l[i] = l[i]+','
        k = ' '.join(l)
        s.write(k)
        s.write('\n')




