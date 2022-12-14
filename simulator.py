with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

#varianta pentru calcularea validului
sum = 0
max = 0
errors = 0
gresit = []
fr=[0]*25
cuv=["IMPUT", "HARSI", "WALON" , "FIXEZ" , "JIDOV" , "QUICK" , "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
for chosen in lines:
    route=chosen.strip('\n')+","
    contor=0
    valid = [0] * 5
    final = ["","","","",""]
    letters={}
    fixed=0
    done=0
    kk=0
    # #random value for testing the algorithm
    # random.seed(42) # seed pentru a avea acelas cuvant random
    # pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
    # chosen="ACARI"

    for word in cuv:
        if kk==5:
            break
        contor+=1
        fixed=contor
        for i in range(5):
            if word[i]!=chosen[i]:
                fixed=0
        if fixed==contor:
            done=contor
            route+=word
        else:
            route+=word+","
        for i in range(5):
            if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
                valid[i]=2
                if final[i]=="":
                    final[i] = word[i]
                if word[i] not in letters :  #Punem caracterul in letters
                    kk+=1
                    letters[word[i]] = [0,1,2,3,4]
                    letters[word[i]].remove(i)
            else:
                for k in range(5):
                    if word[i]==chosen[k]: #varianta cand caracterul se afla in cuvanta si pe pozitia gresita
                        valid[i]=1
                        if word[i] not in letters : #punem caracterul in letters
                            kk+=1
                            letters[word[i]] = [0,1,2,3,4]
                            letters[word[i]].remove(i)
                        break
                else:
                    valid[i]=0 #varianta cand caracterul nu apare deloc in cuvant
        for i in range(5):
            if final[i]=="":
                break
        else:
            final = "".join(final)
            # sys.exit()
            
        for letter in letters:
            for i in range(5):
                if final[i] != "" and i in letters[letter]:
                    letters[letter].remove(i)
    
    #lista cu caracterele posibile
    nr = 0
    possible=[] #cuvintele din dictionar posibile formate cu caracterele din letters
    for word in lines:
        ok=1
        for l in letters:  #daca caracterul nu se afla in letters
            if l not in word: 
                ok=0
                break
        if ok == 1:
            for i in range(len(word)-1):
                if word[i] not in letters: #daca caracterul nu se afla in letters
                    ok=0
                elif final[i]!="": 
                    if word[i]!=final[i]: #daca caracterul e deja aparut in final
                        ok=0
                else:
                    for poz in letters[word[i]]:
                        if i == poz:
                            break
                    else:
                        ok =0

        
        if ok==1:
            
            possible.append(word.strip("\n")) #pune cuvantele in lista fara \n

            nr+=1 #verificam cate cuvinte sunt posibile de incercat 
    if done==0:
        for j in range(len(possible)-1,-1,-1):
            contor+=1
            if possible[j].strip("\n")==chosen.strip("\n"):
                route+=possible[j]
            else:
                route+=possible[j]+","
            if possible[j].strip("\n")==chosen.strip("\n"):
                break
    if done!=0:
        contor=done
    sum+=contor
    fr[contor]+=1
    if contor>max:
        max=contor
    print(route)

print(sum/len(lines))
