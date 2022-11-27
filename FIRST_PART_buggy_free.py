import random
with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

chosen=lines[random.randrange(1,11454)]
ok=0
while ok==0:
    maxi=0
    cuvant = input("Cuvant: ")
    cuvant = cuvant.upper()
    if len(cuvant)<5:
        print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
    else:
        for cuv in lines:
            k=0
            for i in range(5):
                if cuv[i]==cuvant[i]:
                    k+=1
            if k>maxi:
                maxi=k
        if maxi!=5 or len(cuvant)!=5:
            print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
        else:
            ok=1

nr=0
while cuvant.strip('\n')!=chosen.strip('\n'):
    valid=[0]*5
    for i in range(5):
        if cuvant[i]==chosen[i]:
            valid[i]=2
        else:
            if chosen.find(cuvant[i])!=-1:
                if valid[i]!=2:
                    nr=1
                    for j in range(i+1,5):
                        if cuvant[i]==cuvant[j] and cuvant[i]!='' and valid[i]!=2:
                            nr=nr+1
                            cuvant=cuvant[:j]+'0'+cuvant[j+1:]
                    if nr>1 and cuvant[i]!='0' and valid[i]!=2:
                        valid[i]=1
                    else:
                        if nr==1 and valid[i]!=2:
                            valid[i]=1
                
                    
    print(valid)
        
    ok=0
    while ok==0:
        maxi=0
        cuvant = input("Cuvant: ")
        cuvant = cuvant.upper()
        if len(cuvant)<5:
            print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
        else:
            for cuv in lines:
                k=0
                for i in range(5):
                    if cuv[i]==cuvant[i]:
                        k+=1
                if k>maxi:
                    maxi=k
            if maxi!=5 or len(cuvant)!=5:
                print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
            else:
                ok=1
print(f"Bravo! Cuvantul era intr-adevar, {chosen}")
