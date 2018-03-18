from bs4 import BeautifulSoup
import urllib2
import pandas as pd
import time
from subprocess import call
f=urllib2.urlopen('https://www.codechef.com/contests')
soup=BeautifulSoup(f,"html.parser")
r=soup.find_all("tbody")
row=r[0].find_all("tr")
A=[]
B=[]
C=[]
D=[]
for l in row:
    q=l.find_all("td")
    A.append(q[0].find(text=True))
    B.append(q[1].find(text=True))
    C.append(q[2].find(text=True))
    D.append(q[3].find(text=True))

print "\n"
row1=r[1].find_all("tr")
for l in row1:
    q=l.find_all("td")
    A.append(q[0].find(text=True))
    B.append(q[1].find(text=True))
    C.append(q[2].find(text=True))
    D.append(q[3].find(text=True))
for t in range(0,len(A)):
    call(["notify-send",A[t],"\n",B[t],"\n",'Start Date:'+C[t],"\n",'End Date:'+D[t]])
    
