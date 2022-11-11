import math
from math import log2

with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

best=""
maxi=0
for word in lines: 
    valid=[0]*5
    for i in range(3**5):  #takink every posibility of valid
        nr=0
        entropy=0.0
        for j in range(5):
            valid[j]=i%3
            i=i//3
        for cuv in lines: #and counting how many words are there with that
            ok=1
            for k in range(5):
                if valid[k]==2:
                    if word[k]!=cuv[k]:
                        ok=0
                if valid[k]==1:
                    num=0
                    for z in range(5):
                        if cuv[z]==word[k]:
                            num+=1
                    if num==0:
                        ok=0
                if valid[k]==0:
                    for z in range(5):
                        if cuv[z]==word[k]:
                            ok=0
            if ok==1:
                nr+=1
        entropy+=-math.log2(nr/11454) #here is (i think) how entropy should be calculated 
    print(entropy)
    if entropy>maxi:
        best=word
print(best)

#O(N^2*243)==many hours
