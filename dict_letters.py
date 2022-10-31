import random

with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

cuv=["QUICK", "WALON", "JIDOV", "HARHSE", "FIXEZ", "IMPUT", "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
valid = [0] * 5
final = ["","","","",""]
letters= {}

#random value for testing the algorithm
random.seed(1000) # seed pentru a avea acelas cuvant random
pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
# chosen=lines[pozz]\
chosen = "ACARI"

for word in cuv:
	for i in range(5):
		if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
			valid[i]=2
			final[i] = word[i]
			if word[i] not in letters :  #Punem caracterul in letters
				letters[word[i]] = [0,1,2,3,4]
			
			letters[word[i]].pop(i)
		else:
			for k in range(5):
				if word[i]==chosen[k]: #varianta cand caracterul se afla in cuvanta si pe pozitia gresita
					valid[i]=1
					if word[i] not in letters : #punem caracterul in letters
						letters[word[i]] = [0,1,2,3,4]
					if letters[word[i]][i] == i:
						letters[word[i]].pop(i)
					break
			else:
				valid[i]=0 #varianta cand caracterul nu apare deloc in cuvant
	print(valid) #testing in terminal
	valid = [0] * 5 #resetam valid pentru a calcula trece prin urmatorul cuvant

for letter in letters:
	for i in range(5):
		if final[i] != "" and i in letters[letter]:
			letters[letter].pop(i)
	
print(f"letter choices are: {letters} ") #din ce litere este format cuvantul nostru
print(f"our first guess is : {final}") #final este cuvantul care il ghicim
print(f"the chosen word is : {chosen}") #testing in terminal (vedem care e cuvantul random)
