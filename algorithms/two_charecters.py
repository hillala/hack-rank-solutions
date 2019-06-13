#!/bin/python

import sys


s_len = int(raw_input().strip())
s = raw_input().strip()
letters=[s[i] for i in range(len(s)-1) if s[i]==s[i+1]]
for l in letters:
    s=s.replace(l,'')
if len(s)==2:
    t=s
else:
    ss=list(set(s))
    t=[]
    for i in range(len(ss)-2):
        for j in xrange(i+1,len(ss)):
            s1=s
            l1=ss[i]
            l2=ss[j]
            for l in s1:
                if not(l1==l or l==l2):
                    s1=s1.replace(l,'')
            flag=0
            if len(s1)>1:   
                for k in range(len(s1)-1):
                    if s1[k]==s1[k+1]:
                        flag=1
                if flag==0 and len(s1)>len(t):
                    t=s1
print(len(t))        