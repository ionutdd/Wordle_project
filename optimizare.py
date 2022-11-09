#################################
#DE REZOLVAT LETTERS BUGG
################################
import random

with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

random.seed(42) # seed pentru a avea acelas cuvant random
pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
chosen="IMPUI"

#verific daca a gasit pt toate cuvintele
total = len(lines)
sum = 0
max = 0
errors = 0
gresit = []
fr=[0]*12
cuv=["IMPUT", "HARSI", "WALON", "FIXEZ" , "JIDOV" , "QUICK" , "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul


route=chosen.strip('\n')+","
contor=0 #contirizam fiecare incercare
valid = [0] * 5 
final = ["","","","",""] #cuvantul final
letters={} #unde o sa se stocheze caracterele posibile si pozitiile posibile
fixed=0
done=0


print(chosen)
# print("Cuvintele prin care a ajuns la cuvantul ales sunt:") ###########

for word in cuv:
    if len(letters) == 5: #daca cuvantul nostru are caractere distincte
        break
    contor+=1 #incercam un cuvant
    route+=word+"," #adaugam cuvantul la incercari
        
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
        done=contor #cuvantul a fost gasit
        total-=1
        break
        
    for letter in letters:
        for i in range(5):
            if final[i] != "" and i in letters[letter]:
                letters[letter].remove(i)
    # print(word) ############################################
    
#lista cu caracterele posibile
print(letters)

terminat = False
for word in lines:
    if terminat: #se opreste atunci cand a gasit cuvantul (line 144)
        break
    if done: #daca s-a gasit in primele 7 cuvinte
        break

    ok=1
    for l in letters:  #daca caracterul nu se afla in letters
        if l not in word: 
            ok=0
            break
    if ok == 1:
        for i in range(len(word)-1):
            if word[i] not in letters: #daca caracterul nu se afla in letters
                ok=0
                break
            elif final[i]!="": 
                if word[i]!=final[i]: #daca caracterul nu seamna cu ce este in final
                    ok=0
                    break
            else:
                for poz in letters[word[i]]:
                    if i == poz:
                        break
                else:
                    ok = 0

        
    if ok == 1:
        word = word.strip("\n")
        route+=word+","
        contor+=1 #adaugam la contor cand il testam cu chosen

        #############################
        #trying WORD with the chosen
        #############################
        for i in range(5):
            if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
                valid[i]=2
                if final[i]=="":
                    final[i] = word[i]
                    letters[word[i]].remove(i)
            else:
                for k in range(5):
                    if word[i]==chosen[k]: #varianta cand caracterul se afla in cuvanta si pe pozitia gresita
                        valid[i]=1
                        letters[word[i]].remove(i)
                        break
                else:
                    valid[i]=0 #varianta cand caracterul nu apare deloc in cuvant

        for letter in letters:
            for i in range(5):
                if final[i] != "" and i in letters[letter]:
                    letters[letter].remove(i)

        ############################
        #verificam daca este cuvantul final
        ############################
        for i in range(5):
            if final[i]=="":
                break
        else:
            final = "".join(final)
            total-=1
            terminat=True
            # sys.exit()

print(f"Incercari: {contor}")
sum+=contor
fr[contor]+=1

# print(total)
# for i in range(len(fr)):
#     print(f"numarul de incercari pt {i} este {fr[i]}")

# print(sum/len(lines))
# print()