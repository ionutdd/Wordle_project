import random
with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

chosen=lines[random.randrange(1,11454)]

maxi=0
while maxi!=5:
    cuvant = input("Cuvant: ")
    cuvant = cuvant.upper()
    for cuv in lines:
        k=0
        for i in range(5):
            if cuv[i]==cuvant[i]:
                k+=1
        if k>maxi:
            maxi=k
    if maxi!=5:
        print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
while cuvant.strip('\n')!=chosen.strip('\n'):
    valid=[0]*5
    for i in range(5):
        if cuvant[i]==chosen[i]:
            valid[i]=2
        else:
            if chosen.find(cuvant[i])!=-1:
                if valid[i]!=2:
                    valid[i]=1
    print(valid)
    maxi=0
    while maxi!=5:
        cuvant = input("Cuvant: ")
        cuvant = cuvant.upper()
        for cuv in lines:
            k=0
            for i in range(5):
                if cuv[i]==cuvant[i]:
                    k+=1
            if k>maxi:
                maxi=k
        if maxi!=5:
            print("Cuvantul introdus nu apare in dictionar! Incearca altul!")
print(f"Bravo! Cuvantul era intr-adevar, {chosen}")
