import random
import sys
# Alphabet = {"A": 0, "B": 0, "C": 0, "D":0, "E":0, "F":0, "G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0, "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}

# #cele mai bune 5 caractere
# char= ["A", "I", "E", "U", "R"]

# #vectorul de pozitii optime
# p= [0, 0, 0, 0, 0, 0]

#citim dictionarul si le punem in lines
with open('cuvinte_wordle.txt') as f:
    lines = f.readlines()

# #frecventa fiecarei litere din fiecare cuvant
# for cuvant in lines:
#     cuvant = cuvant.strip("\n")
#     for chr in cuvant:
#         Alphabet[chr]+=1

#  #sortare dupa literele cele mai frecvente
# Alphabet2 = dict(sorted(Alphabet.items(), key=lambda item: item[1]))
# print(Alphabet2)

# #gasirea pozitiilor optime pentru ch cele mai frecvnte
# for k in char:
# 	for cuv in lines:
# 		cuv = cuv.strip("\n")
# 		for i in range(len(cuv)):
# 			if cuv[i]==k:
# 				p[i]+=1
# 	print(f"Pentru {k}:") #R pentru pozitia 1; A pentru pozitia 2; U pentru pozitia 3; E pentru pozitia 4; I pentru pozitia 5    
    
# #Trebuie gasit un cuvant valid optim, care sa aiba cat mai multe similaritati cu cuv RAUEI
# 	for i in range (0,5):
# 		print(f"pe pozitia {i+1} este {p[i]}")
# 		p[i]=0
# 	print(end="\n")

# #gaseste primul cuv optim:
# #for cuv in lines:
# 	#if cuv[1]=="A" and cuv[3]=="E" and cuv[4]=="I" and cuv[0]=="R":
# 		#print(cuv)
# #deci,
# cuv="RATEI"

# #alege un cuv random + verificare dintre cuv ales si chosen
# valid = [0] * 5

# #seed
# random.seed(5)

# #vectorul valid e astfel: 2 e "green" 1 e "yellow" 0 e "No luck!"
# #chosen e cuvantul ales de calculator
# pozz=random.randrange(0,len(lines))
# chosen=lines[pozz]

# for i in range(5):
# 	if cuv[i]==chosen[i]:
# 		valid[i]=2
# 	else:
# 		for k in range(0,5):
# 			if cuv[i]==chosen[k]:
# 				valid[i]=1
# 				break
# 		else:
# 			valid[i]=0
# print(chosen)
# print(valid)

# #Cautam cele mai mic nr de cuvinte astfel incat sa "acoperim" tot alfabetul SI sa maximizam cele mai probabile pozitii ale acestor litere
# #Fiecare "if" este pentru fiecare pozitie si cu literele care se regasesc cel mai probabil pe acea pozitie
# for cuv in lines:
# 	if cuv[3]=="S" or cuv[3]=="C" or cuv[3]=="M" or cuv[3]=="P" or cuv[3]=="D" or cuv[3]=="B" or cuv[3]=="G":
# 		if cuv[1]=="A" or cuv[1]=="U" or cuv[1]=="O":
# 			if cuv[2]=="Z" or cuv[2]=="X":
# 				if cuv[0]=="V" or cuv[0]=="F" or cuv[0]=="H" or cuv[0]=="J" or cuv[0]=="K" or cuv[0]=="W" or cuv[0]=="Q":
# 					if cuv[4]=="I" or cuv[4]=="E" or cuv[4]=="T" or cuv[4]=="Y":
# 						print(cuv)


# #Din pacate, nu s-au gasit cuvinte cu Q si cu W, asa ca le-am luat separat, iar Q si W se gasesc aproape exclusiv pe pozitia 0, deoarece sunt putine cuvinte care contin aceste litere
# for cuv in lines:
# 	if cuv.find("Q")!=-1:
# 		print(cuv)
# for cuv in lines:
# 	if cuv.find("W")!=-1:
# 		print(cuv)

		

#varianta pentru calcularea validului
cuv=["QUICK", "WALON", "JIDOV", "HARHSE", "FIXEZ", "IMPUT", "RUGBY"] #cele 7 cuvinte care trec prin tot alfabetul
valid = [0] * 5
final = ["","","","",""]
letters={}

# #random value for testing the algorithm
random.seed(42) # seed pentru a avea acelas cuvant random
pozz=random.randrange(0,len(lines)) # o pozitie random intre 0 si len(lines)-1
chosen="CIUIN"


for word in cuv:
	for i in range(5):
		if word[i]==chosen[i]: #varianta cand caracterul apare pe aceeasi pozitie ca in chosen
			valid[i]=2
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

"""I want to change possible word to be pushed when they are good"""
#lista cu cuv posibile

nr=0 #intializam o valoare pentru a calcula cate cuvinte exista posibile

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
		
print(possible)		
	
if len(possible) == 1:
	print(f"cuvantul este {possible[0]}")
	sys.exit()
else:
	pass #cream o functie care trece prin cuvintele posibile si le verifica cu chosen		
	
# print(max)
print(len(possible))
print(possible)
