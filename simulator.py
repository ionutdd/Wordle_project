with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

#varianta pentru calcularea validului
sum = 0
max = 0
errors = 0
gresit = []

cuv=["QUICK", "WALON", "JIDOV", "HARHSE", "FIXEZ", "IMPUT", "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
for chosen in lines:
    valid = [0] * 5
    final = ["","","","",""]
    letters={}

    # #random value for testing the algorithm
    # random.seed(42) # seed pentru a avea acelas cuvant random
    # pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
    # chosen="ACARI"
    print(f"the chosen word is : {chosen}")

    for word in cuv:
        for i in range(5):
            if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
                valid[i]=2
                if final[i]=="":
                    final[i] = word[i]
                if word[i] not in letters :  #Punem caracterul in letters
                    letters[word[i]] = [0,1,2,3,4]
                    letters[word[i]].remove(i)
            else:
                for k in range(5):
                    if word[i]==chosen[k]: #varianta cand caracterul se afla in cuvanta si pe pozitia gresita
                        valid[i]=1
                        if word[i] not in letters : #punem caracterul in letters
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
            print(f"cuvantul este {final}")
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

    print(len(possible))
    if len(possible) == 0:
        errors+=1	
    sum+=len(possible)
    if len(possible) > max:
        max = len(possible)

    # # print(max)
    # print(len(possible))
    # print(possible)
print(sum/11454)
print(max)

print(f"numarul de cuvinte gresite este:{errors}")

# failed words : ['BIBIC', 'BIBIL', 'BIFID', 'BIGII', 'BINIS', 'BIRIS', 'BITII', 'CILII', 'CINIC', 'CIPIC', 'CIRII', 'CIRIP', 'CIRIS', 'CITII', 'CITIM', 'CITIT',
#                 'CIUIN', 'CIVIC', 'CIVIL', 'CIVIT', 'DIGIT', 'DILIA', 'DILIE', 'DILII', 'DILIM', 'DILIT', 'DILIU', 'DIMIA', 'DIMIE', 'DIMII', 'DIOIC', 'DIRIG',
#                 'DIVID', 'DIVIN', 'DIXIE', 'FILIT', 'FINII', 'FINIM', 'FINIS', 'FINIT', 'FIRII', 'FIRIZ', 'FISIC', 'FISIU', 'FITIL', 'FIZIC', 'GIMIA', 'GIMIE', 
#                 'GIMII', 'GINII', 'GINIM', 'GINIT', 'HIOID', 'HIPIC', 'HITIT', 'JIBII', 'JILIP', 'JIPII', 'JITIA', 'JITIE', 'JITII', 'KAZOO', 'KIPII', 'LICIT', 
#                 'LIDIC', 'LIGII', 'LIMIN', 'LINIA', 'LINIE', 'LINII', 'LINIO', 'LIPIA', 'LIPIE', 'LIPII', 'LIPIM', 'LIPIT', 'LIRIC', 'LISII', 'LITIA', 'LITIC', 
#                 'LITIE', 'LITII', 'LITIU', 'LIVID', 'MICII', 'MICIM', 'MICIT', 'MIDIA', 'MIDIE', 'MIDII', 'MIEII', 'MIJII', 'MIJIM', 'MIJIT', 'MIMIC', 'MIMII', 
#                 'MINIA', 'MINIE', 'MINIM', 'MINIU', 'MIRIA', 'MIRIE', 'MIRII', 'MISIA', 'MISIE', 'MISII', 'MISIL', 'MISIR', 'MISIT', 'MITIC', 'MITII', 'MITIM', 
#                 'MITIT', 'MIXIA', 'MIXIE', 'MIXII', 'MIZID', 'NICIO', 'NIMIC', 'NISIP', 'NITII', 'NIXIS', 'OIDIA', 'OIDIE', 'OIDII', 'PICII', 'PIEII', 'PILII', 
#                 'PILIM', 'PILIT', 'PINII', 'PIPIT', 'PISIC', 'PITIC', 'PITIG', 'PITII', 'PITIM', 'PITIS', 'PITIT', 'PIUIA', 'PIUIE', 'PIUIT', 'PIUUU', 'REMUU', 
#                 'RICIN', 'RIDIC', 'RIFII', 'RIGID', 'RIGII', 'RITIN', 'RIZIC', 'RIZIL', 'SIBIR', 'SICII', 'SIGIL', 'SILII', 'SILIM', 'SILIT', 'SIMIT', 'SINIA', 
#                 'SINIE', 'SINII', 'SIPII', 'SIRIC', 'SIVII', 'TIBIA', 'TIBII', 'TIFIC', 'TIMIA', 'TIMID', 'TIMIE', 'TIMII', 'TIMIN', 'TIMIR', 'TIPIA', 'TIPIC', 
#                 'TIPIE', 'TIPII', 'TIPIM', 'TIPIS', 'TIPIT', 'TISII', 'TIUIA', 'TIUIE', 'TIUII', 'TIUIM', 'TIUIT', 'TIVIC', 'TIVII', 'TIVIL', 'TIVIM', 'TIVIT', 
#                 'TIZIC', 'TIZII', 'UICII', 'UIMII', 'UIMIM', 'UIMIT', 'UIRII', 'UITIT', 'UIUIU', 'VACUU', 'VICIA', 'VICIE', 'VICII', 'VICIU', 'VIGIA', 'VIGIE', 
#                 'VIGII', 'VIGIL', 'VILII', 'VILIT', 'VINIA', 'VINIE', 'VINII', 'VINIL', 'VINIU', 'VIOII', 'VIPIA', 'VIPIE', 'VIPII', 'VIRID', 'VIRIL', 'VISIN', 
#                 'VITII', 'VITIU', 'VIZII', 'VIZIR', 'WIDIA', 'WIDII', 'XIFIA', 'XIFIE', 'XIFII', 'XILIT', 'ZIDII', 'ZIDIM', 'ZIDIT', 'ZISII']
